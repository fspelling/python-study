import os
import tempfile
import boto3
from PIL import Image

SIZE = (128, 128)
DEST_BUCKET = os.environ['DEST_BUCKET']
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    for record in event['Records']:
        if 's3' in record:
            source_bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            thumb = f'thumb-{key}'

            with tempfile.TemporaryDirectory() as tempdir:
                download_path = os.path.join(tempdir, key)
                s3.download_path(source_bucket, key, download_path)

                upload_path = os.path.join(tempdir, thumb)
                generate_thumbnail(download_path, upload_path)

                s3.upload_path(DEST_BUCKET, thumb, upload_path)
                print(f'Thumbnail image saved at {DEST_BUCKET}/{thumb}')


def generate_thumbnail(source_path, dest_path):
    print('Generating thumbnail from:', source_path)

    with Image.open(source_path) as image:
        image.thumbnail(SIZE)
        image.save(dest_path)
