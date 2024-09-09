# Upgrading a Kubernets Cluster from to 1.30.0-1.1

**1. update the repo URL version** 
```shell
  vim /etc/apt/sources.list.d/kubernetes.list
  deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /
```
**2. Drain the controlpane node**
```
  kubectl drain controlplane --ignore-daemonsets
```
**3. get the latest version**
```shell
  apt update
  apt-cache madison kubeadm
```
**4. Update the Kubeadm**
```shell
  apt-get install kubeadm=1.30.0-1.1
```
**5. Update the controlplane**
```shell
  kubeadm upgrade plan v1.30.0
  kubeadm upgrade apply v1.30.0
```
**6. Update the Kubelet**
```shell
  apt-get install kubelet=1.30.0-1.1
```
**7. Restart the daemons**
```shell
  systemctl daemon-reload
  systemctl restart kubelet
```
**8. reshecdule the controlplane node**
```shell
  kubectl uncordon controlplane
```
**9. Identify if there is any taint**
```shell
  kubectl describe node controlplane | grep -i taint
  kubectl taint node controlplane node-role.kubernetes.io/control-plane:NoSchedule-
```
**10. Drain the worker nodes**
```shell
  kubectl drain node01 --ignore-daemonsets
```
**11. SSH to the worker node and update the Kubernetes repo URL version**
```shell
  ssh node01
  vim /etc/apt/sources.list.d/kubernetes.list
  deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /
```
**12. Identify the latest versions for the nodes**
```shell
  apt update
  apt-cache madison kubeadm
```
**13. Update the worker node Kubeadm**
```shell
  apt-get install kubeadm=1.30.0-1.1
```
**14.Upgrade the node**
```shell
  kubeadm upgrade node
```
**15. Update the worker node kubelet**
```shell
  apt-get install kubelet=1.30.0-1.1
```
**16. Restart the daemons**
```shell
  systemctl daemon-reload
  systemctl restart kubelet
```
**17. Uncordon the worker node**
```shell
  kubectl uncordon node01
```

__Repeat the steps for all worker nodes__
