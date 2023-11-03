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

## Mãos à obra!

### Capítulo 1 - Deployment

Depois de obter acesso a um cluster Kubernetes em funcionamento, você pode implantar suas aplicações nele. Para fazer isso, você irá criar um **Deployment** no Kubernetes. O **Deployment** instrui o Kubernetes sobre como criar e atualizar instâncias da sua aplicação. Uma vez que você tenha criado um **Deployment**, o _control plane_ do Kubernetes escalona as instâncias da aplicação incluídas nesse **Deployment** para serem executadas em _nodes_ individuais no cluster.

Você pode criar e gerenciar um **Deployment** usando a interface de linha de comando do Kubernetes, o **kubectl**.

> 💡 Dica!
> 
> O formato comum de um comando do kubectl é: `kubectl action resource`

Quando você cria um **Deployment**, precisa especificar a imagem contâinerizada da sua aplicação.

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

> 💡 Dica!
> 
> Você pode obter ajuda utilizando o comando `kubectl create deployment --help`

### Capítulo 2 - Explorando o cluster

#### Pods

Quando você criou um **Deployment** no Capítulo 1, o Kubernetes criou um **Pod** para hospedar a instância da sua aplicação. Um **Pod** é uma abstração do Kubernetes que representa um grupo de um ou mais contêineres de aplicação e alguns recursos compartilhados para esses contêineres. Esses recursos incluem:

- Armazenamento compartilhado, como Volumes
- Rede, como um endereço IP exclusivo no cluster
- Informações sobre como executar cada contêiner, como a versão da imagem do contêiner ou portas específicas a serem usadas

Um **Pod** modela um "host lógico" específico da aplicação e pode conter diferentes contêineres de aplicação que estão relativamente acoplados. Por exemplo, um Pod pode incluir tanto o contêiner com a sua aplicação Node.js quanto um contêiner diferente que fornece os dados a serem publicados pelo servidor web Node.js. Os contêineres em um Pod compartilham um endereço IP e espaço de porta, estão sempre localizados e programados juntos e são executados em um contexto compartilhado no mesmo **Node**.

#### Nodes

No Kubernetes, os **Nodes** são os trabalhadores do cluster e desempenham um papel crucial na execução de suas aplicações. Pense neles como as máquinas físicas ou virtuais que compõem o seu cluster Kubernetes.

> ⚠️ Atenção!
>
> Para visualizar os **Nodes** você precisaria de permissão para realizar operações _cluster-scoped_, no entanto, nesse minicurso, você está limitado(a) a fazer operações _namespace-scoped_ para que os objetos que você está criando não se misturem com os dos colegas.

Abaixo podemos ver como se parece a saída para o comando `kubectl get nodes`.
```
ubuntu@ip-172-31-6-4:~$ kubectl get nodes
NAME              STATUS   ROLES           AGE   VERSION
ip-172-31-6-197   Ready    <none>          8d    v1.28.2
ip-172-31-6-4     Ready    control-plane   8d    v1.28.2
ip-172-31-9-99    Ready    <none>          8d    v1.28.2
```

#### Troubleshooting com kubectl

In Chapter 1, you used the kubectl command-line interface. You'll continue to use it in Chapter 2 to get information about deployed applications and their environments. The most common operations can be done with the following kubectl subcommands:

- `kubectl get` - list resources
- `kubectl describe` - show detailed information about a resource
- `kubectl logs` - print the logs from a container in a pod
- `kubectl exec` - execute a command on a container in a pod

You can use these commands to see when applications were deployed, what their current statuses are, where they are running and what their configurations are.

Now that we know more about our cluster components and the command line, let's explore our application.

A node is a worker machine in Kubernetes and may be a VM or physical machine, depending on the cluster. Multiple Pods can run on one Node.

##### Check application configuration

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
If no pods are running, please wait a couple of seconds and list the Pods again. You can continue once you see one Pod running.

Next, to view what containers are inside that Pod and what images are used to build those containers we run the kubectl describe pods command:

```bash
kubectl describe pods
```

We see here details about the Pod’s container: IP address, the ports used and a list of events related to the lifecycle of the Pod.

The output of the describe subcommand is extensive and covers some concepts that we didn’t explain yet, but don’t worry, they will become familiar by the end of this bootcamp.

Note: the describe subcommand can be used to get detailed information about most of the Kubernetes primitives, including Nodes, Pods, and Deployments. The describe output is designed to be human readable, not to be scripted against.

##### View the container logs

Anything that the application would normally send to standard output becomes logs for the container within the Pod. We can retrieve these logs using the kubectl logs command:

```bash
kubectl logs "$POD_NAME"
```

Note: We don't need to specify the container name, because we only have one container inside the pod.
Executing command on the container

We can execute commands directly on the container once the Pod is up and running. For this, we use the exec subcommand and use the name of the Pod as a parameter. Let’s list the environment variables:

```bash
kubectl exec "$POD_NAME" -- env
```

Again, it's worth mentioning that the name of the container itself can be omitted since we only have a single container in the Pod.

Next let’s start a bash session in the Pod’s container:

```bash
kubectl exec -ti $POD_NAME -- bash
```

We have now an open console on the container where we run our NodeJS application. The source code of the app is in the server.js file:

```bash
cat server.js
```

You can check that the application is up by running a curl command:

```bash
curl http://localhost:8080
```

Note: here we used localhost because we executed the command inside the NodeJS Pod. If you cannot connect to localhost:8080, check to make sure you have run the kubectl exec command and are launching the command from within the Pod

To close your container connection, type exit.

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
