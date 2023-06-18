import json
import os
import boto3

INSTANCE_ID = os.getenv('INSTANCE_ID')

def start():
    try:
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(INSTANCE_ID)
        instance.start()
    except Exception as e:
        print(e)

def stop():
    try:
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(INSTANCE_ID)
        instance.stop()
    except Exception as e:
        print(e)


def callback(event: dict, context: dict):
    action = event['data']['name']
    print(f"action = {action}")

    if action == "start":
        text = '起こしたからちょい待ち'
        start()

    if action == "stop":
        text = 'もう少ししたら止まるよ'
        stop()

    print(text)
    return {
        "type": 4,  # 4=ChannelMessageWithSource / 5=DeferredChannelMessageWithSource
        "data": {
            "content": text
        }
    }


