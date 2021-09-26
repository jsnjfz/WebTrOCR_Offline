#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020/4/28 14:54
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.web import StaticFileHandler
from backend.tools.get_host_ip import host_ip
from backend.webInterface import tr_run
from backend.webInterface import tr_index
from backend.tools import log
import logging
logger = logging.getLogger(log.LOGGER_ROOT_NAME+'.'+__name__)

current_path = os.path.dirname(__file__)
settings = dict(
    # debug=True,
    static_path=os.path.join(current_path, "")  # 配置静态文件路径
)


def make_app():
    return tornado.web.Application([
        #(r"/api/upload", kunshan_upload_async.Upload),
        #(r"/api/upload", kunshan_upload.Upload),
        (r"/api/tr-run/", tr_run.TrRun),
        (r"/", tr_index.Index),
        (r"/(.*)", StaticFileHandler,
         {"path": os.path.join(current_path, "dist/TrWebOcr_fontend"), "default_filename": "index.html"}),

    ], **settings)


if __name__ == "__main__":
    port = 8090
    app = make_app()
    server = tornado.httpserver.HTTPServer(app,max_buffer_size=504857600, max_body_size=504857600)
    # server.listen(port)
    server.bind(port)
    server.start(1)
    logger.info(f'server is running: {host_ip()}:{port}')

    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()
