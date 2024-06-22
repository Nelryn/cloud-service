import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

s3 = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3.upload_fileobj(file, 'my-cloud-service-bucket', file.filename)
    return jsonify({'message': 'File uploaded successfully'})

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to my cloud service!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

