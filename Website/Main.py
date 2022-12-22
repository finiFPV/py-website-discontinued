if __name__ == '__main__':
    from flask import Flask
    from pages import app
    from logging import DEBUG, basicConfig
    from secrets import token_urlsafe

    root = Flask(__name__)
    root.config['SECRET_KEY'] = token_urlsafe(16)
    root.register_blueprint(app, url_prefix='/')
    basicConfig(filename=f'logs.log', level=DEBUG)
    root.run(host='127.0.0.1', debug = True)