import cherrypy as cherrypy
import os

from produtos import Paginadeprodutos
from pag import Pag
from cadastro import Cadastro
from portifolio import PORT
from pagprod import Paginaprod
from cadastroVende import CadastrodeVende
from portifolioL import PORTL
from portiC import PORTC
from cad import CAD
from login import Lo
localDir = os.path.dirname(__file__)

class Home:
    @cherrypy.expose
    def index(self):
        html = open(localDir+"/fragments/topo.html").read()
        html +='''
            <div><img class="sapo" src="/imagens/fixo.jpg"><img class="cl" src="/imagens/abaixo.jpg"></div>
                <div><img class="ganhocl" src="/imagens/ganhohome.jpg"></div>
                <div><h1 class="textganhocl">RIDER CHALLENGE</h1><br>
                <p class="textganhocl1">Pronto(a) para provar a sua paixão pelo <br> motociclismo e
                concorrer à uma Low Rider® S? </p></div>
                <div><button class="cll butt butt2">Participe</button></div>
            
                <div><img class="boacl" src="/imagens/ganhohome1.jpg"></div>
                
                <div><h1 class="textganhocl2">DEIXE O SEU PASSEIO <br> MAIS COMPLETO</h1><br>
                <p class="textganhocl3">A Skull Motors oferece horas de pilotagem<br>empolgante, vitórias
                em corridas, 117 anos<br>de história e muito mais.</p></div>
                <div><button class="cll2 butt butt2">Participe</button></div>
                <br>'''
        html += open(localDir+"/fragments/base.html").read()
        return html

# objetos para cada classe:
root = Home()
root.produtos = Paginadeprodutos()
root.pag = Pag()
root.cadastro = Cadastro()
root.portifolio = PORT()
root.cadastroVende = CadastrodeVende()
root.pagprod = Paginaprod()
root.portifolioL= PORTL()
root.portiC= PORTC()
root.cad = CAD()
root.login = Lo()
local_config = {'/': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': localDir}}
cherrypy.quickstart(root, config=local_config)