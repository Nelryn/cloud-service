import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3.upload_fileobj(file, 'my-cloud-service-bucket', file.filename)
    return jsonify({'message': 'File uploaded successfully'})


@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    table.put_item(Item=data)
    return jsonify({'message': 'Item added successfully'})


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to my cloud service!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

