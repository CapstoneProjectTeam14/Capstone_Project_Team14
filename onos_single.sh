sudo docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos onosproject/onos -e ONOS_APPS="drivers,openflow-base,netcfghostprovider,lldpprovider,gui2,fwd,openflow"


