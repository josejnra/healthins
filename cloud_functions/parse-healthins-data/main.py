from uuid import uuid4

message_example = {
  "columns": [
    "NIC_PT",
    "NUI_PT",
    "NAME",
    "time",
    "state",
    "county"
  ],
  "rows": [
    [
      "29370",
      "7161",
      "Anderson County, TX",
      "2017",
      "48",
      "001"
    ],
    [
      "56065",
      "15499",
      "Angelina County, TX",
      "2017",
      "48",
      "005"
    ]
  ]
}



import base64
import json
from datetime import datetime

from google.cloud import storage


def main(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    client = storage.Client.from_service_account_json('/home/jose/Projects/PycharmProjects/etus/key.json')
    bucket = client.get_bucket('healthins-parsed-data')

    now = datetime.utcnow()

    blob2 = bucket.blob(
        f"{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/{now.strftime('%Y%m%d%H%M%S')}_{uuid4().hex}.json")
    blob2.upload_from_string(pubsub_message, content_type='application/json')


import pandas as pd
import dask.dataframe as dd
from pprint import pprint
import gcsfs

if __name__ == '__main__':
    pandas_df = pd.DataFrame({'x': [2, 3, 2, 3, 4, 10, 11, 12, 13], 'y': [1, 0, 0, 0, 1, 1, 0, 1, 1]})
    # Bonus convert a Pandas DF to Dask DF
    dask_df = dd.from_pandas(pandas_df, npartitions=2)
    dask_df = dask_df.reset_index(drop=True)
    dask_df.to_parquet('gs://healthins-parsed-data/my_parquet_file',
                       storage_options={'token': '/home/jose/Projects/PycharmProjects/etus/key.json'})  # use a service account key with correct permissions

    # df = dd.read_parquet('gs://gdecarlo-cloud-tests.appspot.com/test_parquet',
    #                      storage_options={'token': '/home/jose/Projects/PycharmProjects/etus/key.json'})
    # df.head()
