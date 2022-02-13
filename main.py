import cherrypy


class Todo(object):
    @cherrypy.expose
    def index(self):

        return """
        <html>

        <body>

            <form method="POST" action="store">
                <h1>Store Your Todo</h1>
                <br>
                <br><br>
                <label for="desc">Todo Content</label>
                <br/>
                <textarea name="desc" id="desc"></textarea>
                <br/>
                <br/>

                <label for="date">Date</label>
                <br/>

                <input type="date" name="date" id="date">
                <br/>
                <br/>
                <button type="submit">Store Todo</button>
            </form>
        </body>

        </html>
        """

    @cherrypy.expose
    def store(self, desc, date):
        return desc


if __name__ == '__main__':
    cherrypy.quickstart(Todo(), '/')
