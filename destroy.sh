#!/bin/bash

source .env

eksctl delete cluster "$CLUSTER_NAME" \
    --region "$CLUSTER_REGION" \
    --profile nufuturo