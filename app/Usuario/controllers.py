from ..extensions import Blueprint, request, jsonify, db
from .model import Usuario

usuario_api = Blueprint('usuario_api', __name__)

@usuario_api.route("/usuarios",methods = ['GET','POST'])
def index():
    
    if request.method == 'GET':
        usuarios = Usuario.query.all()
        return jsonify([user.json() for user in usuarios])
    
    if request.method == 'POST':
        data = request.json
       
        nome = data.get('nome', None)
        senha = data.get('senha', None)
        telefone = data.get('telefone', None)
        email = data.get('email', None)
        
        if (nome is None):
            return {"error": "nome invalido ou ausente"}, 400
        if ( not(isinstance(nome,str))):
            return {"error": "tipagem errada"}, 400
        if (senha is None):
            return {"error": "senha invalida ou ausente"}, 400
        if ( not(isinstance(senha,str))):
            return {"error": "tipagem errada"}, 400
        if (telefone is None):
            return {"error": "telefone invalido ou ausente"}, 400
        if ( not(isinstance(telefone,str))):
            return {"error": "tipagem errada"}, 400
        if (email is None):
            return {"error": "email invalido ou ausente"}, 400
        if ( not(isinstance(email,str))):
            return {"error": "tipagem errada"}, 400

        if Usuario.query.filter_by(telefone=telefone).first():
            return {"error": "esse telefone já existe"},400

        usuario = Usuario(
            nome = nome,
            senha = senha,
            telefone = telefone,
            email = email
        )
        
        db.session.add(usuario)
        db.session.commit()

        return usuario.json(), 200
        

