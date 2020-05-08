# Register

Este desarrollo es realizado para sistemas distribuidos, queremos dar a conocer el funcionamiento de register a traves del lenguaje de programacion Python y como editor de texto Eclipse acompañado del complemento pyDev, el cual nos permite la refactorización de código, la depuración gráfica y el análisis de código.

Ahora bien, ¿Cual es la finalidad del proyecto? Register forma parte de una de las tecnologias de criptomonedas completamente digitales peer to peer, como Bitcoin, este sistema distribuido almacena informacion ahora conocido como blockchain.

Blockchain puede almacenar cualquier tipo de informacion en forma de bloques que están encadenados usando hashes. De aquí el nombre "blockchain" (block = bloque, chain = cadena, "cadena de bloques").


# ¿Qué es "Register"?🚀

El objetivo de register es detectar cualquier tipo de manipulacion en la informacion almacenada usando hash, esta funcion toma informacion de cualquier tamaño y a partir de ella se produce otra informacion de tamaño fijo, que generalmente sirve para identificar la entrada.

Podemos definir que Register es como un router, debido a que su funcion es recibir datos de tipo hash y los envia al bloque correspondiente,para este caso tenemos un bloque o componente llamado Coordinador el cual realiza el envio de dos direcciones debidamente codificadas con el algoritmo SHA256,a este proceso se le conoce como transacciones no confirmadas, una vez coordinador realiza el envio de la transacccion no confirmada, register realiza una peticion de tipo POST a un nodo conectado para añadir la transacción al conjunto de transacciones sin confirmar retornando a Coordinador un tipo de dato booleano y de esta manera continue verificando sus reglas internas.

# Pre-requisitos 📋

Para el desarrollo de la aplicación se debe instalado:

- Eclipse.
- Python.

Luego realizar los siguientes pasos:

- Añadir Python a las variables de entorno.
- Añadir la librería JSON (import json), empleada para manipular las etiquetas y valores del JSON recibido.
- Desde línea de comando añadir la librería web.py (import web) permite entre una de sus muchas funciones publicar y dejar a la escucha la aplicación en el puerto indicado.

# Instalación 🔧

Tener instalado el complemento pyDev que permite usar Eclipse como IDE de Python.

Tambien se debe instalar web.py revisar el siguiente link:

	hhttps://webpy.org/
    
Luego Clonar el proyecto

	git clone https://github.com/jhonnyrod/sisdistribuidos

# Codigo ⚙️

!/usr/bin/env python
import web
import json
from collections import Counter

urls = (
    '/index/', 'index'
)

class index:
    def POST(self):
        # How to obtain the name key and then print the value?
        web.header('Content-Type', 'application/json')
        data = web.data()
        my_json = data.decode('utf8').replace("'", '"')
        res=json.loads(my_json)
        print(Counter(res["direccion1"]))
        if (res["direccion1"].isalnum() and res["direccion2"].isalnum() and (len(res["direccion1"]) == 64) and (len(res["direccion2"]) == 64)):
            comp=True
        else:
            comp=False
        resp= json.dumps({"direccion1":res["direccion1"], "direccion2": res["direccion2"],"monto":res["monto"], "comprobador":comp})      
        return resp

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


# Ejecutando las pruebas ⚙️
En primer lugar debe ejecutar el comando	

	Python3 init.py 8888, Ahora nuestra web estará escuchando peticiones en el puerto 8888, dirección
	http://142.44.246.23:8888/index/.


para probar su funcionamiento enviaremos la petición http utilizando POSTMAN, será de tipo POST y en el cuerpo de la se enviará un JSON compuesto por tres etiquetas:
    {
    "direccion1": "Cadena Hash compuesta por 64 caracteres entre letras y numeros",
    "direccion2": "Cadena Hash compuesta por 64 caracteres entre letras y numeros",
    "monto": Valor numerico
    }

Como respuesta a la petición el método retorna un nuevo JSON con compuesto por cuatro etiquetas, las tres recibidas anteriormente y una etiqueta más llamada "Comprobador"  la cual corresponde a un valor booleano el cual indica si los valores recibidos en el JSON inicial son correctos o no, es decir verifica que los valores de "direccion1",  "direccion2" y "monto" cumplan con las características especificadas en el JSON. Esta respuesta tiene el siguiente aspecto:
    {
    "direccion1": "Cadena Hash compuesta por 64 caracteres entre letras y numeros",
    "direccion2": "Cadena Hash compuesta por 64 caracteres entre letras y numeros",
    "monto": Valor numerico,
    "monto": "Verdadero o Falso segun corresponda",	
    }

# Vista previa ⌨️

https://github.com/jhonnyrod/sisdistribuidos/blob/master/Ejemplo%20Peticion.png

# Construido con 🛠️

- Eclipse - Framework de modelado
- POSTMAN - (Pruebas) Envío de peticiones HTTP REST
- Python3 - Lenguaje de Programacion


# Autores ✒️

- Diana León 
- Jonathan Rodriguez
- Jeisson Guauta

# Expresiones de Gratitud 🎁

