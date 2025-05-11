from flask_cors import CORS
from flask_limiter import Limiter
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

cors  = CORS()
limiter = Limiter(key_func=lambda: 'global')
db    = SQLAlchemy()
migrate = Migrate()
