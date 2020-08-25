import json

def handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({
            'contents': [
                'Hello from Lambda! 2',
                'test'
            ]
        })
    }
