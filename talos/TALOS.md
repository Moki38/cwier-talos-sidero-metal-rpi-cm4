# Talos Linux workload-cluster (cwier-cluster)

## Configure BootFromDiskMethod
```
By default, Sidero will use iPXE’s exit command to attempt to force boot from disk. On Raspberry Pi, this will drop you into the bootloader interface, and you will need to connect a keyboard and manually select the disk to boot from.

The BootFromDiskMethod can be configured on individual Servers, on ServerClasses, or as a command-line argument to the Sidero metal controller itself (--boot-from-disk-method=<value>). In order to force the Pi to use the configured bootloader order, the BootFromDiskMethod needs to be set to ipxe-sanboot

```

## Installation Disk
```
/dev/mmcblk0

apiVersion: metal.sidero.dev/v1alpha2
kind: Server
...
spec:
  accepted: false
  configPatches:
    - op: replace
      path: /machine/install/disk
      value: /dev/mmcblk0
```

## Exclude sidero-system from PodSecurity
```
talosctl edit machineconfig -n 192.168.90.50
```

## Testing Configuration
```
curl http://192.168.90.50:8081/configdata?uuid=$SERVER_UUID
```

## Edit sidero-controller-manager
```
kubectl -n sidero-system edit deployments.apps sidero-controller-manager 
```

## kubectl get servers -o wide
```
NAME                                   HOSTNAME             BMC IP   ACCEPTED   CORDONED   ALLOCATED   CLEAN   POWER   AGE
00c03141-0000-0000-0000-d83add0621c6   node92.belni.local            false                                     on      9h
00d03141-0000-0000-0000-d83add641b84   node93.belni.local            false                                     on      9h
00d03141-0000-0000-0000-d83add641cc0   node91.belni.local            false                                     on      9h
00d03141-0000-0000-0000-d83add641cc6   node95.belni.local            false                                     on      9h
00d03141-0000-0000-0000-d83add641cd8   node96.belni.local            false                                     on      9h
00d03141-0000-0000-0000-d83add641d0b   node94.belni.local            false                                     on      9h
```

## Accept servers
```
kubectl patch server 00000000-0000-0000-0000-d05099d33360 --type='json' -p='[{"op": "replace", "path": "/spec/accepted", "value": true}]'
```
