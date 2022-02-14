from mako.template import Template
import cherrypy

# cherrypy.engine.stop()
# cherrypy.server.httpserver = None
# cherrypy.config.update({'server.socket_port': 80})
# cherrypy.engine.start()


class Todo(object):
    @cherrypy.expose
    def index(self):

        mytemplate = Template(filename='template/index.html')
        return mytemplate.render()

    @cherrypy.expose
    def store(self, desc, date):
        return desc


if __name__ == '__main__':
    cherrypy.quickstart(Todo(), '/')
