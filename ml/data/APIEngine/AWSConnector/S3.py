import boto3
from AWSConnector import Config
from botocore.exceptions import ClientError


class S3:
    """
     This class let to get connected to S3 service and manopulate the objetcs
     stores there.
    """
    session = None
    client = None

    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=Config.instance().get_value('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=Config.instance().get_value('AWS_SECRET_ACCESS_KEY'),
            region_name=Config.instance().get_value('AWS_REGION')).resource('s3')
        self.client = boto3.client('s3',
                                   aws_access_key_id=Config.instance().get_value('AWS_ACCESS_KEY_ID'),
                                   aws_secret_access_key=Config.instance().get_value('AWS_SECRET_ACCESS_KEY'),
                                   region_name=Config.instance().get_value('AWS_REGION'))

    def get_bucket(self, bucket):
        return self.session.Bucket(bucket)

    def upload_file(self, file, bucket_name, file_name):
        """
        Upload an object to AWS
        """
        try:
            return self.get_bucket(bucket_name).put_object(Body=file, Key=file_name)
        except ClientError as e:
            print(e)
            return e

    def get_object(self, key):
        obj = self.get_bucket(Config.instance().get_value('AWS_S3_BUCKET')).Object(key=key)
        print(obj)
        return obj.get()
