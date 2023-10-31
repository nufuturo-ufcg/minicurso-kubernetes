users = [
    "abraao-araujo",
    "andrielly-lucena",
    "bianca-pacheco",
    "carlos-ribeiro",
    "carmelita-medeiros",
    "cilas-marques",
    "dalton-guerrero",
    "fabio-morais",
    "guilherme-peixoto",
    "ingrid-castro",
    "joao-arthur",
    "joao-lucena",
    "joao-santos",
    "jonatas-lima",
    "julia-menezes",
    "marcelo-fechine",
    "mariane-zeitouni",
    "mayara-pinheiro",
    "narallynne-araujo",
    "nicolas-leite",
    "rodrigo-cavalcanti",
    "sheila-paiva",
    "thiago-silva",
    "victor-andrade",   
]

for user in users:
    kube_role = """kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: {}
namespace: {}
rules:
- apiGroups:
    - ""
    - "apps"
    - "batch"
    - "extensions"
    resources:
    - "configmaps"
    - "cronjobs"
    - "deployments"
    - "events"
    - "ingresses"
    - "jobs"
    - "pods"
    - "pods/attach"
    - "pods/exec"
    - "pods/log"
    - "pods/portforward"
    - "secrets"
    - "services"
    verbs:
    - "create"
    - "delete"
    - "describe"
    - "get"
    - "list"
    - "patch"
    - "update"
    """.format(f"{user}-role", user)

    with open(f"roles/{user}-role.yaml", 'w') as role_file:
        role_file.write(kube_role)