from ..extensions import db
import datetime

class Resposta_Enquete(db.Model):
    
    __tablename__ = 'resposta_enquete'
    
    id_resposta_enquete = db.Column(db.Integer,primary_key = True)
    resposta = db.Column(db.String(200),nullable = False)
    
    enquete_resposta = db.Column(db.Integer, db.ForeignKey('enquete.id_enquete'), nullable = False)
    usuario_resposta = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable = False)