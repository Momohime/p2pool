from p2pool.bitcoin import networks

PARENT = networks.nets['ecurrency']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'aae0f7b3e7a122e0'.decode('hex')
PREFIX = 'bba7f2e40a11b75a'.decode('hex')
P2P_PORT = 8179
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9179
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
