import json
import boto3
import requests
import io
import pandas as pd
s3 = boto3.client('s3')

def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()

def cleaned_name(rest_name):
    cleaned_name = rest_name.lower().replace(' ', '_')
    return cleaned_name

def upload(text, bucket, file_name):
    s3.put_object(
        Body=text,
        Bucket=bucket,
        Key=file_name
    )

def request_and_download_locally(name):
    receipts = find_receipts(name)
    receipts_df = pd.DataFrame(receipts)
    file_name = f'{cleaned_name(name)}.csv'
    receipts_df.to_csv(file_name, index = False)
    df = pd.read_csv(file_name)
    return df, file_name

def upload_and_read(file_name, bucket_name):
    s3.upload_file(file_name, bucket_name, file_name)
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    text = obj['Body'].read()
    return text