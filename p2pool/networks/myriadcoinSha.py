 from p2pool.bitcoin import networks
 
 PARENT = networks.nets['myriadcoinSha'],
        SHARE_PERIOD=10, # seconds
        NEW_SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='fc70135c700a00ee'.decode('hex'),
        PREFIX='9472ef181e88efcb'.decode('hex'),
        P2P_PORT=5577,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=5578,
        BOOTSTRAP_ADDRS='birdspool.no-ip.org nz.p2pool.geek.nz uk.p2pool.geek.nz meziti.nl'.split(' '),
        #ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: True,