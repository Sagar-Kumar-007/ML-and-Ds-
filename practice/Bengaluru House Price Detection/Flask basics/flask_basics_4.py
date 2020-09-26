# The url_for() function is very useful for dynamically building a URL for a specific function. The function accepts
# the name of a function as first argument, and one or more keyword arguments, each corresponding to the variable
# part of URL.


from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route("/admin/")
def func():
    return "Hello Admin"


@app.route("/guest/<name>/")
def func2(name):
    return f"Hello {name} as Guest"


@app.route("/user/<var>/")
def func3(var):
    if var == "admin":
        return redirect(url_for('func'))             # Redirect Function is used to redirect something and url_for()
        # specifies the url to be redirected. Note that the function should be entered as a string.
    else:
        return redirect(url_for('func2', name=var))


if __name__ == "__main__":
    app.run()
