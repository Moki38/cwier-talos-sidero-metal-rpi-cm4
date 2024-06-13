# Talos Linux

## Talos Linux Image
```
https://factory.talos.dev/image/86c5da69b80b298eab89fa6024337fa7ca7702584fd1344d167a08a0abbc6a2f/v1.7.4/metal-arm64.raw.xz

net.ifnames=0
configTxtAppend: 'dtoverlay=dwc2,dr_mode=host'


Your image schematic ID is: 86c5da69b80b298eab89fa6024337fa7ca7702584fd1344d167a08a0abbc6a2f

overlay:
    image: siderolabs/sbc-raspberrypi
    name: rpi_generic
    options:
        configTxtAppend: dtoverlay=dwc2,dr_mode=host
customization:
    extraKernelArgs:
        - net.ifnames=0
```
## Upgrade Image Link (if i ever need it)
```
factory.talos.dev/installer/86c5da69b80b298eab89fa6024337fa7ca7702584fd1344d167a08a0abbc6a2f:v1.7.4
```

# Sidero Metal
```
export SIDERO_IP=192.168.90.50

SIDERO_CONTROLLER_MANAGER_HOST_NETWORK=true SIDERO_CONTROLLER_MANAGER_DEPLOYMENT_STRATEGY=Recreate SIDERO_CONTROLLER_MANAGER_API_ENDPOINT=${SIDERO_IP} clusterctl init -i sidero -b talos -c talos

watch -n 2 kubectl get pods -A

Fetching providers
Installing cert-manager Version="v1.14.5"
Waiting for cert-manager to be available...
Installing Provider="cluster-api" Version="v1.7.3" TargetNamespace="capi-system"
Installing Provider="bootstrap-talos" Version="v0.6.5" TargetNamespace="cabpt-system"
[KubeAPIWarningLogger] would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "manager" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "manager" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "manager" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "manager" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
Installing Provider="control-plane-talos" Version="v0.5.6" TargetNamespace="cacppt-system"
[KubeAPIWarningLogger] would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "manager" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "manager" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "manager" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "manager" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
Installing Provider="infrastructure-sidero" Version="v0.6.5" TargetNamespace="sidero-system"
[KubeAPIWarningLogger] would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "manager" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "manager" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "manager" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "manager" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
[KubeAPIWarningLogger] would violate PodSecurity "restricted:latest": host namespaces (hostNetwork=true), allowPrivilegeEscalation != false (containers "manager", "siderolink", "serverlogs", "serverevents" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (containers "manager", "siderolink", "serverlogs", "serverevents" must set securityContext.capabilities.drop=["ALL"]; container "siderolink" must not include "NET_ADMIN" in securityContext.capabilities.add), restricted volume types (volume "dev-tun" uses restricted volume type "hostPath"), runAsNonRoot != true (pod or containers "manager", "siderolink", "serverlogs", "serverevents" must set securityContext.runAsNonRoot=true), seccompProfile (pod or containers "manager", "siderolink", "serverlogs", "serverevents" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")

Your management cluster has been initialized successfully!

You can now create your first workload cluster by running the following:

  clusterctl generate cluster [name] --kubernetes-version [version] | kubectl apply -f -

kubectl get pods -A

NAMESPACE       NAME                                         READY   STATUS    RESTARTS        AGE
cabpt-system    cabpt-controller-manager-5758996f4c-2vj65    1/1     Running   0               3m8s
cacppt-system   cacppt-controller-manager-6bb5849f57-vb566   1/1     Running   0               3m7s
capi-system     capi-controller-manager-7ff88d7c65-29mwn     1/1     Running   0               3m10s
cert-manager    cert-manager-5fcfc99f7-nx58n                 1/1     Running   0               3m35s
cert-manager    cert-manager-cainjector-75cfc9f6b7-wgv9x     1/1     Running   0               3m35s
cert-manager    cert-manager-webhook-74b65dbf6f-9mlsw        1/1     Running   0               3m34s
kube-system     coredns-64b67fc8fd-p5z25                     1/1     Running   0               7m18s
kube-system     coredns-64b67fc8fd-ttgt9                     1/1     Running   0               7m18s
kube-system     kube-apiserver-boot-cwier                    1/1     Running   0               6m48s
kube-system     kube-controller-manager-boot-cwier           1/1     Running   1 (7m46s ago)   6m18s
kube-system     kube-flannel-qn9s7                           1/1     Running   0               7m2s
kube-system     kube-proxy-l6cr8                             1/1     Running   0               7m2s
kube-system     kube-scheduler-boot-cwier                    1/1     Running   1 (7m39s ago)   6m3s
sidero-system   caps-controller-manager-c98458ccf-bvdxj      1/1     Running   0               2m56s
sidero-system   sidero-controller-manager-55548f8496-bmrb5   4/4     Running   0               2m56s
```
## Test TFTP
```
wget http://${SIDERO_ENDPOINT}:8081/tftp/

ipxe-arm64.efi
ipxe.efi
snp-arm64.efi
snp.efi
undionly.kpxe
undionly.kpxe.0
```
## Create Talos Cluster backup

