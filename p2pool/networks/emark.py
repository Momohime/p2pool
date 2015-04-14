from p2pool.bitcoin import networks

PARENT = networks.nets['emark']
SHARE_PERIOD = 120 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'fc70035c7a81dede'.decode('hex')
PREFIX = '247dede81efcd37b'.decode('hex')
P2P_PORT = 5556
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 5555
BOOTSTRAP_ADDRS = 'mining.p2pools.com rav3n.dtdns.net pool.hostv.pl p2pool.org ispace.co.uk emark.securepayment.cc 46.163.71.216 85.214.33.151 213.136.71.190'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
