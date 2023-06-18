import json
import os
import boto3

def start(instance_id):
    try:
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(instance_id)
        instance.start()
    except Exception as e:
        print(e)

def stop(instance_id):
    try:
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(instance_id)
        instance.stop()
    except Exception as e:
        print(e)


def callback(event: dict, context: dict):
    action = event['data']['name']
    instance_id = event['data']['instance_id']

    if action == "start":
        text = '起こしたからちょい待ち'
        start(instance_id)

    if action == "stop":
        text = 'もう少ししたら止まるよ'
        stop(instance_id)

    print(text)
    return {
        "type": 4,  # 4=ChannelMessageWithSource / 5=DeferredChannelMessageWithSource
        "data": {
            "content": text
        }
    }