### ETCD
```
talosctl -n 192.168.90.50 etcd snapshot db.snapshot
```
### Machine Config
```
talosctl -n 192.168.90.50 get mc v1alpha1 -o yaml | yq .spec - > talos_machineconfig_tftp.yaml
```

## Fix Raspberry PI CM4
Links:
https://www.sidero.dev/v0.6/guides/rpi4-as-servers/
https://github.com/raspberrypi/rpi-eeprom?tab=readme-ov-file

### Update BOOT EEPROM CM4
https://github.com/raspberrypi/usbboot
```
sudo apt install git libusb-1.0-0-dev pkg-config build-essential
git clone --recurse-submodules --shallow-submodules --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
git submodule update --init
```
### Boot.txt
```
BOOT_ORDER=0xf21
ENABLE_SELF_UPDATE=0
TFTP_PREFIX=2
```
### Config.txt
```
dtoverlay=dwc2,dr_mode=host
```

## Write EEPROM to CM4 
```
cd /root/cwier-talos-omni/rpi-uefi/usbboot
./rpiboot -d recovery
```
## Test EEPROM update
```
Bootloader: e608a69d    2024/04/15
```

## Update PKGS package
```
cd /root/cwier-talos-omni/talos
git clone http://github.com/talos-systems/pkgs
mkdir -p raspberrypi4-uefi/serials
cd raspberrypi4-uefi
cat > pkg.yaml << EOF
name: raspberrypi4-uefi
variant: alpine
install:
  - unzip
steps:
# {{ if eq .ARCH "aarch64" }} This in fact is YAML comment, but Go templating instruction is evaluated by bldr restricting build to arm64 only
  - sources:
      - url: https://github.com/pftf/RPi4/releases/download/v1.37/RPi4_UEFI_Firmware_v1.37.zip # <-- update version NR accordingly.
        destination: RPi4_UEFI_Firmware.zip
        sha256: 71a2343604a2f0f312ea9db215dcc71337fab2589809ca20a878b85ff35d154d
        sha512: 2e86a547d279f9e74b2e47572c3640826896e65e6647075409cf105322c55fa5beea17005300000bc2851c76cb5413b3901db14bb3590bb31a1cdfb7f448934e
    prepare:
      - |
        unzip RPi4_UEFI_Firmware.zip
        rm RPi4_UEFI_Firmware.zip
        mkdir /rpi4
        mv ./* /rpi4
    install:
      - |
        mkdir /tftp
        ls /pkg/serials | while read serial; do mkdir /tftp/\$serial && cp -r /rpi4/* /tftp/\$serial && cp -r /pkg/serials/\$serial/* /tftp/\$serial/; done
# {{ else }}
  - install:
      - |
                mkdir -p /tftp
# {{ end }}
finalize:
  - from: /
    to: /
EOF
```

