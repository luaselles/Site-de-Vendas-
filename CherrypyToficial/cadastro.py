import cherrypy as cherrypy
import sqlite3
import os
localDir = os.path.dirname(__file__)

class Cadastro():
    id=0
    nome=""
    senha=""
    fone=""
    email=""
    RG=""
    data=""
    @cherrypy.expose
    def index(self):
        html = open(localDir + "/fragments/topo.html").read()
        html += '''
                <br>
                <h1 style="margin-top:90px; margin-left:50px; letter-spacing: 1px; font-size:25px; font-family:arial;"> CADASTRO DO CLIENTE </h1>
                <br>
                <hr>
                <br>
                <form action="cliente" method="GET">
                    <div><label style="margin-left:50px;  letter-spacing: 1px; font-size:15px; font-family:arial;">Nome:</label><br></div>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="nome" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">Senha:</label></div>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="senha" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px;  letter-spacing: 1px; font-size:15px; font-family:arial;">Telefone:</label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="fone" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">E-mail:</label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="email" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">RG: </label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="RG" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">Data de Nascimento:</label>
                   <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" name="data" value="%s" type="date"/> </div>
                    <br>
                    <button style="margin-left:50px; margin-top:20px" class="button">Cadastrar</button>
                    <br>
                    <br>
                    
                </form>
        ''' % (self.nome, self.senha, self.fone, self.email, self.RG, self.data)

        #montar o corpo da tabela com os candidatos cadastrados#
        html += self.montartabela()

        html += open(localDir + "/fragments/base.html").read()
        return html

    def montartabela(self):
        html = '''<table style="background-color: #5d5d5d; margin-top:90px; width:90%; border: 2px solid #d0d0d0;" >'''
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        cursor.execute("select * from cliente order by nome")
        dados = cursor.fetchall()
        for linha in dados:
            html += '''
                <div>
                <tr><th style="color: white; text-align: justify;letter-spacing: 1px; font-size:15px; font-family:arial;">ID Cliente</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Nome Cliente</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Número Telefone</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Email Cliente</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">RG Cliente</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Data de Nascimento</th>
                </tr>
                <tr>
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td style="color: white; margin-left:100px; margin-right:80px; letter-spacing: 1px; font-size:20px; font-family:arial;">%s  </td> 
                <td><a href='apagar?id=%s'>Apagar</a></td> 
                <td><a href='alterar?id=%s'>Alterar</a></td> </tr></div>''' % (linha[0], linha[1], linha[3], linha[4], linha[5], linha[6], linha[0], linha[0])
        html += "</table>"
        return html

    @cherrypy.expose
    def alterar(self, id):
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        cursor.execute("select * from cliente where idcliente="+str(id))
        dados = cursor.fetchall()
        self.id = int(dados[0][0])
        self.nome = dados[0][1]
        self.senha = dados[0][2]
        self.fone = dados[0][3]
        self.email = dados[0][4]
        self.RG = dados[0][5]
        self.data = dados[0][6]
        cursor.close()
        con.close()
        raise cherrypy.HTTPRedirect('/.')

    @cherrypy.expose
    def apagar(self, id):
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        cursor.execute("delete from cliente where idcliente="+str(id))
        con.commit()
        con.close()
        raise cherrypy.HTTPRedirect('/.')

    @cherrypy.expose
    def cliente(self, nome, senha, fone, email, RG, data):
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        sucesso=True
        mensagem = "Erro ao cadastrar/alterar, clique <a href='/.'>aqui</a> para retornar"
        if self.id==0:
            sql = "insert into  cliente(nome,senha,fone,email,rg,data) values ('%s','%s','%s','%s','%s','%s')"%(nome, senha, fone, email, RG, data)
        else:
            sql = "update cliente set nome='%s',senha='%s',fone='%s',email='%s',rg='%s',data='%s' where idcliente=%d"%(nome, senha, fone, email, RG, data, self.id)
        try:
            cursor.execute(sql)
            con.commit()
        except:
            sucesso = False
        con.close()
        if not sucesso:
            return mensagem
        else:
            self.id = 0
            self.nome = self.senha = self.fone = self.email = self.RG = self.data = ""
            cherrypy.HTTPRedirect('/.')


#cherrypy.quickstart(Cadastro())
