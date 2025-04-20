from flask import Flask, request, render_template, redirect
from shared.middleware.auth import authenticate
import urllib.parse
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

SP_CONFIG = {
    "client_id": "sp-client-001",
    "redirect_uri": "http://sp:5001/callback"
}

@app.route('/')
def index():
    token = request.args.get('token')
    if not token:
        # 构建授权URL
        auth_url = f"http://idp:5000/login?client_id={SP_CONFIG['client_id']}"
        auth_url += f"&redirect_uri={urllib.parse.quote(SP_CONFIG['redirect_uri'])}"
        return redirect(auth_url)
    
    # 验证令牌
    user = authenticate(token)
    if user:
        return render_template('index.html', user=user)
    
    return "Invalid authentication", 401

@app.route('/callback')
def callback():
    token = request.args.get('token')
    return redirect(f"/?token={token}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
