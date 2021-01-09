import pandas as pd
import dask.dataframe as dd
from uuid import uuid4
from datetime import datetime


def main(event, context):

    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = event['data']

    pandas_df = pd.DataFrame(pubsub_message['rows'], columns=pubsub_message['columns'])

    dask_df = dd.from_pandas(pandas_df, npartitions=1)
    dask_df = dask_df.reset_index(drop=True)

    now = datetime.utcnow()
    path = f"gs://healthins-parsed-data/{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/{uuid4().hex}"
    dask_df.to_parquet(path,
                       storage_options={'token': '/home/jose/Projects/PycharmProjects/etus/key.json'})


    # client = storage.Client.from_service_account_json('/home/jose/Projects/PycharmProjects/etus/key.json')
    # bucket = client.get_bucket('healthins-parsed-data')
    #
    # now = datetime.utcnow()
    #
    # blob2 = bucket.blob(
    #     f"{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/{now.strftime('%Y%m%d%H%M%S')}_{uuid4().hex}.json")
    # blob2.upload_from_string(pubsub_message, content_type='application/json')


# if __name__ == '__main__':
#     pandas_df = pd.DataFrame(message_example['rows'], columns=message_example['columns'])
#
#     dask_df = dd.from_pandas(pandas_df, npartitions=1)
#     dask_df = dask_df.reset_index(drop=True)
#
#     now = datetime.utcnow()
#     path = f"gs://healthins-parsed-data/{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}"
#     dask_df.to_parquet(path,
#                        storage_options={'token': '/home/jose/Projects/PycharmProjects/etus/key.json'})  # use a service account key with correct permissions
#
#     df = dd.read_parquet(path,
#                          storage_options={'token': '/home/jose/Projects/PycharmProjects/etus/key.json'})
#
#     print(df.head())
