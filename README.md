# cwier-talos-sidero-metal-rpi-cm4
My Raspberry PI (CM4) development cluster (Talos Linux/Sidero Metal)

## Intro
```
This repo is just my things for building my Talos Linux / Sidero Metal setup on Raspberry PI CM4

## Hardware

[Hardware used in this project](hardware/HARDWARE.md)

## Hardware Details
```
┌──────────────────┬────────────────────────┬───────────────────┬──────────┬──────────────┬────────────────┬───────────────────┐
│ Hostname         │ Model                  │ MAC               │ Serial   │ Role         │  IP            │  OS               │
├──────────────────┼────────────────────────┼───────────────────┼──────────┼──────────────┼────────────────┼───────────────────┤
│ router-cwier     │ CM4 8Gb eMMC (32Gb)    │ e4:5f:01:d0:fe:04 │ 80e2c651 │ Router       │ 192.168.90.40  │ Raspbian Bookworm │
├──────────────────┼────────────────────────┼───────────────────┼──────────┼──────────────┼────────────────┼───────────────────┤
│ sidero-cwier     │ PI4 4Gb SDCARD (32Gb)  │ dc:a6:32:54:35:93 │ x        │ Sidero Metal │ 192.168.90.50  │ Talos Linux       │
├──────────────────┼────────────────────────┼───────────────────┼──────────┼──────────────┼────────────────┼───────────────────┤
│ node91           │ CM4 8Gb eMMC (32Gb)    │ d8:3a:dd:64:1c:c0 │ 0b655de6 │ Worker       │ 192.168.90.91  │ Talos Linux       │
│ node92           │ CM4 4Gb eMMC (32Gb)    │ d8:3a:dd:06:21:c6 │ 5a17f915 │ Controlplane │ 192.168.90.92  │ Talos Linux       │
│ node93           │ CM4 4Gb eMMC (32Gb)    │ d8:3a:dd:64:1b:84 │ 1974734d │ Controlplane │ 192.168.90.93  │ Talos Linux       │
│ node94           │ CM4 4Gb eMMC (32Gb)    │ d8:3a:dd:64:1d:0b │ 2c7d9a08 │ Controlplane │ 192.168.90.94  │ Talos Linux       │
│ node95           │ CM4 4Gb eMMC (32Gb)    │ d8:3a:dd:64:1c:c6 │ 7eb56880 │ Controlplane │ 192.168.90.95  │ Talos Linux       │
│ node96           │ CM4 4Gb eMMC (32Gb)    │ d8:3a:dd:64:1c:d8 │ 43f32a64 │ Controlplane │ 192.168.90.96  │ Talos Linux       │
└──────────────────┴────────────────────────┴───────────────────┴──────────┴──────────────┴────────────────┴───────────────────┘
```

## Router Setup Node
[Linux setup](router/ROUTER.md)

## Linux Application Containers (Docker) used for infrastructure and monitoring
[Docker containers](docker/DOCKER.md)
- coredns
- kea-dhcp4
- postgresql
- pgadmin
- node-exporter
- prometheus
- alertmanager
- grafana
- cadvisor
- loki
- promtail

## Sidero Metal Node
[Sidero Metal node setup](sidero/SIDERO.md)

## Talos Linux Cluster
[Talos Linux Cluster setup](talos/TALOS.md)

# Links

# [!IMPORTANT] Disclaimer 
This is my setup, running om my hardware.
You might find this usefull (you are welcome) or useless (i don't care).
The code may contain password, emails addresses, serials and is as such not secure!!! (use at your own risk)

Eric van Dijken <eric@cwier.nl>

