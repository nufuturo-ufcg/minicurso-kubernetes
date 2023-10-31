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
    kube_rolebinding = """kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {}-rolebinding
  namespace: {}
subjects:
- kind: User
  name: {}-user
roleRef:
  kind: Role
  name: {}-role
  apiGroup: rbac.authorization.k8s.io
""".format(user, user, user, user)

    with open(f"rolebindings/{user}-rolebinding.yaml", 'w') as rolebinding_file:
        rolebinding_file.write(kube_rolebinding)