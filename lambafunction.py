import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    # TODO implement
    payload = json.loads(json.dumps(event))
    payload_data = str(payload['body'])
    print(payload_data)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                      ContentType='text/csv',
                                      Body=payload_data)
    result = json.loads(response['Body'].read().decode())
    preds = {"Prediction": result}
    response_dict = {
          "statusCode": 200,
          "body": json.dumps(preds)
                }
    return response_dict

