### Rappi Pay Challenge

### Software and Tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com)
4. [GitCLI](https://git-scm.com)

Create a new environment
'''
python -m venv venv
'''

pip install requirements.txt

run python app.py locally or go to the deployed version on Heroku: 

https://rappi-pay-challenge-nleal.herokuapp.com/

* Incovenientes:
- De primera instancia se trato de hacer una full app mas elaborada como se ve en el repo:

https://github.com/napoleonleal/RappiPayChallengeFail

pero al persisitir los errores y el tiempo corriendo decidi empezar de cero y hacer un proyecto mas sencillo y llamar la API

- Se utilizo One-Hot Encoding en lugar de LabelEncoder ya que es lo que tengo entendido que aumenta mas las metricas/performance de los modelos pero al momento de querer hacer predicciones en API no encontre manera de poder darle un Input parecido al del dataset original y poder hacer predicciones es por eso que la API recibe las columnas dummy de igual manera con 1/0

- Al hacer el One-Hot Encoding se elimino la primera 'dummy-variable' para evitar el 'dummy-variable trap' es por eso que la primera columna de cada variable que paso por el one-hot encoding hace falta al momento de hacer la peticion en la API

Columnas actuales del proyecto:
-Limite TC(0-99000)
-Tasa Interes TC(0-100)
-Monto de transaccion
-Hora de transaccion(0-23)
-is_prime(1,0)

** Al ser el genero Masculino la primera variable dummy de la columna genero original, se elimino, es por eso que para indicar que la transaccion fue hecha
** por un usuario de genero masculino se debe ingresar 0 tanto en 'Genero F' como en 'Genero Otro'

-Genero F(1,0)
-Genero Otro(1,0)

** Al ser la compra 'en abarrotes' la primera variable dummy de la columna establecimiento original, se elimino, es por eso que para indicar que la transaccion fue 
** hecha por un usuario en un abarrote se debe ingresar 0 en todas las demas opciones de compra.

-Compra en línea(1,0)
-Compra en Farmacia(1,0)
-Compra en Supermercado(1,0)
-Compra en Tienda departamental(1,0)
-Compra en lugar desconocido(1,0)

** Al ser la ciudad 'cancun' la primera variable dummy de la columna ciudad original, se elimino, es por eso que para indicar que la transaccion fue 
** hecha por un usuario en cancun se debe ingresar 0 en todas las demas opciones de ciudad.

-Ciudad de México(1,0)
-Guadalajara(1,0)
-Monterrey(1,0)
-Nezahualcóyotl(1,0)
-Tijuana(1,0)
-Toluca(1,0)

** Al ser el status_txn 'aceptado' la primera variable dummy de la columna status_txn original, se elimino, es por eso que para indicar que la transaccion fue 
** hecha por un usuario y fue aceptada se debe ingresar 0 en todas las demas opciones de txn.

-Txn En proceso(1,0)
-Txn_Rechazada(1,0)

** Al ser la marca 'apple' la primera variable dummy de la columna marca original, se elimino, es por eso que para indicar que la transaccion fue 
** hecha por un usuario con dispositivo apple se debe ingresar 0 en todas las demas opciones de marca.

-Marca Huawei(1,0)
-Marca Motorola(1,0)
-Marca Samsung(1,0)

** Al ser el proveedor 'ATT' la primera variable dummy de la columna proveedor original, se elimino, es por eso que para indicar que la transaccion fue 
** hecha por un usuario con proveedor 'ATT' se debe ingresar 0 en todas las demas opciones de Proveedor.

-Proveedor Movistar(1,0)
-Proveedor Telcel(1,0)

* Se que no es lo optimo, por eso entiendo si quedo descalificado del challenge pero aun si llegar asi me encantaria poder reunirme de igual forma para la presentacion y poder recibir feedback/consejos del equipo
