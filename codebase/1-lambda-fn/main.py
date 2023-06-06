def lambda_handler(event, context):
    print("Hello world")
    
    url = "https://data.texas.gov/resource/naix-2893.json"
    
    return {
        'statusCode': 200, 'records': 'ok'
    }