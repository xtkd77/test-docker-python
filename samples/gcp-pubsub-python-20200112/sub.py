#!/usr/bin/env python3

import os, sys, time, datetime
from google.cloud import pubsub_v1

def callback(message):
    #print(f"receive: {message}")
    now = datetime.datetime.now()
    print( "msg = \"" + message.data.decode("utf-8") + "\"" +  "  [" + now.isoformat(" ") + "]")
    message.ack()

project_id = sys.argv[1]
sub_name = sys.argv[2]
cred_file = sys.argv[3] 
#cred_file = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

subscriber = pubsub_v1.subscriber.Client.from_service_account_file(cred_file)
#subscriber = pubsub_v1.SubscriberClient()
subpath = subscriber.subscription_path(project_id, sub_name)
#subpath = f"projects/{project_id}/subscriptions/{sub_name}"
flow_control = pubsub_v1.types.FlowControl(max_messages=2)

subscriber.subscribe(subpath, callback=callback, flow_control = flow_control)

input()


