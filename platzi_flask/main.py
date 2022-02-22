'''1) importancion de la clase Flask '''
from flask import Flask, request

'''2) crear una instancia de Flask:
    se crea una variable app y se
    llama a la clasde Flask que por
    parametro tiene el nombre de la
    aplicacion que en este caso es
    el nombre del archivo (main.py)
    indicado por __name__
'''
app = Flask(__name__)

'''4) con el decorador @app.route()
que recibe como parametro la ruta en
donde se va correr esta funcion'''
@app.route('/')
def hello():
    '''3) se crea la funcion que esn este
    caso mostrara un saludo'''
    '''para conocer la direccion ip del
    usuario se puede usar request.remote_addr'''
    user_ip = request.remote_addr
    return f'Hello World, tu IP es{user_ip}'


'''Otra forma poner el modo debuggin en flask
es enviando por prametro debug = True, tambien
se puede enviar otros parametros'''
if __name__ == '__main__':
    app.run(port = 5000, debug = True)

