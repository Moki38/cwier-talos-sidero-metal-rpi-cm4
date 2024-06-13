# Router node

## Install router node

This node will provide the network services for my Talos Linux development cluster.

Base OS: Raspbian Bookwork Lite (64Bit)

### Basic Setup

- Set root password
- apt upgrade, apt update
- apt install -y lvm2 git i2c-tools jq open-iscsi dnsutils nfs-common yq
- Setup ssh keys
- Update /etc/issue
- Update /etc/ssh/sshd_config
- Add "dtoverlay=dwc2,dr_mode=host" to /boot/firmware/config.txt
- Add "net.ifnames=0 disable.ipv6=1" to /boot/firmware/cmdline.txt
- Configure network interface eth0 (/etc/network/interfaces.d/eth0)
- Configure /etc/resolv.conf
- Disable BT/Wifi (dtoverlay=disable-wifi, dtoverlay=disable-bt) /boot/firmware/config.txt
- Enable RTC (dtparam=i2c_vc=on; dtoverlay=i2c-rtc,pcf85063a,i2c_csi_dsi) /boot/firmware/config.txt
- Enable I2C (raspi-config)
- Enable rsyslogd

### IPTables
```
apt -y install iptables-persistent
````
edit /etc/iptables/rules.v4

### Setup Docker
```
curl -fsSL https://get.docker.com -o get-docker.sh
echo " cgroup_memory=1 cgroup_enable=memory" >> /boot/firmware/config.txt
```
### Kubernetes / Talos tools
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
sudo curl -Lo /usr/local/bin/clusterctl   "https://github.com/kubernetes-sigs/cluster-api/releases/download/v1.7.2/clusterctl-$(uname -s | tr '[:upper:]' '[:lower:]')-arm64"
sudo curl -Lo /usr/local/bin/talosctl  "https://github.com/talos-systems/talos/releases/latest/download/talosctl-$(uname -s | tr '[:upper:]' '[:lower:]')-arm64"
```

