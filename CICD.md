# K8S Argo instructions

## CD

Based on:
- https://argoproj.github.io/argo-cd/getting_started/
- https://youtu.be/2WSJF7d8dUg (That DevOps Guy)

Install Argo:

```
alias k=kubectl
k create namespace argocd
wget https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
mv install.yaml argo/argocd
k apply -n argocd -f argo/argocd/install.yaml
```

Start port forwarding (most secure) in separate terminal. This allows you to open
Argo GUI via http://localhost:8080:

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Finally, deploy app:

```
k apply -n argocd -f argo/argocd/app.yaml
```

## CI

Based on:
- https://docs.docker.com/docker-hub/builds/
