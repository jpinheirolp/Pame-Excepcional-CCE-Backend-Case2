from ..extensions import db
import datetime

class Usuario(db.Model):
    
    __tablename__ = 'usuario'   
    
    id_usuario = db.Column(db.Integer,primary_key = True)
    
    nome = db.Column(db.String(40),nullable = False)
    senha = db.Column(db.String(50),nullable = False)
    telefone = db.Column(db.String(15),nullable = False, unique = True)
    email = db.Column(db.String(50),nullable = False, unique = True)
    
    #data_criacao_perfil = db.Column(db.DateTime,default = datetime.datetime.now())
    #Posts = db.relationship('Post', backref='usuario')
    #Comentarios = db.relationship('Comentario', backref='usuario')
    #Enquetes = db.relationship('Enquete', backref='usuario')
    #Respostas = db.relationship('Resposta_Enquete', backref='usuario')

    def json(self):
        return {
            #"id": self.id_usuario,
            "nome": self.nome,
            "senha": self.senha,
            "telefone": self.telefone,
            "email": self.email,
            #"data_criacao_perfil": self.data_criacao_perfil,
            #"posts": self.Posts,
            #"comentarios": self.Comentarios
        }
