import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '01fefe05'.decode('hex')
P2P_PORT = 25255
ADDRESS_VERSION = 20
RPC_PORT = 25256
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'anarchistsprimeaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*256 >> (height + 1)//10256
POW_FUNC = data.hash256
BLOCK_PERIOD = 126 # s
SYMBOL = '256'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'anarchistsprime') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/AnarchistsPrime/') if platform.system() == 'Darwin' else os.path.expanduser('~/.anarchistsprime'), 'anarchistsprime.conf')
BLOCK_EXPLORER_URL_PREFIX = 'None'
ADDRESS_EXPLORER_URL_PREFIX = 'None'
TX_EXPLORER_URL_PREFIX = 'None'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
