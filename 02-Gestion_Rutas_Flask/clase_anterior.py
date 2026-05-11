from flask import Flask, jsonify

app = Flask(_name_)

tareas = [
    {'id': 1, 'tarea':'Estudiar Flask'},
    {'id': 2, 'tarea':'Desarrollar una API'},
    {'id': 3, 'tarea':'Crear una aplicación web'}
]

@app.route('/')
def index():
    return '<h1>Hola desde Flask</h1>'

@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h1>'

@app.route('/servicios')
def servicios():
    return '<h1>Servicios</h1>'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'<h1>Hola, {nombre}!</h1>'

@app.route('/producto/<categoria>/<producto>')
def producto(categoria, producto):
    return f'<h1>Producto: {producto}</h1><p>Categoría: {categoria}</p>'

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    resultado = num1 + num2
    return f'<h1>Suma: {resultado}</h1>'

@app.route('/api/tareas')
def obtener_tareas():
    return jsonify(tareas)

if _name_ == '_main_':
    app.run(debug=True)