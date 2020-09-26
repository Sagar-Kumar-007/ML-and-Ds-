# Flask is a Web Application FrameWork
from flask import Flask   # We import Flask from flask
app=Flask(__name__)       # We call the Flask module to a variable...which we later route using the command @app.route("The word you want to enter after the address")
                          # The Parameter we give to Flask() is the name of the module. Since, we want the flask server to run from this file, we give it __name__ else it would be the name of the file.
@app.route("/")
def func():               # We define a function which should run when we open the page.
    return "Hello World"
if __name__=="__main__":  # This is used to ensure that we are running the program from this file and not the module (flask in this case)...for more info visit Geeks for Geeks
    app.run()