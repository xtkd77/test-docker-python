python3 -m venv testenv
source testenv/bin/activate
pip3 install -r requirements.txt
#export GOOGLE_APPLICATION_CREDENTIALS="./key.json"
#export TOPIC_ID="topic0000"

python3 pub.py $GOOGLE_CLOUD  $TOPIC_ID key.json
