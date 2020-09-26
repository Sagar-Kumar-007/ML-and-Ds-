# Flask HTTP Methods: Http protocol is the foundation of data communication in world wide web. Different methods of
#                     data retrieval from specified URL are defined in this protocol.
# GET: Sends data in unencrypted form to the server. Most common method.
# HEAD: Same as GET, but without response body
# POST: Used to send HTML form data to server. Data received by POST method is not cached by server.
#       HTML forms:
#                   An HTML form is used to collect user input. The user input is most often sent to a server for processing.
#                   <form>:  The tag used in html is the <form> tag. The HTML <form> element is used to create an HTML form for user input.
#                            The <form> element is a container for different types of input elements, such as: text fields, checkboxes, radio buttons,
#                            submit buttons, etc.
#                   <input>: The <input type="text"> defines a single-line input field for text input. The value of type (text,radio,checkbox,submit,button) can be changed according to our requirements.
#                   <label>: The <label> tag defines a label for many form elements.
#                            The <label> element is useful for screen-reader users, because the screen-reader will read out loud the label when the user focus on the input element.
#                            The <label> element also help users who have difficulty clicking on very small regions (such as radio buttons or checkboxes) - because when the user clicks
#                            the text within the <label> element, it toggles the radio button/checkbox.
#                            The for attribute of the <label> tag should be equal to the id attribute of the <input> element to bind them together.
#                            While using input of type radio, make sure to assign the name attribute. For example, in the gender radio button, if you
#                            assign different names to all the inputs, you can select all the radio buttons, and if you have specified the same name for
#                            all the buttons (say gender), you will be able to select only one of the genders.
#                            The <input type="submit"> defines a button for submitting the form data to a form-handler.
#                            The form-handler is typically a file on the server with a script for processing input data.
#                            The form-handler is specified in the form's action attribute.
#                            The action attribute defines the action to be performed when the form is submitted.
#                            Usually, the form data is sent to a file on the server when the user clicks on the submit button.
#                            Syntax can be:
#                            <form action="/action.php">
#                              <label for="textbox">First Name</label>
#                              <input type='text' id="textbox" name="textbox"></input>
#                              <input type='radio' id="radio1" name="gender"></input><label for="radio1">Male</label>
#                              <input type='radio' id="radio2" name="gender"></input><label for="radio2">Female</label>
#                              <input type="submit" value="Submit">           # We use value attribute to assign the box with something initially.
#              Name Attribute: Notice that each input field must have a name attribute to be submitted.
#                              If the name attribute is omitted, the value of the input field will not be sent at all.


# To demonstrate the HTTP methods, we will first create a HTML form and then use the POST method to receive the information from the client to the server.
# Generally, flask uses GET method, so if the html document is not in forms then we will use the get method to receive the information.


from flask import Flask, url_for, redirect, request

app = Flask(__name__)


@app.route("/info/<name>/<sex>")
def info(name,sex):
    #return f"Hello {name}"
    return f"{name} is a {sex}"


@app.route("/login", methods=['POST', 'GET'])
def func():
    if request.method == 'POST':
        user = request.form['nm']
        sex = request.form['gender']
        return redirect(url_for('info', name=user,sex=sex))
    else:
        user = request.args.get('nm')
        sex = request.args.get('gender')
        return redirect(url_for('info', name=user,sex=sex))


if __name__ == "__main__":
    app.run(debug=True)
