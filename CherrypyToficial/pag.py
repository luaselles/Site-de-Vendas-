import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class Pag:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "/fragments/topo.html").read()
        html += '''
                <style>
                #fix{position:fixed; width:200px; height:200px; top:200px; left:190px; background-color:white; border: 4px solid; border-color:#3e3e3e;}
              #fix2{position:fixed; width:100px; height:100px; top:420px; left:235px; background-color:white; color:#3e3e3e; text-align:center; font-family:arial;}
              #fix1{position:fixed; width:200px; height:200px; top:200px; left:555px; background-color:white; border: 4px solid; border-color:#3e3e3e;}
              #fix4{position:fixed; width:100px; height:100px;  top:420px; left:610px; background-color:white; color:#3e3e3e; text-align:center; font-family:arial;}
              #fix5{position:fixed; width:200px; height:200px; top:200px; left:910px; background-color:white; border: 4px solid; border-color:#3e3e3e;}
              #fix6{position:fixed; width:100px; height:100px; right:-10px; top:420px; left:690px; background-color:white; color:#3e3e3e; text-align:center; font-family:arial;}
                 .img{width:180px;margin-top: 10px; margin-left:10px;}
                 </style>
                 
                <div id="fix"><a href="/portiC/"><img class="img" src="/imagens/images2.png"></a></div>
                <div id="fix2"><h1>CAIO</h1></div>
                <div id="fix1"><a href="/portifolioL/"><img class="img" src="/imagens/images1.png"></a></div>
                <div id="fix4"><h1>LUANA</h1></div>
                <div id="fix5"><a href="/portifolio/"><img class="img" src="/imagens/images3.png"></a></div>
                <div id="fix6"><h1>MARINA</h1></div>
                
               <div style="background-color: #d0d0d0; height:200px; margin-top: 480px;
            width: 100%;"></div>
            </section>
            
            </body>
            </html>
        '''
        #html += open(localDir + "/fragments/base.html").read()
        return html
