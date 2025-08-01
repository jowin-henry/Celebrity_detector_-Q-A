# from flask import Flask
# from dotenv import load_dotenv
# import os

# def create_app():
#     load_dotenv()
#     template_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','templates'))

#     app = Flask(__name__ , template_folder=template_path)

#     app.secret_key = os.getenv("SECRET_KEY" , "default_secret")

#     from app.routes import main

#     app.register_blueprint(main)

#     return app

from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    template_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'templates')
    )

    app = Flask(__name__, template_folder=template_path)
    app.secret_key = os.getenv("SECRET_KEY", "default_secret")

    # ✅ Set max file size (e.g., 16 MB)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

    # ✅ Handle oversized file uploads gracefully
    @app.errorhandler(413)
    def too_large(e):
        return "Uploaded file is too large. Please upload an image under 16 MB.", 413

    # Register your routes blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
