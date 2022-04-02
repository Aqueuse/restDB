from flask import Flask, render_template, request

import databases.MongoDB as mongodb
from security.security import is_authorized

app = Flask(__name__)


@app.route('/findone', methods=['POST'])
def findone():
    if not is_authorized(request.remote_addr):
        return "Null"

    database_arguments = {
        "database": request.form['database'],
        "database-name": request.form['database-name'],
        "mongo-collection": request.form['mongo-collection'],
        "mongo-filter": request.form['mongo-filter']
    }

    for key, value in database_arguments.items():
        if value == "None":
            return "POST parameter " + key + " is missing"

    if database_arguments["database"] == "mongodb":
        result = mongodb.find_one_in_collection(
            database_arguments["database-name"],
            database_arguments["mongo-collection"],
            database_arguments["mongo-filter"]
        )
        return "{'result':"+str(result)+"}"
    else:
        return "{'result':'database not recognized'}"


@app.route('/findall', methods=['POST'])
def findall():
    if not is_authorized(request.remote_addr):
        return "Null"

    database_arguments = {
        "database": request.form['database'],
        "database-name": request.form['database-name'],
        "mongo-collection": request.form['mongo-collection'],
        "mongo-filter": request.form['mongo-filter']
    }

    for key, value in database_arguments.items():
        if value == "None":
            return "POST parameter " + key + " is missing"

    if database_arguments["database"] == "mongodb":
        result = mongodb.find_all_in_collection(
            database_arguments["database-name"],
            database_arguments["mongo-collection"],
            database_arguments["mongo-filter"]
        )
        return "{'result':"+str(result)+"}"
    else:
        return "{'result':'database not recognized'}"


@app.route('/append', methods=['POST'])
def append():
    if not is_authorized(request.remote_addr):
        return "Null"

    database_arguments = {
        "database": request.form['database'],
        "database-name": request.form['database-name'],
        "mongo-collection": request.form['mongo-collection'],
        "mongo-document": request.form['mongo-document']
    }

    for key, value in database_arguments.items():
        if value == "None":
            return "POST parameter " + key + " is missing"

    if database_arguments["database"] == "mongodb":
        result = mongodb.append_to_collection(
            database_arguments["database-name"],
            database_arguments["mongo-collection"],
            database_arguments["mongo-document"]
        )
        return "{'result':"+str(result)+"}"
    else:
        return "{'result':'database not recognized'}"


@app.route('/update', methods=['POST'])
def update():
    if not is_authorized(request.remote_addr):
        return "Null"

    database_arguments = {
        "database": request.form['database'],
        "database-name": request.form['database-name'],
        "mongo-collection": request.form['mongo-collection'],
        "mongo-filter": request.form['mongo-filter'],
        "mongo-set-values": request.form['mongo-set-values']
    }

    for key, value in database_arguments.items():
        if value == "None":
            return "POST parameter " + key + " is missing"

    if database_arguments["database"] == "mongodb":
        result = mongodb.update_item_in_collection(
            database_arguments["database-name"],
            database_arguments["mongo-collection"],
            database_arguments["mongo-filter"],
            database_arguments["mongo-set-values"]
        )
        return "{'result':"+str(result)+"}"
    else:
        return "{'result':'database not recognized'}"


@app.route('/delete', methods=['POST'])
def delete():
    if not is_authorized(request.remote_addr):
        return "Null"

    database_arguments = {
        "database": request.form['database'],
        "database-name": request.form['database-name'],
        "mongo-collection": request.form['mongo-collection'],
        "mongo-filter": request.form['mongo-filter']
    }

    for key, value in database_arguments.items():
        if value == "None":
            return "POST parameter " + key + " is missing"

    if database_arguments["database"] == "mongodb":
        result = mongodb.delete_item_in_collection(
            database_arguments["database-name"],
            database_arguments["mongo-collection"],
            database_arguments["mongo-filter"]
        )
        return "{'result':" + str(result) + "}"
    else:
        return "{'result':'database not recognized'}"


@app.route('/welcome', methods=['GET'])
def welcome():
    if not is_authorized(request.remote_addr):
        return "Null"
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(debug=True)
