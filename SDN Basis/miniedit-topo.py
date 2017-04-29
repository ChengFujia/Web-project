#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s7, s8)
    net.addLink(s7, s9)
    net.addLink(s8, h1)
    net.addLink(s9, h2)
    net.addLink(s10, h3)
    net.addLink(s10, h4)
    net.addLink(s6, s7)
    net.addLink(s7, s10)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s7').start([])
    net.get('s6').start([])
    net.get('s8').start([])
    net.get('s10').start([])
    net.get('s9').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()