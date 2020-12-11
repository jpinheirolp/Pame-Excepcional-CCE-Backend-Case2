from ..extensions import db

class Usuario(db.Model):
    
    __tablename__ = 'usuario'   
    
    id_usuario = db.Column(db.Integer,primary_key = True)
    
    nome = db.Column(db.String(40),nullable = False)
    senha = db.Column(db.String(50),nullable = False)
    telefone = db.Column(db.String(15),nullable = False, unique = True)
    email = db.Column(db.String(50),nullable = False, unique = True)
    
    data_criacao_perfil = db.Column(db.Date(),nullable = False)
    Posts = db.relationship('Post', backref='usuario')
    Comentarios = db.relationship('Comentario', backref='usuario')

