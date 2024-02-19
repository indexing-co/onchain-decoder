import json
import os
import tornado

from utils.blocks import get_raw_block


class DecodeBlockHandler(tornado.web.RequestHandler):
    async def get(self, chain_id, block_number):
        raw_block = await get_raw_block(chain_or_id=chain_id, block_number=block_number)
        self.write(json.dumps(raw_block))


decode_handlers = [
    ("/decode/([A-z0-9]+)/block/([0-9]+)", DecodeBlockHandler),
]
