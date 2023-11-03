# Minicurso Kubernetes

## Pré-requisitos

1. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Verifique a instalação:
```bash
aws --version
```

2. [Python3](https://www.python.org/downloads/)

Verifique a instalação:
```bash
python3 --version
pip3 --version
```

3. gimme-aws-creds

Instalando como módulo python:
```bash
pip3 install --upgrade gimme-aws-creds
```
Verifique a instalação:
```bash
gimme-aws-creds --version
```

4. [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

Verifique a instalação:
```bash
kubectl version
```

## Conectando-se ao cluster (Maria Luísa)

1. Faça ssh para o control plane do cluster:

```bash
ssh ubuntu@54.207.145.223
```

2. Verifique que você está conectada ao cluster:

```bash 
kubectl get pods
```

## Conectando-se ao cluster (Resto)

1. Siga esse [tutorial](https://github.com/nufuturo-ufcg/stress-testing-automation/blob/main/doc/aws-credentials.md) para atualizar suas credenciais da AWS;

2. Execute o comando abaixo para configurar o kubectl:

```bash
aws eks update-kubeconfig --name minicurso-kubernetes --region sa-east-1 --profile nufuturo
```

3. Agora vamos alterar o namespace default para o que você irá utilizar. Execute o comando abaixo alterando `<meu-namespace>` pelo prefixo do seu email ccc, com hífen no lugar do ponto. Ex: carlos-ribeiro.:

```bash
kubectl config set-context --current --namespace=<meu_namespace>
```

4. Verifique que você está conectado(a) ao cluster:
```bash 
kubectl get pods
```

## Mãos a obra

### Capítulo 1 - Deployment

Depois de obter acesso a um cluster Kubernetes em funcionamento, você pode implantar suas aplicações nele. Para fazer isso, você irá criar um **Deployment** no Kubernetes. O **Deployment** instrui o Kubernetes sobre como criar e atualizar instâncias da sua aplicação. Uma vez que você tenha criado um **Deployment**, o _control plane_ do Kubernetes escalona as instâncias da aplicação incluídas nesse **Deployment** para serem executadas em _nodes_ individuais no cluster.

Você pode criar e gerenciar um **Deployment** usando a interface de linha de comando do Kubernetes, o **kubectl**.

> 💡 Dica
> 
> O formato comum de um comando do kubectl é: `kubectl action resource`

Quando você cria uma **Deployment**, precisará especificar a imagem contâinerizada da sua aplicação e o número de réplicas que deseja executar.

Vamos implantar nossa primeira aplicação no Kubernetes com o comando `kubectl create deployment`. Precisamos fornecer o nome do **Deployment** e a localização da imagem da aplicação:
```bash
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

Para listar seus deployments utilize o comando a seguir:
```bash
kubectl get deployments
```

Podemos ver que há 1 deployment executando uma única instância da sua aplicação. A aplicação está executando dentro de um contâiner no seu _Node_.

#### Exercícios

No exemplo acima, criamos um **Deployment** a partir da imagem `gcr.io/google-samples/kubernetes-bootcamp:v1`. Experimente criar outros deployments utilizando outras imagens e variando o número de réplicas.

> 💡 Dica
> 
> Você pode obter ajuda utilizando o comando `kubectl create deployment --help`

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

