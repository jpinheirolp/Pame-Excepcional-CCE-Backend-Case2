from ..extensions import db

class Enquete(db.Model):
    
    __tablename__ = 'enquete'
    
    id_enquete = db.Column(db.Integer,primary_key = True)
    
    pergunta = db.Column(db.String(200),nullable = False)
    data_enquete = db.Column(db.DateTime(),default = datetime.datetime.now())
    
    usuario_enquete = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable = False)
    Respostas = db.relationship('Resposta_Enquete', backref='enquete')