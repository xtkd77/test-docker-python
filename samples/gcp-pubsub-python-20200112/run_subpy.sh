python3 -m venv testenv
source testenv/bin/activate
pip3 install -r requirements.txt
#export GOOGLE_APPLICATION_CREDENTIALS="./key.json"
export SUBSCRIPTION_ID="subsc0000"

python3 sub.py $GOOGLE_CLOUD  $SUBSCRIPTION_ID key.json


