import sys

user = sys.argv[1]

kube_role = """kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
    name: {}-role
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
""".format(user, user)

with open(f"roles/{user}-role.yaml", 'w') as role_file:
    role_file.write(kube_role)