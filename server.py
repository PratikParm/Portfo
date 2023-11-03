from flask import Flask, render_template, request, jsonify
from passwordchecker import pwned_api_check
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check_password',methods=['POST','GET'])
def html_page():
    return render_template('passwordchkr.html')


@app.route('/submit_password', methods=['POST','GET'])
def check_password():
    password = request.json.get('password')
    count = pwned_api_check(password)

    if count:
        return jsonify({'message': f'The password was found {count} times. You should change your password!!'})
    else:
        return jsonify({'message': f'The password was not found. You can use this password!'})


if __name__ == '__main__':
    app.run()
