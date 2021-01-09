import json
import base64
from uuid import uuid4
from datetime import datetime

import pandas as pd
import dask.dataframe as dd


def main(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    pandas_df = pd.DataFrame(pubsub_message['rows'], columns=pubsub_message['columns'])

    dask_df = dd.from_pandas(pandas_df, npartitions=1)
    dask_df = dask_df.reset_index(drop=True)

    now = datetime.utcnow()
    path = f"gs://healthins-parsed-data/{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/{uuid4().hex}"
    dask_df.to_parquet(path,
                       storage_options={'token': './key.json'})
