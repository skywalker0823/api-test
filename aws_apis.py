# For AWS api calls
import boto3, os, sys, dotenv

dotenv.load_dotenv()

class AWSAPIs():
    def __init__(self):
        pass

    def get_s3_all_buckets(self):
        s3 = boto3.resource('s3')
        return [bucket.name for bucket in s3.buckets.all()]

    def get_s3_bucket_objects(self, bucket_name):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        return [obj.key for obj in bucket.objects.all()]
    
    #Route53
    def get_hosted_zones(self):
        client = boto3.client('route53')
        response = client.list_hosted_zones()
        return response['HostedZones']