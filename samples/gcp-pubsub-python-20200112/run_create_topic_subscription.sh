export TOPIC_ID="topic0000"
export SUBSCRIPTION_ID="subsc0000"
gcloud pubsub topics create ${TOPIC_ID}
gcloud pubsub subscriptions create ${SUBSCRIPTION_ID} --topic=${TOPIC_ID}

echo "------"
echo "gcloud pubsub topics list"
echo "------"
gcloud pubsub topics list
echo "------"
echo "gcloud pubsub subscriptions list"
echo "------"
gcloud pubsub subscriptions list

gcloud pubsub publish topics publish ${TOPIC_ID} --message "Hello World!"


