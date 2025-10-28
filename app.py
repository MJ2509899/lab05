from flask import Flask, render_template, request, redirect, url_for

# 👇 Tell Flask to look for HTML files in the "src" folder
app = Flask(__name__, template_folder='src', static_folder='static')

# In-memory list to store user data
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/table')
def table():
    return render_template('table.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')

        users.append({'name': name, 'email': email, 'age': age})
        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
