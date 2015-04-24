from p2pool.bitcoin import networks

PARENT = networks.nets['titcoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//1 # shares
REAL_CHAIN_LENGTH = 12*60*60//4 # shares
TARGET_LOOKBEHIND = 69 # shares
SPREAD = 69 # blocks
IDENTIFIER = 'fc70035c7a86969f'.decode('hex')
PREFIX = '247696981efcd37b'.decode('hex')
P2P_PORT = 8698
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 16969
BOOTSTRAP_ADDRS = 'mining.p2pools.com rav3n.dtdns.net pool.hostv.pl p2pool.org seed.titcoins.info titcoin.hopto.org titcoin.isasecret.com titcoin.slyip.com titcoin.sytes.net 108.61.10.90 95.85.23.9 109.120.173.59 188.165.84.239'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
