# Workload cluster
## These are our servers
```
kubectl get servers -o wide

NAME                                   HOSTNAME             BMC IP   ACCEPTED   CORDONED   ALLOCATED   CLEAN   POWER   AGE
00c03141-0000-0000-0000-d83add0621c6   node92.belni.local            true                              true    on      28h
00d03141-0000-0000-0000-d83add641b84   node93.belni.local            false                                     on      28h
00d03141-0000-0000-0000-d83add641cc0   node91.belni.local            false                                     on      28h
00d03141-0000-0000-0000-d83add641cc6   node95.belni.local            false                                     on      28h
00d03141-0000-0000-0000-d83add641cd8   node96.belni.local            false                                     on      28h
00d03141-0000-0000-0000-d83add641d0b   node94.belni.local            false                                     on      28h
```

## Generate config
```
export CONTROL_PLANE_SERVERCLASS=any
export WORKER_SERVERCLASS=any
export TALOS_VERSION=v1.7.4
export KUBERNETES_VERSION=v1.30.1
export CONTROL_PLANE_PORT=6443
export CONTROL_PLANE_ENDPOINT=192.168.90.92

clusterctl generate cluster workload-cluster -i sidero > workload-cluster.yaml
```

## Create the cluster
```
kubectl apply -f workload-cluster.yaml
```


# DEBUG (This can't be good)
```
2024/06/14 14:32:08 Using "agent-arm64" environment for "00d03141-0000-0000-0000-d83add641cc0"

2024/06/14 14:30:28 open /var/lib/sidero/tftp/0b655de6/overlays/dwc2.dtbo: no such file or directory
2024/06/14 14:30:28 open /var/lib/sidero/tftp/0b655de6/cmdline.txt: no such file or directory
2024/06/14 14:33:17 open /var/lib/sidero/tftp/0b655de6/pieeprom.upd: no such file or directory
2024/06/14 14:33:17 open /var/lib/sidero/tftp/0b655de6/recover4.elf: no such file or directory
2024/06/14 14:33:17 open /var/lib/sidero/tftp/0b655de6/recovery.elf: no such file or directory
2024/06/14 14:33:30 open /var/lib/sidero/tftp/0b655de6/overlays/overlay_map.dtb: no such file or directory
2024/06/14 14:33:29 open /var/lib/sidero/tftp/0b655de6/bootcfg.txt: no such file or directory
2024/06/14 14:33:30 open /var/lib/sidero/tftp/0b655de6/recovery8.img: no such file or directory
2024/06/14 14:33:30 open /var/lib/sidero/tftp/0b655de6/kernel8.img: no such file or directory
2024/06/14 14:33:29 open /var/lib/sidero/tftp/0b655de6/dt-blob.bin: no such file or directory
2024/06/14 14:33:29 open /var/lib/sidero/tftp/0b655de6/recovery.elf: no such file or directory
```

