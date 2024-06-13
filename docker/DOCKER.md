# Docker

The story as goes: Practice what your preach.
So, everything should run in a container.... unless

(Don't forget to copy and edit the config files.)
## Docker
```
cp daemon.json /etc/docker

systemctl restart docker
```

## CoreDNS
```
mkdir -p /data/coredns/data

docker run --restart always -d -v /data/coredns/data:/root -p 53:53/udp -p 9253:9253 --name coredns docker.io/coredns/coredns -conf /root/Corefile
```

## Postgresql / PGadmin
```
mkdir -p /data/postgres/data

docker run --name postgresql -d -p 5432:5432 -v /data/postgresql/data:/var/lib/postgresql/data -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=d29f90eb10309b8577e4 docker.io/postgres:latest

docker run --name pgadmin -p 5050:80 -e 'PGADMIN_DEFAULT_EMAIL=pgadmin@cwier.nl' -e 'PGADMIN_DEFAULT_PASSWORD=d29f90eb10309b8577e4' -d docker.io/dpage/pgadmin4
```

## ISC KEA DHCPv4 server
Create the Postgresql KEA database
```
TODO:
psql -d kea_dhcp -f data/dhcpdb_create.pgsql

No ARM64 version, we have build our own ARM64 version.
```
mkdir -p /data/kea/config
mkdir -p /data/kea/data

docker run --restart always --name kea-dhcp4 -d ---network host -p 67:67/udp -p 8000:8000 -p 8001:8001 -v /data/kea/data:/var/lib/kea -v /data/kea/config:/etc/kea moki38/kea-dhcp4
```

## Node-exporter
```
docker run -d --restart always -p 9100:9100 --name node-exporter --net="host" --pid="host" -v "/:/host:ro,rslave" quay.io/prometheus/node-exporter:latest --path.rootfs=/host
```

## Prometheus
```
mkdir -p /data/prometheus/config
mkdir -p /data/prometheus/data
mkdir -p /data/alertmanager/config

docker run --restart always -d -p 9090:9090 --name prometheus -v /data/prometheus/config:/etc/prometheus -v /data/prometheus/data:/prometheus -v /data/alertmanager/config:/etc/alertmanager docker.io/prom/prometheus
```

## Alertmanager
```
mkdir -p /data/alertmanager/data

docker run --restart always -d -p 9093:9093 --name alertmanager -v /data/alertmanager/config:/etc/alertmanager -v /data/alertmanager/data:/alertmanager docker.io/prom/alertmanager
```

## Grafana
```
mkdir -p /data/grafana/config
mkdir -p /data/grafana/data

docker run -d -p 3000:3000 --restart always --name grafana -v /data/grafana/config:/etc/grafana -v /data/grafana/data:/var/lib/grafana docker.io/grafana/grafana-oss
```

## Cadvisor
```
docker run --restart always --volume=/:/rootfs:ro --volume=/var/run:/var/run:ro --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/dev/disk/:/dev/disk:ro --volume=/etc/machine-id:/etc/machine-id:ro --publish=8080:8080 --detach=true --name=cadvisor --privileged --device=/dev/kmsg gcr.io/cadvisor/cadvisor -docker_only=true
```
## Haproxy
```
mkdir -p /data/haproxy/config
mkdir -p /data/haproxy/errors
mkdir -p /data/haproxy/www

docker run --restart always -d --name haproxy -p80:80 -p443:443 -p8404:8404 -v "/data/letsencrypt/config:/etc/letsencrypt/config" -v /data/haproxy/www:/var/www -v /data/haproxy/errors:/etc/haproxy/errors -v /data/haproxy/config:/usr/local/etc/haproxy:ro --sysctl net.ipv4.ip_unprivileged_port_start=0 docker.io/haproxy
```
mkdir -p /data/letsencrypt/config
mkdir -p /data/letsencrypt/data

## Letsencrypt
```
podman run -it --rm --name certbot -v "/data/letsencrypt/config:/etc/letsencrypt" -v "/data/letsencrypt/data:/var/lib/letsencrypt" docker.io/certbot/certbot certonly --manual --preferred-challenges dns
```

## Promtail
```
docker run --name promtail -d -v /data/loki/config:/mnt/config -v /var/log:/var/log --link loki grafana/promtail:3.0.0 -config.file=/mnt/config/promtail-config.yaml
```

## Loki
```
docker run --name loki -d -v /data/loki/config:/mnt/config -p 3100:3100 grafana/loki:3.0.0 -config.file=/mnt/config/loki-config.yaml
```

