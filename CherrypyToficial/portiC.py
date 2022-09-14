import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class PORTC:
    @cherrypy.expose
    def index(self):
        html = open(localDir+"/static/Oultimohomem.html").read()
        return html
