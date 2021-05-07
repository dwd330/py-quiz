from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


class qbank(Resource):
    def get(self):
        data = pd.read_csv('bank.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200
    
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('index', required=True)
        parser.add_argument('question', required=True)
        parser.add_argument('answer', required=True)
        parser.add_argument('mark', required=True)
        args = parser.parse_args()

        data = pd.read_csv('bank.csv')

        new_data = pd.DataFrame({
            'index'        : [args['index']],
            'question'     : [args['question']],
            'answer'       : [args['answer']],
            'mark'         : [args['mark']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('bank.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201



api.add_resource(qbank,'/api/qbank')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000,debug=True)
