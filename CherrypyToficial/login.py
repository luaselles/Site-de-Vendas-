import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class Lo:
    @cherrypy.expose
    def index(self):
        html = open(localDir+"/static/telalogin.html").read()
        return html
