from flask import Flask
from flask_cors import CORS

def create_app():  ## Application Factory (Uygulama Fabrikası) kalıbı.
    try:
        app = Flask(__name__)  ## Flask uygulamasını başlatıyoruz
        
        # Tüm uygulama için CORS'u aktif et
        CORS(app)
        
        # routes.py içinde hazırladığımız Blueprint'i ana uygulamaya kaydediyoruz
        from app.routes import bp
        app.register_blueprint(bp)
        
        return app

    except Exception as e:  ## Hata Yakalama
        print(f"KRİTİK HATA (App Factory): {e}")
        raise e





    