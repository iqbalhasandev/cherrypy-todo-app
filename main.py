from mako.template import Template
import cherrypy
import webbrowser

# cherrypy.log.screen = False
# cherrypy.config.update({'environment': 'production'})


class openBrowser():
    def callbrowser(self):
        url = 'http://127.0.0.1:8080/'
        # Open URL in a new tab, if a browser window is already open.
        webbrowser.open_new_tab(url)


cherrypy.engine.openBrowser = openBrowser()
cherrypy.engine.openBrowser.callbrowser()


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
