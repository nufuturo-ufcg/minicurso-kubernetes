# Minicurso Kubernetes

## Pré-requisitos

1. [Python3](https://www.python.org/downloads/)
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. [gimme-aws-creds](https://github.com/Nike-Inc/gimme-aws-creds)
4. [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

### Conectando-se ao cluster

1. Siga esse [tutorial](https://github.com/nufuturo-ufcg/stress-testing-automation/blob/main/doc/aws-credentials.md) para atualizar suas credenciais da AWS;
2. Execute o comando abaixo para configurar o kubectl:
```bash
aws eks update-kubeconfig --name minicurso-kubernetes --region sa-east-1 --profile nufuturo
```
3. Execute o comando abaixo para alterando `<meu-namespace>` pelo prefixo do seu email ccc, com hífen no lugar do ponto. Ex: carlos-ribeiro.:
```bash
kubectl config set-context --current --namespace=<meu_namespace>
```

## Mãos a obra

### Capítulo 1 - Deploy

#### Introdução

Once you have a running Kubernetes cluster, you can deploy your containerized applications on top of it. To do so, you create a Kubernetes Deployment. The Deployment instructs Kubernetes how to create and update instances of your application. Once you've created a Deployment, the Kubernetes control plane schedules the application instances included in that Deployment to run on individual Nodes in the cluster.

You can create and manage a Deployment by using the Kubernetes command line interface, kubectl.

When you create a Deployment, you'll need to specify the container image for your application and the number of replicas that you want to run.

The common format of a kubectl command is: kubectl action resource (?)

Let’s deploy our first app on Kubernetes with the kubectl create deployment command. We need to provide the deployment name and app image location

```bash
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

To list your deployments use the kubectl get deployments command:
```bash
kubectl get deployments
```

We see that there is 1 deployment running a single instance of your app. The instance is running inside a container on your node.

### Capítulo 2 - Visualização (?)

Let's verify that the application we deployed in the previous scenario is running. We'll use the kubectl get command and look for existing Pods:

```bash
kubectl get pods
```

kubectl get - list resources

kubectl describe - show detailed information about a resource

kubectl logs - print the logs from a container in a pod

### Capítulo 3 - Expondo a aplicação

### Capítulo 4 - Scaling

### Capítulo 5 - Update

