from tablero import app
from tablero.controllers import controlers

(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

if __name__ == '__main__':
    app.run(debug= True)