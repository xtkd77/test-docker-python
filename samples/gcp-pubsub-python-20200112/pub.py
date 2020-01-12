#!/usr/bin/env python
"""
python3 pub.py project_id topic_id key.json
"""
import sys, os, time, datetime
from google.cloud import pubsub_v1


project_id, topic_name = sys.argv[1], sys.argv[2]
cred_file = sys.argv[3] 

publisher = pubsub_v1.publisher.Client.from_service_account_file(cred_file)
#publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print("project_id={}".format(project_id))
print("topic_path={}".format(topic_name))

cnt = 0
while True:
    data = u"Message from test publisher {}".format(cnt) + datetime.datetime.now().isoformat(" ")
    data = data.encode("utf-8")
    print("Publish: " + data.decode("utf-8", "ignore") )
    future = publisher.publish(topic_path, data=data)
    print("return ", future.result())
    time.sleep(0.25)
    cnt = cnt + 1
