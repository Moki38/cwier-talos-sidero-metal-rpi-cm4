# Sidero Metal on Raspberry PI4

## Create Talos node

```
export SIDERO_ENDPOINT=192.168.90.50
talosctl gen config --config-patch='[{"op": "add", "path": "/cluster/allowSchedulingOnControlPlanes", "value": true},{"op": "replace", "path": "/machine/install/disk", "value": "/dev/mmcblk0"}]' rpi4-sidero https://${SIDERO_ENDPOINT}:6443/

talosctl apply-config --insecure -n ${SIDERO_ENDPOINT} -f controlplane.yaml

talosctl config merge talosconfig
talosctl config endpoints ${SIDERO_ENDPOINT}
talosctl config nodes ${SIDERO_ENDPOINT}
talosctl bootstrap
talosctl kubeconfig
kubectl get nodes
talosctl -n 192.168.90.50 dmesg -f
```

## Setup Sidero Metal

```
export SIDERO_IP=192.168.90.50
SIDERO_CONTROLLER_MANAGER_HOST_NETWORK=true SIDERO_CONTROLLER_MANAGER_DEPLOYMENT_STRATEGY=Recreate SIDERO_CONTROLLER_MANAGER_API_ENDPOINT=${SIDERO_IP} clusterctl init -i sidero -b talos -c talos

kubectl get pods -A

curl -I http://${SIDERO_ENDPOINT}:8081/tftp/ipxe.efi
curl -I http://${SIDERO_ENDPOINT}:8081/tftp/ipxe-arm64.efi

wget http://${SIDERO_ENDPOINT}:8081/tftp/
```
## Create a backup
```
talosctl -n 192.168.90.50 etcd snapshot db.snapshot
talosctl -n 192.168.90.50 get mc v1alpha1 -o yaml | yq .spec - > talos_machineconfig_tftp.yaml
```

