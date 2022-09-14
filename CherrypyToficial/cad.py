import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class CAD:
    @cherrypy.expose
    def index(self):
        html = open(localDir+"/static/cadastro.html").read()
        return html