from ..extensions import db

class Post(db.Model):
    
    __tablename__ = 'post'
    
    id_post = db.Column(db.Integer,primary_key = True)
    
    localizacao = db.Column(db.String(40),default = "Não informado")
    descricao = db.Column(db.String(200),default = "descrição")
    imagem = db.Column(db.String(50),nullable = False) # ainda não sei como colocar uma imagem
    data_post = db.Column(db.DateTime(),nullable = False)
    
    usuario_post = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),nullable = False)
    Comentarios = db.relationship('Comentario', backref='post')