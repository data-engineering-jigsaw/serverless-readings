import requests
import pandas as pd
def lambda_handler(event, context):
    print("Hello world")
    
    url = "https://data.texas.gov/resource/naix-2893.json"
    records = pd.read_json(url).to_dict('records')
    return {
        'statusCode': 200, 'records': records[:2]
    }