import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class Paginaprod:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "/fragments/topo.html").read()
        html += self.carrega_corpo()
        html += open(localDir + "/fragments/base.html").read()
        return html

    def carrega_corpo(self):
        html='''
        <header>
            <div><img class="sapo" src="/imagens/fundi_prod.jpg"></div>
            <div><img class="clab" src="/imagens/boa.jpg">
            <img class="clab" src="/imagens/enco.jpg"></div>
            <br>
            <img class="clab" src="/imagens/baixo.jpg"></div>
            <br><br>
            <h1 class="textw">DESCRIÇÃO DA MOTO</h1>
            <br><br>
            <p><ul class="textww">
                <li>apenas 17.001 KM</li>
                <br>
                <li>manual do proprietário</li>
                <br>
                <li>ABS COM NÍVEIS DE AJUSTES</li>
                <br>
                 <li>Amortecedor de Direção</li>
                 <br>
                  <li>Controle de Tração . Eletrônico 8 Níveis</li>
                  <br>
                   <li>Computador de Bordo</li>
                   <br>
                    <li>Regulagem de Suspensão . Eletrônico</li>
                    <br>
                    <li>3 Modos de Pilotagem</li>
                    <br>
                    <li>Farol em LED</li>
                    <br>
                    <li>Pisca em LED</li>
                    <br>
                    <li> Contra-Peso de Guidon</li>
                    <br>
                    <li>Painel Digital</li>
                    <br>
              </ul>
            </p>
            <hr>
            <br>
            <p class="tis"><b>Marca:</b> Honda</p>
            <br>
            <p class="tis"><b>Modelo:</b> 1299 Panigale</p>
             <br>
            <p class="tis"><b>Cilindradas:</b> 1000</p>
             <br>
            <p class="tis"><b>Km:</b> 17001</p>
             <br>
            <p class="tis"><b>Estilo:</b> Esportiva</p>
             <br>
             <hr>
             <br>
             <h1 class="textw">OUTRAS INFORMAÇÕES</h1>
            <br><br>
            <p class="tis"><b>IPVA pago:</b> Sim</p>
            <br>
            <p class="tis"><b>Veículo licenciado:</b> Sim</p>
            </header>'''
        return html