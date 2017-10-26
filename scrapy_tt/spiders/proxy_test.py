import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path
import socket
from tornado.escape import json_decode, json_encode


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write(self.request.headers['user-agent'] + \
#                    "\nyour current ip is: " + self.request.remote_ip)
#
#
# if __name__ == "__main__":
#     application = tornado.web.Application([(r"/", MainHandler)], debug=True)
#     http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.instance().start()


# from tornado import httpserver
# from tornado import ioloop
#
#
# def handle_request(request):
#     message = "You requested %s\n" % request.uri
#     request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (len(message), message))
#     request.finish()
#
#
# http_server = httpserver.HTTPServer(handle_request)
# http_server.bind(8888)
# http_server.start()
# ioloop.IOLoop.instance().start()

# import tornado.httpserver
# import tornado.ioloop
# import tornado.web
#
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
#
# application = tornado.web.Application([
#     (r"/", MainHandler),
# ])
#
# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()
class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def get(self):
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', friendly user!')
        # self.write(self.request.remote_ip + ':' + str(self.request.connection.context.address[1]))
        self.write(json_encode(self.request.remote_ip + ':' + str(self.request.connection.context.address[1])))
        print(self.request.remote_ip)
        print(self.request.connection.context.address[1])
    # @tornado.web.asynchronous
    # def get(self):
    #     # 获取请求体
    #     body = self.request.body
    #     if not body:
    #         body = None
    #     try:
    #         # 代理发送请求
    #         render_request(
    #             self.request.uri,
    #             callback=self.on_response,
    #             method=self.request.method,
    #             body=body,
    #             headers=self.request.headers,
    #             follow_redirects=False,
    #             allow_nonstandard_methods=True)
    #     except tornado.httpclient.HTTPError as httperror:
    #         if hasattr(httperror, 'response') and httperror.response:
    #             self.on_response(httperror.response)
    #         else:
    #             self.set_status(500)
    #             self.write('Internal server error:\n' + str(httperror))
    #             self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



