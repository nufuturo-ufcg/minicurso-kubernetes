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

## Conectando-se ao cluster

1. Siga esse [tutorial](https://github.com/nufuturo-ufcg/stress-testing-automation/blob/main/doc/aws-credentials.md) para atualizar suas credenciais da AWS;

2. Execute o comando abaixo para configurar o kubectl:

```bash
aws eks update-kubeconfig --name minicurso-kubernetes --region sa-east-1 --profile nufuturo
```

3. Agora vamos alterar o namespace default para o que você irá utilizar. Execute o comando abaixo alterando `<meu-namespace>` pelo prefixo do seu email ccc, com hífen no lugar do ponto. Ex: carlos-ribeiro.:

```bash
kubectl config set-context --current --namespace=<meu_namespace>
```

4. Verifique que você está conectado ao cluster:
```bash 
kubectl get pods
```

## Mãos a obra

### Capítulo 1 - Deployment

Depois de obter acesso a um cluster Kubernetes em funcionamento, você pode implantar suas aplicações nele. Para fazer isso, você cria um **Deployment** no Kubernetes. O **Deployment** instrui o Kubernetes sobre como criar e atualizar instâncias da sua aplicação. Uma vez que você tenha criado um **Deployment**, o _control plane_ do Kubernetes escalona as instâncias da aplicação incluídas nesse **Deployment** para serem executadas em _nodes_ individuais no cluster.

Você pode criar e gerenciar um **Deployment** usando a interface de linha de comando do Kubernetes, o **kubectl**.

> 💡 Dica
> 
> O formato comum de um comando do kubectl é: `kubectl action resource`

Quando você cria uma **Deployment**, precisará especificar a imagem do contêiner para a sua aplicação e o número de réplicas que deseja executar.

Vamos implantar nossa primeira aplicação no Kubernetes com o comando `kubectl create deployment`. Precisamos fornecer o nome do **Deployment** e a localização da imagem da aplicação:
```bash
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

Para listar seus deployments utilize o comando a seguir:
```bash
kubectl get deployments
```

Podemos ver que há 1 deployment executando uma única instância da sua aplicação. A aplicação está executando dentro de um contâiner no seu _Node_.

### Capítulo 2 - Visualização (?)

Após realizar o deploy da nossa aplicação, podemos utilizar uma série de comandos voltados para a visualização dos elementos de nosso cluster. Para verificar o que foi criado para a nossa aplicação, vamos utilizar o seguinte comando para ver os _Pods_ existentes:

```bash
kubectl get pods
```

É possível ver que containers estão dentro de cada _Pod_ e que imagens foram usadas para em sua build utilizando o seguinte comando:

```bash
kubectl describe pods
```

Com a saída desse comando, vemos detalhes sobre o container do _Pod_, como o endereço de IP, as portas utilizadas e uma lista de eventos relacionados ao ciclo de vida do _Pod_. 

Também é possível recuperar os logs dos containers do _Pod_, a partir do comando abaixo:

```bash
kubectl logs <pod-name>
```

Nesse caso não foi necessário especificar o nome do container que queremos ver os logs, já que há apenas um container em seu interior, no entanto, em um cenário em que mais de um container é executado em cada _Pod_, é preciso especificar de qual container serão lidos os logs registrados.

Outra coisa que é possível fazer é executar comandos dentro do container enquanto o _Pod_ estiver em funcionamento, de forma semelhante ao Docker, para isso, usamos o comando exec, passando o nome do _Pod_ de parâmetro e o que queremos executar, como no exemplo abaixo:

```bash
kubectl exec -ti <pod-name> -- bash
```

Agora estamos dentro do container que está rodando a nossa aplicação, para verificar, é possível fazer um curl no localhost na porta 8080, que está rodando a aplicação:

```bash
curl http://localhost:8080
```

### Capítulo 3 - Expondo a aplicação

Nós já temos o nosso serviço rodando em nosso cluster kubernetes, no entanto, ainda não é possível acessá-lo de fora do cluster, pois apesar de nossos _Pods_ possuírem um endereço de IP próprio, eles não são expostos para a internet, ou seja, nossa aplicação não está exposta. Para resolver isso, precisamos criar um **Service**, um componente do kubernetes que permite que os seus aplicativos recebam tráfego, atuando como um load balancer, recebendo o tráfego e passando para algum _Pod_ que esteja rodando a nossa aplicação. Vamos listas os **Services** atuais de nosso cluster:

```bash
kubectl get services
```

Existe apenas um **Service** chamado kubernetes, que é criado por padrão quando o cluster é iniciado. Para criar um novo **Service* e expor nossa aplicação ao tráfego externo, vamos utilizar o comando expose com o parâmetro "NodePort":

``` bash
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080 
```

Agora vamos rodar de novo o get services:

```bash
kubectl get services
```

Nesse momento, nós temos um novo **Service** chamado kubernetes-bootcamp, e podemos ver que ele recebeu um cluster-IP único, uma porta interna, e um IP externo. Agora, podemos utilizar o IP externo do **Service** para acessar o nosso serviço de fora do cluster, para testar isso, basta realizar um curl de fora do :

```bash
curl http://<node-ip>:<service-port>
```

### Capítulo 4 - Scaling

Agora que já temos um serviço rodando e acessível através da internet, entraremos em um assunto que é uma das principais características do kubernetes: o scaling. Nós podemos escalar a nossa aplicação manualmente pelo **Deployment**, garantindo que novos _Pods_ sejam criados com os recursos disponíveis. Dessa forma, o kubernetes vai garantir que existam sempre a quantidade de réplicas definidas pelo usuário no arquivo de **Deployment**. Inicialmente, vamos ver a quantidade de pods rodando a nossa aplicação, novamente com o comando get pods, mas com uma flag a mais, que nos trás mais informações acerca de nossos pods:

```bash
kubectl get pods -o wide
```

É possível ver que existe apenas 1 réplica de nossa aplicação rodando, então agora vamos mudar o número de replicas para 3, utilizando o comando kubectl scale. O número de réplicas também pode ser definido no *.yaml* de nosso **Deployment**.

```bash
kubectl scale deployments/kubernetes-bootcamp --replicas=3

```

Nesse momento, a mudança é aplicada, e agora nós possuímos 3 instâncias de nossa aplicação disponíveis, como podemos checar novamente:

```bash
kubectl get pods -o wide
```

### Capítulo 5 - Update

Um requisito não-funcional que quem utiliza o kubernetes busca cumprir é o de disponibilidade, já que os usuários esperam ter os seus aplicativos disponíveis o tempo todo e que os desenvolvedores implantar novas versões com frequência. Para permitir que novas versões sejam disponibilizadas sem a necessidade de haver tempos de inatividade, em que o serviço não está disponível, o kubernetes realiza atualizações contínuas, atualizando as instâncias dos _Pods_ aos poucos com novas instâncias possuindo uma nova versão da aplicação.

Vamos atualizar a imagem da nossa aplicação para uma segunda versão, utilizando o comando set image:

```bash
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
```

Ao executar o comando, o **Deployment** foi notificado para utilizar uma imagem diferente da sua aplicação e iniciou uma atualização contínua. O status tanto dos novos _Pods_ quanto dos antigos pode ser visto realizando um get pods:

```bash
kubectl get pods
```

E, para ter certeza que a versão da imagem foi atualizada, podemos utilizar um comando que já aprendemos:

```bash
kubectl describe pods
```

Podemos ver que a imagem foi atualizada, e os próximos _Pods_ criados a partir desse **Deployment** terão todos essa nova imagem.