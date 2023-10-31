import sys

user = sys.argv[1]

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