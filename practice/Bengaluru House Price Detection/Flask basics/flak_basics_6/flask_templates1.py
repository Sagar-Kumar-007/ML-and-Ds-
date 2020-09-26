from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route("/info/<name>/<phone>")
def info(name, phone):
    # return f"{name}'s phone number is {phone}"
    return render_template('output.html', nm=name, no=phone)    # Flask will search for the html in templates folder (by default). So make sure to create a templates folder while using render_template


@app.route("/login", methods=['POST'])
def func():
    name1 = request.form['name']
    phone1 = request.form['phone']
    return redirect(url_for('info', name=name1, phone=phone1))


if __name__ == "__main__":
    app.run(debug=True)
