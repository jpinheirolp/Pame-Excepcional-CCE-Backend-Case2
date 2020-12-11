from flask import Flask
from .config import Config
from .extensions import db, migrate
from .Comentario.model import Comentario
from .Enquete.model import Enquete
from .Post.model import Post
from .Resposta_Enquete.model import Resposta_Enquete
from .Usuario.model import Usuario

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app)

    return app