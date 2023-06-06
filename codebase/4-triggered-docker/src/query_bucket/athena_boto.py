import time

import boto3
import pandas as pd
from io import BytesIO

s3_client = boto3.client("s3")
athena_client = boto3.client("athena")

def query_athena(query, db_name, output_bucket_folder):
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": db_name},
        ResultConfiguration={
            "OutputLocation": output_bucket_folder,
            "EncryptionConfiguration": {"EncryptionOption": "SSE_S3"},
        },
    )
    return response

def read_from_bucket(output_bucket_name, output_folder, query_response):
    obj_name = f"{output_folder}/{query_response['QueryExecutionId']}.csv"
    obj = s3_client.get_object(Bucket=output_bucket_name, Key=obj_name)
    data = obj['Body'].read()
    csv = BytesIO(data)
    df = pd.read_csv(csv)
    return df

def get_query_results(output_bucket_name, output_folder, query_response):
    while True:
        try:
            athena_client.get_query_results(QueryExecutionId=query_response["QueryExecutionId"])
            break
        except Exception as err:
            if "not yet finished" in str(err):
                time.sleep(0.01)
            else:
                raise err
    df = read_from_bucket(output_bucket_name, output_folder, query_response)
    return df