"""Custom realist topology example
   Based on Infocom 2018 paper:
   Iraja Tavares da Costa Filho, Roberto & Caggiani Luizelli, Marcelo & Gaspary, Luciano. (2018). 
   Scalable QoE-aware Path Selection in SDN-based Mobile Networks.
   RUN:
   # mn --custom topology.py --topo mytopo --controller remote,ip=172.28.0.13 --link tc --switch=ovs,protocols=OpenFlow13
"""

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import info,setLogLevel
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

class MyTopo( Topo ):
    "Realistic Topology."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        r1 = self.addHost( 'r1', ip='10.0.0.201', mac='00:04:00:00:0F:01')
        r2 = self.addHost( 'r2', ip='10.0.0.202', mac='00:04:00:00:0F:02')
        r3 = self.addHost( 'r3', ip='10.0.0.203', mac='00:04:00:00:0F:03')
        r4 = self.addHost( 'r4', ip='10.0.0.204', mac='00:04:00:00:0F:04')
        r5 = self.addHost( 'r5', ip='10.0.0.205', mac='00:04:00:00:0F:05')
        r6 = self.addHost( 'r6', ip='10.0.0.206', mac='00:04:00:00:0F:06')
        r7 = self.addHost( 'r7', ip='10.0.0.207', mac='00:04:00:00:0F:07')
        r8 = self.addHost( 'r8', ip='10.0.0.208', mac='00:04:00:00:0F:08')
        r9 = self.addHost( 'r9', ip='10.0.0.209', mac='00:04:00:00:0F:09')
        r10 = self.addHost( 'r10', ip='10.0.0.210', mac='00:04:00:00:0F:10')
        r11 = self.addHost( 'r11', ip='10.0.0.211', mac='00:04:00:00:0F:11')
        r12 = self.addHost( 'r12', ip='10.0.0.212', mac='00:04:00:00:0F:12')
        r13 = self.addHost( 'r13', ip='10.0.0.213', mac='00:04:00:00:0F:13')
        r14 = self.addHost( 'r14', ip='10.0.0.214', mac='00:04:00:00:0F:14')
        r15 = self.addHost( 'r15', ip='10.0.0.215', mac='00:04:00:00:0F:15')
        r16 = self.addHost( 'r16', ip='10.0.0.216', mac='00:04:00:00:0F:16')
        r17 = self.addHost( 'r17', ip='10.0.0.217', mac='00:04:00:00:0F:17')
        r18 = self.addHost( 'r18', ip='10.0.0.218', mac='00:04:00:00:0F:18')
        r19 = self.addHost( 'r19', ip='10.0.0.219', mac='00:04:00:00:0F:19')
        r20 = self.addHost( 'r20', ip='10.0.0.220', mac='00:04:00:00:0F:20')
        m1 = self.addHost( 'm1', ip='10.0.0.221', mac='00:04:00:00:0F:21')
        m2 = self.addHost( 'm2', ip='10.0.0.222', mac='00:04:00:00:0F:22')
        m3 = self.addHost( 'm3', ip='10.0.0.223', mac='00:04:00:00:0F:23')
        m4 = self.addHost( 'm4', ip='10.0.0.224', mac='00:04:00:00:0F:24')
        m5 = self.addHost( 'm5', ip='10.0.0.225', mac='00:04:00:00:0F:25')
        a1 = self.addHost( 'a1', ip='10.0.0.226', mac='00:04:00:00:0F:26')
        a2 = self.addHost( 'a2', ip='10.0.0.227', mac='00:04:00:00:0F:27')
        a3 = self.addHost( 'a3', ip='10.0.0.228', mac='00:04:00:00:0F:28')
        a4 = self.addHost( 'a4', ip='10.0.0.229', mac='00:04:00:00:0F:29')
        c1 = self.addHost( 'c1', ip='10.0.0.230', mac='00:04:00:00:0F:30')
        c2 = self.addHost( 'c2', ip='10.0.0.231', mac='00:04:00:00:0F:31')
        c3 = self.addHost( 'c3', ip='10.0.0.232', mac='00:04:00:00:0F:32')
        c4 = self.addHost( 'c4', ip='10.0.0.233', mac='00:04:00:00:0F:33')
        i1 = self.addHost( 'i1', ip='10.0.0.234', mac='00:04:00:00:0F:34')
        #Add hosts
        u001 = self.addHost( 'u001', ip='10.0.0.1', mac='00:04:00:00:00:01')

        cdn1 = self.addHost( 'cdn1', ip='10.0.0.251', mac='00:04:00:00:02:51')
        cdn2 = self.addHost( 'cdn2', ip='10.0.0.252', mac='00:04:00:00:02:52')
        cdn3 = self.addHost( 'cdn3', ip='10.0.0.253', mac='00:04:00:00:02:53')
        ext1 = self.addHost( 'ext1', ip='10.0.0.254', mac='00:04:00:00:02:54')
       
        # Add 34 switches
        s1 = self.addSwitch('s1')  #R1
        s2 = self.addSwitch('s2')  #R2
        s3 = self.addSwitch('s3')  #R3
        s4 = self.addSwitch('s4')  #R4
        s5 = self.addSwitch('s5')  #R5
        s6 = self.addSwitch('s6')    #R6
        s7 = self.addSwitch('s7')    #R7
        s8 = self.addSwitch('s8')    #R8
        s9 = self.addSwitch('s9')    #R9
        s10 = self.addSwitch('s10')  #R10
        s11 = self.addSwitch('s11')  #R11
        s12 = self.addSwitch('s12')  #R12
        s13 = self.addSwitch('s13')  #R13
        s14 = self.addSwitch('s14')  #R14
        s15 = self.addSwitch('s15')  #R15
        s16 = self.addSwitch('s16')  #R16
        s17 = self.addSwitch('s17')  #R17
        s18 = self.addSwitch('s18')  #R18
        s19 = self.addSwitch('s19')  #R19
        s20 = self.addSwitch('s20')  #R20
        s21 = self.addSwitch('s21')  #M1
        s22 = self.addSwitch('s22')  #M2
        s23 = self.addSwitch('s23')  #M3
        s24 = self.addSwitch('s24')  #M4
        s25 = self.addSwitch('s25')  #M5
        s26 = self.addSwitch('s26')  #A1
        s27 = self.addSwitch('s27')  #A2
        s28 = self.addSwitch('s28')  #A3
        s29 = self.addSwitch('s29')  #A4
        s30 = self.addSwitch('s30')  #C1
        s31 = self.addSwitch('s31')  #C2
        s32 = self.addSwitch('s32')  #C3
        s33 = self.addSwitch('s33')  #C4
        s34 = self.addSwitch('s34')  #I1 (Internet)

        # Link parameters
        link100Mbps = dict(bw=20, delay='15ms' )
        link1Gbps = dict(bw=200, delay='5ms')
        linknodeg = dict()

        link100Mbps_1 = dict(bw=20, delay='1ms')
        link100Mbps_4 = dict(bw=20, delay='4ms')
        link100Mbps_5 = dict(bw=20, delay='5ms')
        link100Mbps_6 = dict(bw=20, delay='6ms')
        link100Mbps_7 = dict(bw=20, delay='7ms')
        link100Mbps_8 = dict(bw=20, delay='8ms')
        link100Mbps_9 = dict(bw=20, delay='9ms')
        link100Mbps_10 = dict(bw=20, delay='10ms')
        link100Mbps_11 = dict(bw=20, delay='11ms')
        link100Mbps_15 = dict(bw=20, delay='15ms')
        link100Mbps_20 = dict(bw=20, delay='20ms')
        link100Mbps_25 = dict(bw=20, delay='25ms')
        link100Mbps_30 = dict(bw=20, delay='30ms')
  
        link1Gbps_1 = dict(bw=200, delay='1ms')
        link1Gbps_12 = dict(bw=200, delay='12ms')
        link1Gbps_15 = dict(bw=200, delay='15ms')
        link1Gbps_18 = dict(bw=200, delay='18ms')
        link1Gbps_20 = dict(bw=200, delay='20ms')
        link1Gbps_23 = dict(bw=200, delay='23ms')
        link1Gbps_25 = dict(bw=200, delay='25ms')
        link1Gbps_30 = dict(bw=200, delay='30ms')
      
        # Add links
        #1.2. CREATING LINKS
        self.addLink( cdn1, s25, 0, 99, **link100Mbps_1)
        self.addLink( cdn2, s29, 0, 99, **link1Gbps_1)
        self.addLink( cdn3, s31, 0, 99, **link1Gbps_1)
        self.addLink( ext1, s34, 0, 99, **link1Gbps_30)

        self.addLink( r1, s1, 0, 100)
        self.addLink( r2, s2, 0, 100)
        self.addLink( r3, s3, 0, 100)
        self.addLink( r4, s4, 0, 100)
        self.addLink( r5, s5, 0, 100)
        self.addLink( r6, s6, 0, 100)
        self.addLink( r7, s7, 0, 100)
        self.addLink( r8, s8, 0, 100)
        self.addLink( r9, s9, 0, 100)
        self.addLink( r10, s10, 0, 100)
        self.addLink( r11, s11, 0, 100)
        self.addLink( r12, s12, 0, 100)
        self.addLink( r13, s13, 0, 100)
        self.addLink( r14, s14, 0, 100)
        self.addLink( r15, s15, 0, 100)
        self.addLink( r16, s16, 0, 100)
        self.addLink( r17, s17, 0, 100)
        self.addLink( r18, s18, 0, 100)
        self.addLink( r19, s19, 0, 100)
        self.addLink( r20, s20, 0, 100)
        self.addLink( m1, s21, 0, 100)
        self.addLink( m2, s22, 0, 100)
        self.addLink( m3, s23, 0, 100)
        self.addLink( m4, s24, 0, 100)
        self.addLink( m5, s25, 0, 100)
        self.addLink( a1, s26, 0, 100)
        self.addLink( a2, s27, 0, 100)
        self.addLink( a3, s28, 0, 100)
        self.addLink( a4, s29, 0, 100)
        self.addLink( c1, s30, 0, 100)
        self.addLink( c2, s31, 0, 100)
        self.addLink( c3, s32, 0, 100)
        self.addLink( c4, s33, 0, 100)
        self.addLink( i1, s34, 0, 100)

        #3. CREATING LINKS BETWEEN SWITCHES
        #Level 3.1 - RAN / Metro ->   link100Mbps_5
        self.addLink( s1, s21, 31, 1, **link100Mbps_5)
        self.addLink( s2, s21, 31, 2, **link100Mbps_5)
        self.addLink( s3, s21, 31, 3, **link100Mbps_5)
        self.addLink( s4, s21, 31, 4, **link100Mbps_5)

        self.addLink( s5, s22, 31, 1, **link100Mbps_5)
        self.addLink( s6, s22, 31, 2, **link100Mbps_5)
        self.addLink( s7, s22, 31, 3, **link100Mbps_5)
        self.addLink( s8, s22, 31, 4, **link100Mbps_5)

        self.addLink( s9, s23, 31, 1, **link100Mbps_5)
        self.addLink( s10, s23, 31, 2, **link100Mbps_5)
        self.addLink( s11, s23, 31, 3, **link100Mbps_5)
        self.addLink( s12, s23, 31, 4, **link100Mbps_5)

        self.addLink( s13, s24, 31, 1, **link100Mbps_5)
        self.addLink( s14, s24, 31, 2, **link100Mbps_5)
        self.addLink( s15, s24, 31, 3, **link100Mbps_5)
        self.addLink( s16, s24, 31, 4, **link100Mbps_5)

        self.addLink( s17, s25, 31, 1, **link100Mbps_5)
        self.addLink( s18, s25, 31, 2, **link100Mbps_5)
        self.addLink( s19, s25, 31, 3, **link100Mbps_5)
        self.addLink( s20, s25, 31, 4, **link100Mbps_5)

        #Level 3.1.5 - Metro Ring ->   link100Mbps_5
        self.addLink( s21, s22, 5, 5, **link100Mbps_5)
        self.addLink( s22, s23, 6, 6, **link100Mbps_5)
        self.addLink( s23, s24, 5, 5, **link100Mbps_5)
        self.addLink( s24, s25, 6, 6, **link100Mbps_5)
        self.addLink( s25, s21, 5, 6, **link100Mbps_5) #Link to close ring

        #Level 3.2 - Metro / Access ->   link100Mbps_15
        self.addLink( s22, s27, 7, 1, **link100Mbps_15)
        self.addLink( s23, s28, 7, 1, **link100Mbps_15)

        #Level 3.2.5 - Access ring ->   link100Mbps_10
        self.addLink( s26, s27, 3, 3, **link100Mbps_10)
        self.addLink( s27, s28, 2, 2, **link100Mbps_10)
        self.addLink( s28, s29, 3, 3, **link100Mbps_10)
        self.addLink( s29, s26, 2, 2, **link100Mbps_10) #Link to close ring

        #Level 3.3 - Access / Core ->   link100Mbps_20
        self.addLink( s26, s30, 4, 1, **link100Mbps_20)
        self.addLink( s27, s30, 4, 2, **link100Mbps_20)
        self.addLink( s28, s31, 4, 1, **link100Mbps_20)
        self.addLink( s29, s31, 4, 2, **link100Mbps_20)

        #Level 3.4 - Full-mesh Core ->   link100Mbps_20
        self.addLink( s30, s31, 3, 3, **link100Mbps_20)
        self.addLink( s30, s32, 4, 4, **link100Mbps_20)
        self.addLink( s30, s33, 5, 5, **link100Mbps_20)
        self.addLink( s31, s32, 5, 5, **link100Mbps_20)
        self.addLink( s31, s33, 4, 4, **link100Mbps_20)
        self.addLink( s32, s33, 3, 3, **link100Mbps_20)

        #Level 3.5 - Core / Internet ->   link100Mbps_30
        self.addLink( s32, s34, 1, 1, **link100Mbps_30)
        self.addLink( s33, s34, 1, 2, **link100Mbps_30)
      
        #4.2. CREATING LINKS
        self.addLink( u001, s1, 0, 1)


topos = { 'mytopo': ( lambda: MyTopo() ) }
