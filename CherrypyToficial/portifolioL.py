import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class PORTL:
    @cherrypy.expose
    def index(self):
        html = open(localDir+"/static/PORTIFOLIO.html").read()
        return html
