# TODO: include *all* chains supported by Indexing Co

CHAIN_ID_BY_NAME = {
    "base": 8453,
    "base_goerli": 84531,
    "base_sepolia": 84532,
    "eth_goerli": 5,
    "eth_sepolia": 11155111,
    "ethereum": 1,
    "linea": 59144,
    "lisk_sepolia": 4202,
    "lyra_sepolia": 901,
    "mode": 34443,
    "mode_sepolia": 919,
    "op_goerli": 420,
    "op_sepolia": 11155420,
    "optimism": 10,
    "orderly_sepolia": 4460,
    "pgn_sepolia": 58008,
    "public_goods_network": 424,
    "syndicate_frame_chain": 5101,
    "zora": 7777777,
    "zora_goerli": 999,
    "zora_sepolia": 999999999,
}

CHAIN_NAME_BY_ID = {v: k for k, v in CHAIN_ID_BY_NAME.items()}
