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

