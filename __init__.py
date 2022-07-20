from flask import Flask, render_template, redirect, request
from utilities import isURLValid, randomLinkCode
from db_sql import checkPass, matchPassword, pushToDatabase, searchInDatabase, getLink, submitProblem
import re
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'i-have-removed-the-key'


@app.route('/', methods=['GET', 'POST'])
def runHome():
    """
    If the request method is POST, then get the link code, original link and passcode from the form. If
    the original link is empty, then return the home page with a message. If the original link is not a
    valid URL, then return the home page with a message. If the link code is already in the database,
    then generate a new link code. If the original link starts with https:// or http://, then push the
    link code, passcode and original link to the database. Otherwise, push the link code, passcode and
    the original link with https:// prepended to the database. Then return the home page with the link
    code and a message.
    :return: the rendered template.
    """
    if request.method == "POST":
        link_code = randomLinkCode()
        original_link = request.form.get("oglink")
        passcode = request.form.get("password-here")

        if len(original_link) <= 0:
            return render_template('home.html',push_msg="Put a link !!",push_link='Put a link !!')

        elif isURLValid(original_link) == False:
            return render_template('home.html',push_msg="Invalid URL", push_link='Invalid URL')

        if searchInDatabase(link_code) == True:
            link_code = randomLinkCode()

        if re.search("^https://", original_link) or re.search("^http://", original_link):
            pushToDatabase(link_code, passcode, original_link)
        else:
            pushToDatabase(link_code, passcode, f"https://{original_link}")

        push_link = f'superurl.pythonanywhere.com/{link_code}'

        return render_template('home.html', push_link=push_link,)

    return render_template('home.html',push_msg="Paste link", push_link='Generate a link !')


@app.route('/<link_code>', methods=['GET', 'POST'])
def redirectToOriginalLink(link_code):
    passcode = request.form.get("passcode")
    """
    If the link_code is in the database, then check if it has a password. If it does, then check if the
    password is correct. If it is, then redirect to the original link. If it isn't, then render the
    auth_redirect.html template with the message "Incorrect password !!!" If the link_code doesn't have
    a password, then redirect to the original link. If the link_code isn't in the database, then render
    the not_found.html template.
    
    :param link_code: The code that the user will enter in the browser to access the link
    :return: the link to the original link.
    """
    if searchInDatabase(link_code) == True:
            if checkPass(link_code) == True:
                if request.method == "POST":
                    if len(passcode) <= 0:
                        return render_template('auth_redirect.html', input_message="Please input password !!!")
                    elif matchPassword(link_code, passcode) == True:
                        return redirect(getLink(link_code))
                    return render_template('auth_redirect.html', input_message="Incorrect password !!!")
                return render_template('auth_redirect.html', input_message="Enter secret password")
            else:
                return redirect(getLink(link_code))
    else:
        return render_template('not_found.html')


@app.route('/report-a-problem', methods=['GET', 'POST'])
def redirectToReportPage():
    """
    If the request method is POST, then get the problem from the form and submit it. 
    If the request method is not POST, then render the report_a_problem.html page.
    :return: the rendered template.
    """
    if request.method == "POST":
        problem = request.form.get("msg-box")
        submitProblem(problem)
    return render_template('report_a_problem.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
