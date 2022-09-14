import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class Paginadeprodutos:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "/fragments/topo.html").read()
        html += self.carrega_corpo()
        html += open(localDir + "/fragments/base.html").read()
        return html

    def carrega_corpo(self):
        html='''
            <div><img src="/imagens/prod.jpg"></div>
            <header id="corpo">
              <div><h1 class="classeti">Modelos<br></h1><h5 class="classete">Adquira sua nova motocicleta</h5></div>
              <div class="fix LAS"><h3 class="classet">Honda CB 1000R</h3><br><br><img class="i" src="/imagens/coi.jpg">
               <a href="/pagprod/"><button class="buttonDETALHES">DETALHES</button></a></div>
              <div class="fix LAS"><h3 class="classet">CG 160 Fan</h3><br><br><img class="i" src="/imagens/coi1.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              <div class="fix LAS"><h3 class="classet">CG 160 Titan</h3><br><br><img class="i" src="/imagens/coi2.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              <div class="fix LAS"><h3 class="classet">PCX</h3><br><br><img class="i" src="/imagens/coi3.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              
              <header id="corpo">
               <div><h1 class="classeta">Novidades</h1><h5 class="classete">Adquira seus acessórios</h5></div>
              <div class="fix LAS"><h3 class="classet">CAPACETE X11 CROSSOVER GRAFITE</h3><br><br><img class="i" src="/imagens/cap.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              <div class="fix LAS"><h3 class="classet">Macacão Couro/Macacão Alpinestars</h3><br><br><img class="i" src="/imagens/mac.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              <div class="fix LAS"><h3 class="classet">Bauleto Pro-Tork 45 Litros Smart Box 2</h3><br><br><img class="i" src="/imagens/bau.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              <div class="fix LAS"><h3 class="classet">Luva X11 Impact 2 Cano Curto Couro Com Proteção</h3><br><br><img class="i" src="/imagens/luv.jpg">
              <button class="buttonDETALHES">DETALHES</button></div>
              </header> '''
        return html
