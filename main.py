from flask import Flask, jsonify, request

# Vamos a decir que flask es nustro servidor de nuestra aplicacion
app = Flask(__name__)

# En este caso uso HTTP
@app.route('/')
def root():
    return "Root"

'''
Podemos tener los endpoints con diferentes metodos que se manejan con ç
HTTP que es el protocolo que se utiliza para transmitir informacion a traves de internet. 
Los motodos son:
- GET --> obtener informacion  (normalmente de una BD)
- POST --> me permite crear o guardar informacion
- PUT --> actualizo Informacion
- DELETE --> borrar informacion
'''
# Esto es para pasar parametros
@app.route('/users/<user_id>')
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "9999-222-21"}
    # /users/2654?query=query_test
    # query es un parametro al igual que user_id
    query= request.args.get('query')
    if query:
        user["query"]=query 
    return jsonify(user), 200

@app.route('/users', methods=['POST'])

7:13
if __name__=="__main__":
    app.run(debug=True)