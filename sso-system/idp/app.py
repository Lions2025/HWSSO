from flask import Flask, request, redirect, render_template, jsonify
from utils.jwt_utils import create_jwt, verify_jwt
import urllib.parse
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 模拟用户数据库
USERS = {
    "admin": {"password": "admin123", "email": "admin@example.com"},
    "user1": {"password": "pass123", "email": "user1@example.com"}
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        client_id = request.args.get('client_id')
        redirect_uri = request.args.get('redirect_uri')
        
        if username in USERS and USERS[username]['password'] == password:
            # 生成JWT
            token = create_jwt({
                "sub": username,
                "email": USERS[username]['email'],
                "client_id": client_id
            })
            
            # 构建重定向URL
            redirect_url = f"{redirect_uri}?token={urllib.parse.quote(token)}"
            return redirect(redirect_url)
            
        return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route('/.well-known/openid-configuration')
def discovery_endpoint():
    return jsonify({
        "issuer": "http://idp:5000",
        "authorization_endpoint": "http://idp:5000/login",
        "token_endpoint": "http://idp:5000/token",
        "userinfo_endpoint": "http://idp:5000/userinfo"
    })

@app.route('/userinfo')
def user_info():
    token = request.args.get('token')
    payload = verify_jwt(token)
    if payload:
        return jsonify({
            "sub": payload['sub'],
            "email": payload['email']
        })
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
