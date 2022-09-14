import sqlite3
import cherrypy as cherrypy
import os
localDir = os.path.dirname(__file__)
class CadastrodeVende():
    id=0
    nomevende=""
    senhavende=""
    telefonevende=""
    emailvende=""
    rgvende=""
    datavende=""
    @cherrypy.expose
    def index(self):
        html = open(localDir + "/fragments/topo.html").read()
        html +='''
                <br>
                <h1 style="margin-top:90px; margin-left:50px; letter-spacing: 1px; font-size:25px; font-family:arial;"> CADASTRO DO VENDEDOR </h1>
                <br>
                <hr>
                <br>
                <form action="vendedores" method="GET">
                    <div><label style="margin-left:50px;  letter-spacing: 1px; font-size:15px; font-family:arial;">Nome do Vendedor:</label><br></div>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="nomevende" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">Senha:</label></div>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="senhavende" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px;  letter-spacing: 1px; font-size:15px; font-family:arial;">Telefone do Vendedor:</label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="telefonevende" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">E-mail do Vendedor:</label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="emailvende" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">RG do Vendedor: </label>
                    <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" type="text" name="rgvende" value="%s"/></div>
                    <br>
                    <div><label style="margin-left:50px; letter-spacing: 1px; font-size:15px; font-family:arial;">Data de Nascimento:</label>
                   <div><input style="margin-left:50px; border: 1px solid #ccc; width: 1000px; height: 40px;" name="datavende" value="%s" type="date"/> </div>
                    <br>
                    <button style="margin-left:50px; margin-top:20px" class="button">Cadastrar</button>
                    <br>
                    <br>
                    
                </form>
        ''' % (self.nomevende, self.senhavende, self.telefonevende, self.emailvende, self.rgvende, self.datavende)

        # montar o corpo da tabela com os candidatos cadastrados#
        html += self.montartabela()

        html += open(localDir + "/fragments/base.html").read()
        return html

    def montartabela(self):
        html = '''<table style="background-color: #5d5d5d; margin-top:90px; width:90%; border: 2px solid #d0d0d0;" >'''
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        cursor.execute("select * from vendedores order by nomevende")
        dados = cursor.fetchall()
        for linha in dados:
            html += '''
                <div>
                <tr><th style="color: white; text-align: justify;letter-spacing: 1px; font-size:15px; font-family:arial;">ID Vendedor</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Nome Vendedor</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Número Telefone</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">Email Vendedor</th>
                <th style="color: white; text-align: justify; letter-spacing: 1px; font-size:15px; font-family:arial;">RG Vendedor</th>
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
        cursor.execute("select * from vendedores where idvende="+str(id))
        dados = cursor.fetchall()
        self.id = int(dados[0][0])
        self.nomevende = dados[0][1]
        self.senhavende = dados[0][2]
        self.telefonevende = dados[0][3]
        self.emailvende = dados[0][4]
        self.rgvende = dados[0][5]
        self.datavende = dados[0][6]
        cursor.close()
        con.close()
        raise cherrypy.HTTPRedirect('/.')

    @cherrypy.expose
    def apagar(self,id):
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        cursor.execute("delete from vendedores where idvende="+str(id))
        con.commit()
        con.close()
        raise cherrypy.HTTPRedirect('/.')

    @cherrypy.expose
    def cliente(self, nomevende, senhavende, telefonevende, emailvende, rgvende, datavende):
        con = sqlite3.connect("C:\\Users\\lusel\\Desktop\\AMB_E/cadastro.db")
        cursor = con.cursor()
        sucesso=True
        mensagem = "Erro ao cadastrar/alterar, clique <a href='/.'>aqui</a> para retornar"
        if self.id==0:
            sql = "insert into vendedores(nomevende,senhavende,telefonevende,emailvende,rgvende,datavende) values ('%s','%s','%s','%s','%s','%s')"%(nomevende, senhavende, telefonevende, emailvende, rgvende, datavende)
        else:
            sql = "update vendedores set nomevende='%s',senhavende='%s',telefonevende='%s',emailvende='%s',rgvende='%s',datavende='%s' where idcliente=%d"%(nomevende, senhavende, telefonevende, emailvende, rgvende, datavende,self.id)
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
            self.nomevende = self.senhavende = self.telefonevende = self.emailvende = self.rgvende = self.datavende=""
            cherrypy.HTTPRedirect('/.')


#cherrypy.quickstart(CadastrodeVende())
