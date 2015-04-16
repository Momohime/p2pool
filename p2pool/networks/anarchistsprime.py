from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['anarchistsprime']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//5 # shares
REAL_CHAIN_LENGTH = 12*60*60//5 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'fc70035c7a81666f'.decode('hex')
PREFIX = '247666181efcd37b'.decode('hex')
P2P_PORT = 11050
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9666
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net pool.hostv.pl p2pool.org acp.explorer.ssdpool.com 52.16.23.106 52.17.116.144 178.62.102.181 173.16.173.143 104.155.18.57 128.199.111.217 109.88.89.62 58.7.251.128'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
