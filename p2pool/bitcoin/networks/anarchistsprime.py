import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 11050
ADDRESS_VERSION = 0
RPC_PORT = 21050
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'anarchistsprimeaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 32*53760000 >> (height + 1)//840000
POW_FUNC = data.hash256
BLOCK_PERIOD = 180 # s
SYMBOL = 'APC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'anarchistsprime') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/AnarchistsPrime/') if platform.system() == 'Darwin' else os.path.expanduser('~/.anarchistsprime'), 'anarchistsprime.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/address/'
TX_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
