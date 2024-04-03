from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

accounts = {
    '1': {
        'balance': 10.0
    },
    '2': {
        'balance': 30.0
    }
}

class Account(Resource):
  def get(self, account_id):
    if account_id not in accounts:
      return {'message': 'Account not found'}, 404
    return {'balance': accounts[account_id]['balance']}
  
  def post(self, account_id):
    parser = reqparse.RequestParser()
    parser.add_argument('deposit', type=float, required=True, help='Deposit amount must be a valid number')
    args = parser.parse_args();

    if account_id not in accounts:
      return {'error': 'Account not found'}, 404  
    
    accounts[account_id]['balance'] += args['deposit']
    return {'balance': accounts[account_id]['balance']}
  
api.add_resource(Account, '/<string:account_id>')

if __name__ == '__main__':
    app.run(debug=True)