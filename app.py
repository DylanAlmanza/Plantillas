from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave-secreta'

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario == 'admin' and contraseña == '123':
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Credenciales incorrectas.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/registro')
def registro():
    return "<h2>Página de registro (en construcción)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
