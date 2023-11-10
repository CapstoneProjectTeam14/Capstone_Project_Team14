from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController

class CustomTorusTopology(Topo):
    def build(self):
        # Create switches in a 2x2 grid
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Connect switches in a torus-like fashion
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)

        # Add hosts to each switch
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

def create_and_start_topology():
    # Create a Mininet network with the custom torus-like topology
    net = Mininet(topo=CustomTorusTopology(), controller=None)

    # Add ONOS controllers
    onos_ips = ["Controller_IP_1", "Controller_IP_2", "Controller_IP_3", "Controller_IP_4"]
    for i in range(4):
        controller = RemoteController(f"c{i+1}", ip=onos_ips[i])
        net.addController(controller)

    # Start the Mininet network
    net.start()

    # Open a Mininet command line interface
    net.interact()

    # Clean up after exiting the Mininet CLI
    net.stop()

if __name__ == '__main__':
    create_and_start_topology()