## Build and Upload RPi4_UEFI_Firmware to REGISTRY
```
docker buildx create --name local --use

make PLATFORM=linux/arm64 USERNAME=moki38 REGISTRY=docker.io PUSH=true TARGETS=raspberrypi4-uefi TAG=latest
make[1]: Entering directory '/root/cwier-talos-omni/talos/pkgs/pkgs'
make[2]: Entering directory '/root/cwier-talos-omni/talos/pkgs/pkgs'
[+] Building 4.7s (23/23) FINISHED                                                                                                                  docker-container:local
 => [internal] load build definition from Pkgfile                                                                                                                     0.0s
 => => transferring dockerfile: 12.54kB                                                                                                                               0.0s
 => resolve image config for docker-image://ghcr.io/siderolabs/bldr:v0.3.1                                                                                            0.8s
 => CACHED docker-image://ghcr.io/siderolabs/bldr:v0.3.1@sha256:c6b05876880533c188f5b273a857fc4d1915389e65e1f6dc2ebcd48930f13863                                      0.0s
 => => resolve ghcr.io/siderolabs/bldr:v0.3.1@sha256:c6b05876880533c188f5b273a857fc4d1915389e65e1f6dc2ebcd48930f13863                                                 0.0s
 => load Pkgfile, pkg.yamls and vars.yamls                                                                                                                            0.1s
 => => transferring dockerfile: 8.55kB                                                                                                                                0.1s
 => cksum                                                                                                                                                             0.7s
 => => resolve docker.io/library/alpine:3.20                                                                                                                          0.7s
 => raspberrypi4-uefi:download https://github.com/pftf/RPi4/releases/download/v1.37/RPi4_UEFI_Firmware_v1.37.zip -> RPi4_UEFI_Firmware.zip                            0.0s
 => context                                                                                                                                                           0.1s
 => => transferring context: 4.70kB                                                                                                                                   0.1s
 => CACHED base-apkinstall                                                                                                                                            0.0s
 => CACHED base-symlink                                                                                                                                               0.0s
 => CACHED mkdir /pkg                                                                                                                                                 0.0s
 => CACHED raspberrypi4-uefi:apk-install                                                                                                                              0.0s
 => CACHED raspberrypi4-uefi:context /raspberrypi4-uefi -> /pkg                                                                                                       0.0s
 => CACHED raspberrypi4-uefi:mkdir /tmp/build/0                                                                                                                       0.0s
 => CACHED cksum-apkinstall                                                                                                                                           0.0s
 => CACHED raspberrypi4-uefi:cksum-prepare                                                                                                                            0.0s
 => CACHED raspberrypi4-uefi:cksum-verify                                                                                                                             0.0s
 => CACHED raspberrypi4-uefi:download finalize                                                                                                                        0.0s
 => CACHED raspberrypi4-uefi:download                                                                                                                                 0.0s
 => CACHED raspberrypi4-uefi:prepare-0                                                                                                                                0.0s
 => CACHED raspberrypi4-uefi:install-0                                                                                                                                0.0s
 => CACHED raspberrypi4-uefi:finalize / -> /                                                                                                                          0.0s
 => exporting to image                                                                                                                                                2.4s
 => => exporting layers                                                                                                                                               0.0s
 => => exporting manifest sha256:45e302e57ddd75a59340c44c9d7b4c934b422a6fda511c284eb9260ddb5cef0b                                                                     0.0s
 => => exporting config sha256:1ffaea299a40072c8ffb404e5590c81ec048a47a1e693fd350772090df6d3475                                                                       0.0s
 => => pushing layers                                                                                                                                                 1.9s
 => => pushing manifest for docker.io/moki38/raspberrypi4-uefi:latest@sha256:45e302e57ddd75a59340c44c9d7b4c934b422a6fda511c284eb9260ddb5cef0b                         0.5s
 => [auth] moki38/raspberrypi4-uefi:pull,push token for registry-1.docker.io                                                                                          0.0s
```

## Patch Metal Controller
```
cat > patch-metal.yaml << EOF
spec:
  template:
    spec:
      volumes:
        - name: tftp-folder
          emptyDir: {}
      initContainers:
      - image: docker.io/moki38/raspberrypi4-uefi:latest
        imagePullPolicy: Always
        name: tftp-folder-setup
        command:
          - cp
        args:
          - -r
          - /tftp
          - /var/lib/sidero/
        volumeMounts:
          - mountPath: /var/lib/sidero/tftp
            name: tftp-folder
      containers:
      - name: manager
        volumeMounts:
          - mountPath: /var/lib/sidero/tftp
            name: tftp-folder
EOF
```

## Apllay the patch-metal
```
kubectl -n sidero-system patch deployments.apps sidero-controller-manager --patch "$(cat patch-metal.yaml)"

# kubectl get servers -o wide
NAME                                   HOSTNAME             BMC IP   ACCEPTED   CORDONED   ALLOCATED   CLEAN   POWER   AGE
00c03141-0000-0000-0000-d83add0621c6   node92.belni.local            false                                     on      27m
```
# Next CM4
```
cd /root/cwier-talos-omni/rpi-uefi/usbboot
./rpiboot -d recovery
```
## All server done
```
kubectl get servers -o wide

NAME                                   HOSTNAME             BMC IP   ACCEPTED   CORDONED   ALLOCATED   CLEAN   POWER   AGE
00c03141-0000-0000-0000-d83add0621c6   node92.belni.local            false                                     on      27m
00d03141-0000-0000-0000-d83add641b84   node93.belni.local            false                                     on      73s
00d03141-0000-0000-0000-d83add641cc0   node91.belni.local            false                                     on      10m
00d03141-0000-0000-0000-d83add641cc6   node95.belni.local            false                                     on      72s
00d03141-0000-0000-0000-d83add641cd8   node96.belni.local            false                                     on      63s
00d03141-0000-0000-0000-d83add641d0b   node94.belni.local            false                                     on      72s
```

## Configure BootFromDiskMethod
```
#
By default, Sidero will use iPXE’s exit command to attempt to force boot from disk. On Raspberry Pi, this will drop you into the bootloader interface, and you will need to connect a keyboard and manually select the disk to boot from.

The BootFromDiskMethod can be configured on individual Servers, on ServerClasses, or as a command-line argument to the Sidero metal controller itself (--boot-from-disk-method=<value>). In order to force the Pi to use the configured bootloader order, the BootFromDiskMethod needs to be set to ipxe-sanboot

```

