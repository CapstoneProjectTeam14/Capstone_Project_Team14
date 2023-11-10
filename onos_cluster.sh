# Download Atomix docker image:

docker pull atomix/atomix:3.1.5

# Run four instances of Atomix
docker run -t -d --name atomix-1 atomix/atomix:3.1.5
docker run -t -d --name atomix-2 atomix/atomix:3.1.5
docker run -t -d --name atomix-3 atomix/atomix:3.1.5
docker run -t -d --name atomix-4 atomix/atomix:3.1.5

# Check docker IP of Atomix instances:
docker inspect atomix-1 | grep -i ipaddress
docker inspect atomix-2 | grep -i ipaddress
docker inspect atomix-3 | grep -i ipaddress
docker inspect atomix-4 | grep -i ipaddress

# Check out ONOS source code:
git clone https://gerrit.onosproject.org/onos

# Set relevant environment variables to docker IP of Atomix instances obtained above
export OC1=172.17.0.2
export OC2=172.17.0.3
export OC3=172.17.0.4
export OC4=172.17.0.5


# Generate Atomix configuration files
cd /home/adarsh/onos

./tools/test/bin/atomix-gen-config 172.17.0.2 ~/atomix-1.conf 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/atomix-gen-config 172.17.0.3 ~/atomix-2.conf 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/atomix-gen-config 172.17.0.4 ~/atomix-3.conf 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/atomix-gen-config 172.17.0.5 ~/atomix-4.conf 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5

# Copy Atomix configuration to docker instances
docker cp ~/atomix-1.conf atomix-1:/opt/atomix/conf/atomix.conf
docker cp ~/atomix-2.conf atomix-2:/opt/atomix/conf/atomix.conf
docker cp ~/atomix-3.conf atomix-3:/opt/atomix/conf/atomix.conf
docker cp ~/atomix-4.conf atomix-4:/opt/atomix/conf/atomix.conf

# Restart Atomix docker instances for configuration to take effect
docker restart atomix-1
docker restart atomix-2
docker restart atomix-3
docker restart atomix-4

# Download ONOS docker image
docker pull onosproject/onos:2.2.2

# Run four ONOS docker instances
docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos1 onosproject/onos:2.2.2 
docker run -t -d --name onos2 onosproject/onos:2.2.2 
docker run -t -d --name onos3 onosproject/onos:2.2.2 
docker run -t -d --name onos4 onosproject/onos:2.2.2 

# Check docker IP of ONOS instances
docker inspect onos1 | grep -i ipaddress
docker inspect onos2 | grep -i ipaddress
docker inspect onos3 | grep -i ipaddress
docker inspect onos4 | grep -i ipaddress


# Generate ONOS cluster configuration files using docker IP obtained above
cd /home/adarsh/onos

./tools/test/bin/onos-gen-config 172.17.0.6 ~/cluster-1.json -n 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/onos-gen-config 172.17.0.7 ~/cluster-2.json -n 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/onos-gen-config 172.17.0.8 ~/cluster-3.json -n 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5
./tools/test/bin/onos-gen-config 172.17.0.9 ~/cluster-4.json -n 172.17.0.2 172.17.0.3 172.17.0.4 172.17.0.5

# Create config directory for ONOS docker instances
docker exec onos1 mkdir /root/onos/config
docker exec onos2 mkdir /root/onos/config
docker exec onos3 mkdir /root/onos/config
docker exec onos4 mkdir /root/onos/config

# Copy ONOS cluster configuration to docker instances
docker cp ~/cluster-1.json onos1:/root/onos/config/cluster.json
docker cp ~/cluster-2.json onos2:/root/onos/config/cluster.json
docker cp ~/cluster-3.json onos3:/root/onos/config/cluster.json
docker cp ~/cluster-4.json onos4:/root/onos/config/cluster.json

# Restart ONOS docker instances for configuration to take effect
docker restart onos1
docker restart onos2
docker restart onos3
docker restart onos4