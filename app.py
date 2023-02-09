#pip install mysql-connector-python
#pip install flask
#pip install myapp

import psycopg2
from datetime import datetime
from flask import Flask, make_response, jsonify, request



#conexão com banco de dados
mydb = psycopg2.connect(
    host="dpg-cfhijh1gp3jh03ldkarg-a.oregon-postgres.render.com",
    database="api_teste_28pt",
    user="api_teste_28pt_user",
    password="GPMAU8oCSb9xa4J0kHnkmb0OSUdneMzY"
)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    return "API funcionando!"

@app.route('/geracao', methods=['GET'])
def geracao():

    sql_1 = f"SELECT dataHora, usinaUhe, numUg1, ug1 FROM UHE1 WHERE dataHora BETWEEN '2023-01-01 00:00:00' AND '2023-01-01 03:00:00'"
    sql_2 = f"SELECT dataHora, usinaUhe, numUg2, ug2 FROM UHE1 WHERE dataHora BETWEEN '2023-01-01 00:00:00' AND '2023-01-01 03:00:00'"

    my_cursor = mydb.cursor()
    my_cursor.execute(sql_1)
    scl1 = my_cursor.fetchall()


    ug1 = list()
    for usina in scl1:


        ug1.append(
                    {
                        "data": usina[0],
                        "usina": usina[1],
                        "ug": usina[2],
                        "valor": usina[3]
                    }        
                    )


    my_cursor = mydb.cursor()
    my_cursor.execute(sql_2)
    scl2 = my_cursor.fetchall()

    print (scl2)

    ug2 = list()
    for usina2 in scl2:
        ug2.append(
                    {
                    
                    "data": usina2[0],    
                    "usina": usina2[1],
                    "ug": usina2[2],
                    "valor": usina2[3]
                    }        
                    )

    return make_response(
        jsonify(
                ug1,
                ug2
                )

    )





app.run(host='0.0.0.0', port=5000)
