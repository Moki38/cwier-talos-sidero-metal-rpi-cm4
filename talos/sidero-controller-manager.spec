# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "5"
  creationTimestamp: "2024-06-13T06:43:56Z"
  generation: 5
  labels:
    app: sidero
    cluster.x-k8s.io/provider: infrastructure-sidero
    cluster.x-k8s.io/v1alpha3: v1alpha3
    cluster.x-k8s.io/v1alpha4: v1alpha3
    cluster.x-k8s.io/v1beta1: v1alpha3
    clusterctl.cluster.x-k8s.io: ""
    control-plane: sidero-controller-manager
  name: sidero-controller-manager
  namespace: sidero-system
  resourceVersion: "41819"
  uid: b7672725-ae84-470e-832a-b2ebae9969f5
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: sidero
      cluster.x-k8s.io/provider: sidero
      cluster.x-k8s.io/v1alpha3: v1alpha3
      cluster.x-k8s.io/v1alpha4: v1alpha3
      cluster.x-k8s.io/v1beta1: v1alpha3
      control-plane: sidero-controller-manager
  strategy:
    type: Recreate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: sidero
        cluster.x-k8s.io/provider: sidero
        cluster.x-k8s.io/v1alpha3: v1alpha3
        cluster.x-k8s.io/v1alpha4: v1alpha3
        cluster.x-k8s.io/v1beta1: v1alpha3
        control-plane: sidero-controller-manager
    spec:
      containers:
      - args:
        - --enable-leader-election
        - --diagnostics-address=:8443
        - --insecure-diagnostics=false
        - --api-endpoint=192.168.90.50
        - --api-port=8081
        - --http-port=8081
        - --extra-agent-kernel-args=-
        - --boot-from-disk-method=ipxe-exit
        - --auto-accept-servers=false
        - --insecure-wipe=true
        - --auto-bmc-setup=true
        - --server-reboot-timeout=20m
        - --ipmi-pxe-method=uefi
        - --disable-dhcp-proxy=false
        - --test-power-simulated-explicit-failure-prob=0
        - --test-power-simulated-silent-failure-prob=0
        command:
        - /manager
        env:
        - name: API_ENDPOINT
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: status.hostIP
        image: ghcr.io/siderolabs/sidero-controller-manager:v0.6.5
        imagePullPolicy: Always
        livenessProbe:
          failureThreshold: 3
          httpGet:
            path: /healthz
            port: healthz
            scheme: HTTP
          periodSeconds: 10
          successThreshold: 1
          timeoutSeconds: 1
        name: manager
        ports:
        - containerPort: 9443
          name: webhook-server
          protocol: TCP
        - containerPort: 67
          name: dhcp
          protocol: UDP
        - containerPort: 69
          name: tftp
          protocol: UDP
        - containerPort: 8081
          name: http
          protocol: TCP
        - containerPort: 9440
          name: healthz
          protocol: TCP
        - containerPort: 8443
          name: metrics
          protocol: TCP
        readinessProbe:
          failureThreshold: 3
          httpGet:
            path: /readyz
            port: healthz
            scheme: HTTP
          periodSeconds: 10
          successThreshold: 1
          timeoutSeconds: 1
        resources:
          limits:
            cpu: "1"
            memory: 512Mi
          requests:
            cpu: 100m
            memory: 128Mi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /var/lib/sidero/tftp
          name: tftp-folder
        - mountPath: /tmp/k8s-webhook-server/serving-certs
          name: cert
          readOnly: true
      - args:
        - --wireguard-endpoint=-
        - --wireguard-port=51821
        command:
        - /siderolink-manager
        env:
        - name: API_ENDPOINT
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: status.hostIP
        image: ghcr.io/siderolabs/sidero-controller-manager:v0.6.5
        imagePullPolicy: Always
        name: siderolink
        ports:
        - containerPort: 51821
          name: siderolink
          protocol: UDP
        resources:
          limits:
            cpu: 500m
            memory: 512Mi
          requests:
            cpu: 50m
            memory: 128Mi
        securityContext:
          capabilities:
            add:
            - NET_ADMIN
          privileged: false
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /dev/net/tun
          name: dev-tun
      - command:
        - /log-receiver
        image: ghcr.io/siderolabs/sidero-controller-manager:v0.6.5
        imagePullPolicy: Always
        name: serverlogs
        resources:
          limits:
            cpu: 256m
            memory: 256Mi
          requests:
            cpu: 50m
            memory: 128Mi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      - command:
        - /events-manager
        - --negative-address-filter=-
        image: ghcr.io/siderolabs/sidero-controller-manager:v0.6.5
        imagePullPolicy: Always
        name: serverevents
        resources:
          limits:
            cpu: 256m
            memory: 256Mi
          requests:
            cpu: 50m
            memory: 128Mi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      hostNetwork: true
      initContainers:
      - args:
        - -r
        - /tftp
        - /var/lib/sidero/
        command:
        - cp
        image: docker.io/moki38/raspberrypi4-uefi:v1.8.0-alpha.0-27-ge5990e8
        imagePullPolicy: Always
        name: tftp-folder-setup
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /var/lib/sidero/tftp
          name: tftp-folder
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 10
      volumes:
      - emptyDir: {}
        name: tftp-folder
      - name: cert
        secret:
          defaultMode: 420
          secretName: sidero-webhook-service-cert
      - hostPath:
          path: /dev/net/tun
          type: CharDevice
        name: dev-tun
status:
  availableReplicas: 1
  conditions:
  - lastTransitionTime: "2024-06-13T09:36:39Z"
    lastUpdateTime: "2024-06-13T09:36:39Z"
    message: Deployment has minimum availability.
    reason: MinimumReplicasAvailable
    status: "True"
    type: Available
  - lastTransitionTime: "2024-06-13T06:43:56Z"
    lastUpdateTime: "2024-06-13T09:36:39Z"
    message: ReplicaSet "sidero-controller-manager-64974b559" has successfully progressed.
    reason: NewReplicaSetAvailable
    status: "True"
    type: Progressing
  observedGeneration: 5
  readyReplicas: 1
  replicas: 1
  updatedReplicas: 1
