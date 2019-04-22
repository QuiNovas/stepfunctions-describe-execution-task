import boto3
import json
import logging.config

CLIENT = boto3.client('stepfunctions')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Processing event :{}'.format(json.dumps(event)))
    response = CLIENT.describe_execution(
        executionArn=event['ExecutionArn']
    )
    response['startDate'] = response['startDate'].isoformat()
    response['stopDate'] = response['stopDate'].isoformat()
    response['input'] = json.loads(response['input'])
    if 'output' in response:
        response['output'] = json.loads(response['output'])
    if 'ResponseMetadata' in response:
        del response['ResponseMetadata']
    return response
    