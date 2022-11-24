import tornado.web
import tornado.ioloop
import pyrqlite.dbapi2 as dbapi2
import os

from periodictable import returnMainText, getElementDetails


class PeriodicTableDisplayHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(returnMainText())

class ElementHandler(tornado.web.RequestHandler):
    def get(self, variable):
        self.write(getElementDetails(variable))
        
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", PeriodicTableDisplayHandler),
        (r"/element/(.*)", ElementHandler),
    ])
    osEnviron = os.environ.get("PORT")
    envPort = 8080
    if osEnviron:
        envPort = osEnviron
    else:
        envPort = 8080
    app.listen(envPort)
    print("I'm listening on port" + str(envPort))
    tornado.ioloop.IOLoop.current().start()
