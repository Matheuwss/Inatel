from mininet.topo import Topo

class MyTopo( Topo ):
    "8 hosts and 3 switches - custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, h7)
        self.addLink(s1, h8)

        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s2, h3)

        self.addLink(s3, h4)
        self.addLink(s3, h5)
        self.addLink(s3, h6)

topos = { 'mytopo': ( lambda: MyTopo() ) }