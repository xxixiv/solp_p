from flask import Flask

from config import Config
from extensions import cors, limiter, db, migrate
from flask_migrate import Migrate
from models import Card

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
cors.init_app(app)
limiter.init_app(app)
db.init_app(app)
migrate.init_app(app, db)


@app.cli.command("seed-cards")
def seed_cards():
    cards = [
        Card(
            title='C#',
            subtitle='C# Programming Language',
            image='/c#.png',
            icon='mdi-language-c#',
            text='Learn now',
            description='hi im just here shaaaaaaa'
        ),
        Card(
            title='C++',
            subtitle='C++ Programming Language',
            image='/c++.png',
            icon='mdi-language-c',
            text='Learn now',
            description='hi im just here shaaaaaa'
        ),

        Card(
            title='PHP',
            subtitle='PHP Programming Language',
            image='/php.png',
            icon='mdi-language-c',
            text='Learn now',
            description='hi im just here shaaaa'
        )
    ]

    for card in cards:
        db.session.add(card)
    db.session.commit()
    print("Cards seeded successfully!")


def create_app():
    # register blueprints
    from routes.execute   import execute_bp
    from routes.languages import languages_bp
    # from routes.snippets  import snippets_bp
    from routes.health    import health_bp

    from routes.cards import cards_bp

    # ... other blueprints ...
    app.register_blueprint(cards_bp, url_prefix='/api')
    app.register_blueprint(execute_bp,   url_prefix='/execute')
    app.register_blueprint(languages_bp, url_prefix='/languages')
    # app.register_blueprint(snippets_bp,  url_prefix='/snippets')
    app.register_blueprint(health_bp,    url_prefix='/health')



    return app

if __name__ == '__main__':
    create_app().run()
