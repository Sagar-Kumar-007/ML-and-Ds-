from flask import Flask

app = Flask(__name__)


@app.route("/<var>")  # You can also create a dynamic url using <variable-name> in the route decorator.
def func(var):
    return f"Hello {var}"  # Now entering the url as 127.0.0.1:5000/something would give you the output as Hello something


if __name__ == "__main__":
    app.run()
