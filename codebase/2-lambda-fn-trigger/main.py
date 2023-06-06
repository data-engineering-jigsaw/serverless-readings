
def lambda_handler(event, context):
    print("Function called")
    
    return {
        'statusCode': 200, 'records': 'function called'
    }