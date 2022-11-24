

import tornado.ioloop # import the main event loop (Task Scheduler / Orchestra's Maestro )

"""
So as we know in tornado there's the concept of request handler,
which they're simple classes used to map the request to the request handler
So inside the main class(RequestHandler) there are many functions that will execute different requests.
"""


import tornado.web # Used to map the requests to the request handlers

class HelloHandler (tornado.web.RequestHandler): # So in tornado module we access(.) web package, and from it we access our request handler.
    def get(self): # self keyword is used to indicate that specific object I want to get, then whenever get function is triggred I want to write on a web page
        self.write("Hello Tornado 🌪️!")


# 1. As in any other framework (Django or flask .. ) we need a route to enter in browser in order to render the page
# 2. In tornado we will need an application which will be responsible for the routing system, which will map the requests to different request handlers
# 3. So in that main() we're going to include different functions that will include different request handlers


class PostHandler (tornado.web.RequestHandler):
    def get(self):
        self.write("<h1> This's post 1 📝</h1>")


# Just a handler to render static content based on an HTML file.
class HTMLHandler (tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


# Render dynamic content upon different input
class WeatherHandler (tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "Hot ☀️" if degree > 20 else "Cold 🌦️⛈️"
        drink = "Have some Juice 🍹" if degree > 20 else "you need a hot beverage ☕"
        self.render("weather.html", output = output, drink = drink)
        # emphasizing on above that the first output is gonna be whatever output gonna be displayed in as the outpput variable above depending on the degree



def make_app(): # Sometimes this function is called "main"
    return tornado.web.Application( # list of tuples actually
    [
        (r"/", HelloHandler), # r for route Default route
        (r"/post", PostHandler),
        (r"/home", HTMLHandler),
        (r"/weather", WeatherHandler)
    ],
    debug = True, # for Development 
    autoreload = True # In order to reflect all our changes into the webpage without interrupting the server.
    )

if __name__ == "__main__":
    app = make_app()
    """
    When we start server by default Tornado doesn't tell us that connection has been established or server is listening on port xyz or whatever host name is .. 

    So as a conequense and testing we're gonna print to check if all above operations are validated or not
    """
    # The Default port for Tornado is 8888 and we can enhance this by declaring a port variable to be changed later on 
    port = 8080
    app.listen(port)
    print(f"Server is listening on localhost on port {8888} ")

    # Now start the server on the current thread 
    tornado.ioloop.IOLoop.current().start()


