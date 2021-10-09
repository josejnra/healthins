import json
from datetime import datetime

from google.cloud import storage


class GCPStorage:
    pass


if __name__ == '__main__':
    client = storage.Client.from_service_account_json('/home/jose/Projects/PycharmProjects/healthins/key.json')
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('healthins-raw-data')
    # Then do other things...
    now = datetime.utcnow()

    # blob = bucket.get_blob(f'{now.year}/{now.month}/{now.day}/{now.hour}/file.txt')
    # print(blob.download_as_string())
    # blob.upload_from_string('New contents!')

    d = json.dumps(dict(name="jose", age=27, id=42))
    blob2 = bucket.blob(f"{now.year}/{'{:02d}'.format(now.month)}/{'{:02d}'.format(now.day)}/{'{:02d}'.format(now.hour)}/file.json")
    blob2.upload_from_string(d, content_type='application/json')
