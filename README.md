# minicurso-kubernetes

## Tutorial

### Pré-requisitos

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
3. Execute o comando abaixo para alterar o namespace default:
```bash
kubectl config set-context --current --namespace=<meu_namespace>
```
Altere `<meu-namespace>` pelo prefixo do seu email ccc, com hífen no lugar do ponto. Ex: carlos-ribeiro.