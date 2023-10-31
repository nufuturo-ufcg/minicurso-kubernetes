#!/bin/bash

source .env

# eksctl create cluster --name "$CLUSTER_NAME" --region "$CLUSTER_REGION" --profile nufuturo

rm -rf roles
mkdir roles

python3 create-roles.py