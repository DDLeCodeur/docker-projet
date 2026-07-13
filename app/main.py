from fastapi import FastAPI
import pymysql

app = FastAPI()

@app.get("/")
def test_connexion():
    try:
        connexion = pymysql.connect(
            host="db_mysql", 
            user="root", 
            password="root"
        )
        return {"statut": "Ca marche bien ! Le serveur python discute avec MySQL."}
    except Exception as erreur:
        return {"statut": "Échec", "detail": str(erreur)}