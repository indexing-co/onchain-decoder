import gzip
import os
import tornado

from .constants import CHAIN_ID_BY_NAME, CHAIN_NAME_BY_ID


CHAIN_HOST = os.environ.get(
    "CHAIN_HOST", "https://storage.googleapis.com/indexingco_heartbeats"
)


"""
    TODO
    future abstractions include:
        - falling back to RPCs when appropriate
        - using GCS commands directly when permissions are available
"""


async def get_raw_block(chain_or_id, block_number):
    if chain_or_id.isdigit():
        chain_or_id = CHAIN_NAME_BY_ID[int(chain_or_id)]

    if chain_or_id not in CHAIN_ID_BY_NAME:
        raise Exception("Invalid chain provided")

    if not block_number.isdigit():
        raise Exception("invalid block number provided")

    full_url = f"{CHAIN_HOST}/{chain_or_id}/{block_number}.json.gz"

    http = tornado.httpclient.AsyncHTTPClient()
    response = await http.fetch(full_url, validate_cert=False)
    block_str = gzip.decompress(response.buffer.read())
    return tornado.escape.json_decode(block_str)
