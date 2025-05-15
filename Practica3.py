from flask import Flask, request, jsonify
import json

# https://github.com/Juan-Sebastian-Marin-Salazar/U4Practica3/blob/main/Practica3.py

app = Flask(__name__)

# Funciones de la tarea
def agregar_diccionario(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

def eliminar_diccionario(diccionario, clave):
    diccionario.pop(clave, None)
    return diccionario

def modificar_diccionario(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    return False

def combinar_diccionarios(dic1, dic2):
    return {**dic1, **dic2}

def agregar_conjunto(conjunto, elemento):
    if elemento in conjunto:
        return False
    conjunto.add(elemento)
    return True

def eliminar_conjunto(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    return False

def combinar_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def agregar_tupla(tupla, elemento):
    return tupla + (elemento,)

def eliminar_tupla(tupla, elemento):
    return tuple(x for x in tupla if x != elemento)

def concatenar_tuplas(tupla1, tupla2):
    return tupla1 + tupla2

def revertir_tupla(tupla):
    return tupla[::-1]

def imprimir_diccionario(diccionario):
    return diccionario

def imprimir_tupla(tupla):
    return tupla

def imprimir_conjunto(conjunto):
    return list(conjunto)  # jsonify no admite sets

# RUTAS FLASK

@app.route('/agregar_diccionario')
def ruta_agregar_diccionario():
    dic = json.loads(request.args.get('dic'))
    clave = request.args.get('clave')
    valor = request.args.get('valor')
    return jsonify(agregar_diccionario(dic, clave, valor))

@app.route('/eliminar_diccionario')
def ruta_eliminar_diccionario():
    dic = json.loads(request.args.get('dic'))
    clave = request.args.get('clave')
    return jsonify(eliminar_diccionario(dic, clave))

@app.route('/modificar_diccionario')
def ruta_modificar_diccionario():
    dic = json.loads(request.args.get('dic'))
    clave = request.args.get('clave')
    nuevo_valor = request.args.get('valor')
    return jsonify(modificar_diccionario(dic, clave, nuevo_valor))

@app.route('/combinar_diccionarios')
def ruta_combinar_diccionarios():
    dic1 = json.loads(request.args.get('dic1'))
    dic2 = json.loads(request.args.get('dic2'))
    return jsonify(combinar_diccionarios(dic1, dic2))

@app.route('/agregar_conjunto')
def ruta_agregar_conjunto():
    conjunto = set(json.loads(request.args.get('conjunto')))
    elemento = request.args.get('elemento')
    resultado = agregar_conjunto(conjunto, elemento)
    return jsonify({"resultado": resultado, "conjunto": list(conjunto)})

@app.route('/eliminar_conjunto')
def ruta_eliminar_conjunto():
    conjunto = set(json.loads(request.args.get('conjunto')))
    elemento = request.args.get('elemento')
    resultado = eliminar_conjunto(conjunto, elemento)
    return jsonify({"resultado": resultado, "conjunto": list(conjunto)})

@app.route('/combinar_conjuntos')
def ruta_combinar_conjuntos():
    conjunto1 = set(json.loads(request.args.get('conj1')))
    conjunto2 = set(json.loads(request.args.get('conj2')))
    return jsonify(list(combinar_conjuntos(conjunto1, conjunto2)))

@app.route('/diferencia_conjuntos')
def ruta_diferencia_conjuntos():
    conjunto1 = set(json.loads(request.args.get('conj1')))
    conjunto2 = set(json.loads(request.args.get('conj2')))
    return jsonify(list(diferencia_conjuntos(conjunto1, conjunto2)))

@app.route('/agregar_tupla')
def ruta_agregar_tupla():
    tupla = tuple(json.loads(request.args.get('tupla')))
    elemento = request.args.get('elemento')
    return jsonify(agregar_tupla(tupla, elemento))

@app.route('/eliminar_tupla')
def ruta_eliminar_tupla():
    tupla = tuple(json.loads(request.args.get('tupla')))
    elemento = request.args.get('elemento')
    return jsonify(eliminar_tupla(tupla, elemento))

@app.route('/concatenar_tuplas')
def ruta_concatenar_tuplas():
    tupla1 = tuple(json.loads(request.args.get('tupla1')))
    tupla2 = tuple(json.loads(request.args.get('tupla2')))
    return jsonify(concatenar_tuplas(tupla1, tupla2))

@app.route('/revertir_tupla')
def ruta_revertir_tupla():
    tupla = tuple(json.loads(request.args.get('tupla')))
    return jsonify(revertir_tupla(tupla))

@app.route('/imprimir_diccionario')
def ruta_imprimir_diccionario():
    dic = json.loads(request.args.get('dic'))
    return jsonify(imprimir_diccionario(dic))

@app.route('/imprimir_tupla')
def ruta_imprimir_tupla():
    tupla = tuple(json.loads(request.args.get('tupla')))
    return jsonify(imprimir_tupla(tupla))

@app.route('/imprimir_conjunto')
def ruta_imprimir_conjunto():
    conjunto = set(json.loads(request.args.get('conjunto')))
    return jsonify(imprimir_conjunto(conjunto))

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
