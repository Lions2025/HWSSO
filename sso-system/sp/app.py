from flask import Flask, request, redirect, render_template
from shared.jwt_utils import verify_jwt

app = Flask(__name__)
SP_CLIENT_ID = "your-sp-client-id"

@app.route('/')
def index():
    token = request.args.get('token')
    if not token:
        # 重定向到 IdP 登录
        idp_url = "http://localhost:5000/login"
        redirect_uri = urllib.parse.quote("http://localhost:5001/")
        return redirect(f"{idp_url}?client_id={SP_CLIENT_ID}&redirect_uri={redirect_uri}")
    
    # 验证令牌
    payload = verify_jwt(token, SP_CLIENT_ID)
    if payload:
        return render_template('index.html', user=payload['sub'])
    else:
        return "Invalid token", 401

if __name__ == '__main__':
    app.run(port=5001)
