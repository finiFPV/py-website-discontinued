if __name__ == '__main__':
    from flask import Flask
    from pages import app

    root = Flask(__name__)
    root.register_blueprint(app, url_prefix='/')
    root.run(host='0.0.0.0')