import boto3
import os
import json

def lambda_handler(event, context):

    # Retrieve the topic ARN from the environment variables.

    TOPIC_ARN = os.environ['topicARN']
    print("Topic ARN =", TOPIC_ARN)

    # Create an S3 client and retrieve the S3 bucket name and file name (object key) from the event object.

    s3Client = boto3.resource('s3')

    record = event['Records'][0]
    bucketName = record['s3']['bucket']['name']
    print("bucketName =", bucketName)
    objectKey = record['s3']['object']['key']
    print("objectKey =", objectKey)

    # Read the contents of the file.

    textFile = s3Client.Object(bucketName, objectKey)
    fileContent = textFile.get()['Body'].read()

    print("fileContent =", fileContent)

    # Count the number of words in the file.

    wordCount = len(fileContent.split())
    print('Number of words in text file:', wordCount)

    # Create an SNS client, and format and publish a message containing the word count to the topic.

    snsClient = boto3.client('sns')
    message =  'The word count in the file ' + objectKey + ' is ' + str(wordCount) + '.'

    response = snsClient.publish(
        TopicArn = TOPIC_ARN,
        Subject = 'Word Count Result',
        Message = message
    )

    # Return a successful function execution message.

    return {
        'statusCode': 200,
        'body': json.dumps('File successfully processed by wordCounter Lambda function')
    }
