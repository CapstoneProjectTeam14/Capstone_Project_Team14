      
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import socket
setLogLevel('info')



net=Containernet()
info('*** Adding controller\n')
c0 = RemoteController( 'c0' , ip=socket.gethostbyname("onos"), port=6633)
net.addController(c0)
server = net.addDocker('server', ip='10.0.0.251', dcmd="python app.py", dimage="test_server:latest")
client = net.addDocker('client', ip='10.0.0.252', dimage="test_client:latest")

info('*** Setup network\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
net.addLink(server, s1)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s2, client)
net.start()

info('*** Starting to execute commands\n')

info('Execute: client.cmd("time curl 10.0.0.251:5000/mine")\n')
info(client.cmd("time curl 10.0.0.251:5000/mine") + "\n")

info('Execute: client.cmd("time curl 10.0.0.251:5000/chain")\n')
info(client.cmd("time curl 10.0.0.251:5000/chain") + "\n")

info('Execute: client.cmd("time curl 10.0.0.251:5000/mine")\n')
info(client.cmd("time curl 10.0.0.251:5000/mine") + "\n")

info('Execute: client.cmd("time curl 10.0.0.251:5000/chain")\n')
info(client.cmd("time curl 10.0.0.251:5000/chain") + "\n")

CLI(net)

net.stop()
