#!/bin/bash

source .env

# eksctl create cluster --name "$CLUSTER_NAME" --region "$CLUSTER_REGION" --profile nufuturo

rm -rf roles && mkdir roles
rm -rf rolebindings && mkdir rolebindings

python3 create-roles.py
python3 create-rolebindings.py