#!/bin/bash

source .env

rm -rf roles && mkdir roles
rm -rf rolebindings && mkdir rolebindings

eksctl create cluster \
    --name "$CLUSTER_NAME" \
    --region "$CLUSTER_REGION" \
    --profile nufuturo

create_namespace() {
    kubectl create namespace "$1"
}

create_iamidentitymapping() {
    eksctl create iamidentitymapping \
        --cluster "$CLUSTER_NAME" \
        --region "$CLUSTER_REGION" \
        --arn "$1" \
        --username "$2"-user \
        --profile nufuturo
}

for user in "${!ROLES[@]}"; do
    role="${ROLES[$user]}"

    create_namespace "$user"

    python3 create-role.py "$user"
    python3 create-rolebinding.py "$user"

    kubectl apply -f roles/"$user"-role.yaml
    kubectl apply -f rolebindings/"$user"-rolebinding.yaml

    create_iamidentitymapping "$role" "$user"
done


