import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)

class PORT:
    @cherrypy.expose
    def index(self):
        html = self.carregacorpo()
        return html

    def carregacorpo(self):
        html = '''
            <style type="text/css">
           
            *{font-family: arial; margin: 0.25cm; }
            
            #principal {width: 90%; margin: 0 auto;}
            #topo {width: 100%; height: 40px; background-color: #CDCDCD; float: left; font-family: arial-black; font-size: 25px; vertical-align: middle; border: 2px solid #BCBBBB; text-align: center; color: #767676; text-shadow: 1px 1px 1px #3B3838;}
            #conteudo {width: 100%; height: 1325px; background-color: #FFFFFF; float: left; border: 2px solid #CDCDCD; text-align: center;}
            #rodape {width: 100%; height: 20px; background-color: #CDCDCD; float: left; font-size: 15px; border: 2px solid #BCBBBB; text-align: center;}
            
            h1 {color: #767676;
            font-family: arial-black;
            font-style: normal;
            margin-top: 0.5;
            margin-left: 0.5cm;
            text-shadow: 1px 1px 1px #3B3838;}
            p{margin-left: 0.5cm;}
            
            body{background-image: url("/imagens/triangulos.jpg");}
        </style>
                <section id="principal">
                        <header id="topo">
                            PORTFÓLIO PESSOAL
                        </header>
                        <article id="conteudo">
                            <h1>Sobre mim:</h1>
                            <hr>
                            <p>Nome: Marina Zeni Oliveira Marques Caderan.</p>
                            <p>Idade: 19 anos.</p>
                            <p>Estudante</p>
                            <hr>
                            <h1>Séries preferidas:</h1>
                            <hr>
                            <p style="text-align: center; ">The Good Place</p>
                            <img src="/imagens/TGP.jpg">
                            <p style="text-align: center; ">Mindhunter</p>
                            <img src="/imagens/MINDHUNTER.jpg">
                            <p style="text-align: center; ">House of Cards</p>
                            <img src="/imagens/HOC.png">
                            <hr>
                            <h1>Livros preferidos:</h1>
                            <hr>
                            <p>As crônicas de Gelo e Fogo</p>
                            <p>David Copperfield</p>
                            <p>Fahrenheit 451</p>
                        </article>
                        <footer id="rodape">
                            Rodapé
                        </footer>
                    </section>
                
                
                </body>
                </html>'''
        return html