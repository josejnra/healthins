import json
import base64
import copy
from typing import List
from uuid import uuid4
from datetime import datetime

import pandas as pd
import dask.dataframe as dd

from schemas import parse_name, HealthinsSchema


def main(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    columns = map(parse_name, map(str.upper, pubsub_message['columns']))
    values = apply_schema(columns, pubsub_message['rows'])
    pandas_df = pd.DataFrame([item.__dict__ for item in values])

    dask_df = dd.from_pandas(pandas_df, npartitions=1)
    dask_df = dask_df.reset_index(drop=True)

    now = datetime.utcnow()
    path = f"gs://healthins-parsed-data/{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/{uuid4().hex}"
    dask_df.to_parquet(path,
                       storage_options={'token': './key.json'})


def apply_schema(columns, rows) -> List[HealthinsSchema]:
    new_columns = list(copy.deepcopy(columns))

    def map_columns_to_rows(row):
        mapped = dict()
        for column, value in zip(new_columns, row):
            mapped[column] = value

        return mapped

    items = map(map_columns_to_rows, rows)

    for item in items:
        yield HealthinsSchema(**item)
