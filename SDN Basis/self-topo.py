from mininet.topo import Topo

class Testtopo(Topo):
	def __init__(self):
    		"create a test topology"
		Topo.__init__(self)

		S1 = self.addSwitch('s1')
		S2 = self.addSwitch('s2')
		S3 = self.addSwitch('s3')
		S4 = self.addSwitch('s4')

		H1 = self.addHost('h1')
		H2 = self.addHost('h2')

		self.addLink(S1,S2)
		self.addLink(S2,S3)
		self.addLink(S2,S4)
		self.addLink(S3,H1)
		self.addLink(S4,H2)

topos = {
	'firsttopo':(lambda:Testtopo())
}