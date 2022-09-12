import json
from flask import Flask, request, app, jsonify, url_for, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
xgmodel = pickle.load(open('xgbmodel.pkl', 'rb'))

print(xgmodel.predict(pd.DataFrame([[87000, 61, 669.38, 8, False, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0]], columns=['linea_tc', 'interes_tc', 'monto', 'hora', 'is_prime', 'genero_M', 'genero_N', 'establecimiento_Compra en línea', 'establecimiento_Farmacia', 'establecimiento_Supermercado', 'establecimiento_Tienda departamental', 'establecimiento_Unknown', 'ciudad_Ciudad de México', 'ciudad_Guadalajara', 'ciudad_Monterrey', 'ciudad_Nezahualcóyotl', 'ciudad_Tijuana', 'ciudad_Toluca', 'status_txn_En proceso', 'status_txn_Rechazada', 'marca_Huawei', 'marca_Motorola', 'marca_Samsung', 'proveedor_Movistar', 'proveedor_Telcel'])))
