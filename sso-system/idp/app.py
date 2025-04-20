from flask import Flask, request, redirect, render_template, make_response
from shared.jwt_utils import create_jwt
import urllib.parse

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 实际应验证数据库中的用户凭证
        username = request.form['username']
        password = request.form['password']
        
        if username == "user" and password == "pass":
            # 生成 JWT
            client_id = request.args.get('client_id')
            redirect_uri = request.args.get('redirect_uri')
            token = create_jwt(username, client_id)
            
            # 构建重定向 URL
            redirect_url = f"{redirect_uri}?token={urllib.parse.quote(token)}"
            return redirect(redirect_url)
            
    return render_template('login.html')

@app.route('/userinfo')
def user_info():
    token = request.args.get('token')
    # 这里应添加完整的令牌验证逻辑
    return {'user': 'demo_user', 'email': 'user@example.com'}
