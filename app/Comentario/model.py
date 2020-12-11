from ..extensions import db
import datetime

class Comentario(db.Model):
    
    __tablename__ = 'comentario'
    
    id_comentario = db.Column(db.Integer,primary_key = True)
    
    curtida = db.Column(db.Boolean,nullable = False) 
    texto = db.Column(db.String(200),default = "")        
    data_comentario = db.Column(db.DateTime(),default = datetime.datetime.now())
    
    usuario_comentario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable = False)
    usuario_post = db.Column(db.Integer, db.ForeignKey('post.id_post'), nullable = False)

