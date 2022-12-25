if __name__ == "__main__":
    from logging import DEBUG, basicConfig
    from secrets import token_urlsafe
    from flask import Flask
    from pages import app
    from os import getcwd

    WEBSITE = 'fini8'

    root = Flask(__name__)
    root.config["SECRET_KEY"] = token_urlsafe(16)
    root.register_blueprint(app, url_prefix="/")

    basicConfig(filename=f"{getcwd()}\\{WEBSITE}.log", level=DEBUG)

    root.run(host="127.0.0.1")