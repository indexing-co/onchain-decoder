import tornado


class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("pong")


class GCPHealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)


health_check_handlers = [
    ("/ping", PingHandler),
    ("/_ah/health", GCPHealthHandler),
]
