# More about Dynamic Url
# The default variable type is string...you can change the data type to int, float and path...ex: <int:variable-name>
# You can also use two or more route decorators to run more functions on different web addresses.
# Note that using while using the parameters of route decorator it is preferred to use "/" at the end. Take an example of @app.route("/abc") and @app.route("/abc/")... In both the cases, if you enter /abc at the end of the url, you will get the same output but if you enter /abc/, you will get output only for the second case.
from flask import Flask
app=Flask(__name__)

@app.route("/a/<int:phone>/")
def func(phone):
    return f"Your Phone number is {phone}"
@app.route("/b/<float:var>/") # Note that if you entered the address in the wrong data type then you will get an error.
def func2(var):
    return f"You have entered: {var}"

if __name__=="__main__":
    app.run()