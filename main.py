from flask import Flask
from flask_restful import Api, Resource, reqparse

import databases.MongoDB as mongodb

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class FindOne(Resource):
    @staticmethod
    def post():
        parser.add_argument('database', type=str, location='form')
        parser.add_argument('database-name', type=str, location='form')
        parser.add_argument("mongo-collection", type=str, location='form')
        parser.add_argument('mongo-filter', type=str, location='form')
        args = parser.parse_args()

        database_arguments = {
            "database_arg": args.get("database"),
            "database_name_arg": args.get("database-name"),
            "mongo_collection_arg": args.get("mongo-collection"),
            "mongo_filter_arg": args.get("mongo-filter")
        }

        for key, value in database_arguments.items():
            if value == "None":
                return "POST parameter " + key + " is missing"

        if database_arguments["database_arg"] == "mongodb":
            result = mongodb.find_one_in_collection(
                database_arguments["database_name_arg"],
                database_arguments["mongo_collection_arg"],
                database_arguments["mongo_filter_arg"]
            )
            return "{'result':"+str(result)+"}"
        else:
            return "{'result':'database not recognized'}"


class FindAll(Resource):
    @staticmethod
    def post():
        parser.add_argument('database', type=str, location='form')
        parser.add_argument('database-name', type=str, location='form')
        parser.add_argument('mongo-collection', type=str, location='form')
        parser.add_argument('mongo-filter', type=str, location='form')
        args = parser.parse_args()

        database_arguments = {
            "database_arg": args.get("database"),
            "database_name_arg": args.get("database-name"),
            "mongo_collection_arg": args.get("mongo-collection"),
            "mongo_filter_arg": args.get("mongo-filter")
        }

        for key, value in database_arguments.items():
            if value == "None":
                return "POST parameter " + key + " is missing"

        if database_arguments["database_arg"] == "mongodb":
            result = mongodb.find_one_in_collection(
                database_arguments["database_name_arg"],
                database_arguments["mongo_collection_arg"],
                database_arguments["mongo_filter_arg"]
            )
            return "{'result':" + str(result) + "}"
        else:
            return "{'result':'database not recognized'}"


class Append(Resource):
    @staticmethod
    def post():
        parser.add_argument('database', type=str, location='form')
        parser.add_argument('database-name', type=str, location='form')
        parser.add_argument('mongo-collection', type=str, location='form')
        parser.add_argument('mongo-document', type=str, location='form')
        args = parser.parse_args()

        database_arguments = {
            "database_arg": args.get("database"),
            "database_name_arg": args.get("database-name"),
            "mongo_collection_arg": args.get("mongo-collection"),
            "mongo_document_arg": args.get("mongo-document")
        }

        for key, value in database_arguments.items():
            if value == "None":
                return "POST parameter " + key + " is missing"

        if database_arguments["database_arg"] == "mongodb":
            result = mongodb.append_to_collection(
                database_arguments["database_name_arg"],
                database_arguments["mongo_collection_arg"],
                database_arguments["mongo_document_arg"]
            )
            return "{'result':" + str(result) + "}"
        else:
            return "{'result':'database not recognized'}"


class Update(Resource):
    @staticmethod
    def post():
        parser.add_argument('database', type=str, location='form')
        parser.add_argument('database-name', type=str, location='form')
        parser.add_argument('mongo-collection', type=str, location='form')
        parser.add_argument('mongo-filter', type=str, location='form')
        parser.add_argument('mongo-set-values', type=str, location='form')
        args = parser.parse_args()

        database_arguments = {
            "database_arg": args.get("database"),
            "database_name_arg": args.get("database-name"),
            "mongo_collection_arg": args.get("mongo-collection"),
            "mongo_filter_arg": args.get("mongo-filter"),
            "mongo_set_values_arg": args.get("mongo-set-values")
        }

        for key, value in database_arguments.items():
            if value == "None":
                return "POST parameter " + key + " is missing"

        if database_arguments["database_arg"] == "mongodb":
            result = mongodb.update_item_in_collection(
                database_arguments["database_name_arg"],
                database_arguments["mongo_collection_arg"],
                database_arguments["mongo_filter_arg"],
                database_arguments["mongo_set_values_arg"]
            )
            return "{'result':" + str(result) + "}"
        else:
            return "{'result':'database not recognized'}"


class Delete(Resource):
    @staticmethod
    def post():
        parser.add_argument('filter', type=str, location='form')
        args = parser.parse_args()
        print(args)
        return {"osef": "3000"}


api.add_resource(FindOne, '/findone')
api.add_resource(FindAll, '/findall')
api.add_resource(Append, '/append')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')


@app.route('/welcome')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
