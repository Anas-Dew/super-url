from flask import Flask, render_template, redirect, request
from utilities import isURLValid, randomLinkCode
# from db_mongo import pushToDatabase, searchInDatabase, getLink
from db_sql import checkPass, matchPassword, pushToDatabase, searchInDatabase, getLink, submitProblem
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def runHome():
    if request.method == "POST":
        link_code = randomLinkCode()
        original_link = request.form.get("og-link")
        passcode = request.form.get("password-here")

        if len(original_link) <= 0:
            return render_template('home.html', push_link='Put a link !!', abbr="Haha still you didn't generated any link, get one buddy!")

        elif isURLValid(original_link) == False:
            return render_template('home.html', push_link='Invalid URL', abbr="Haha still you didn't generated any link, get one buddy!")

        if searchInDatabase(link_code) == True:
            link_code = randomLinkCode()

        if re.search("^https://", original_link) or re.search("^http://", original_link):
            pushToDatabase(link_code, passcode, original_link)
        else:
            pushToDatabase(link_code, passcode, f"https://{original_link}")

        push_link = f'superurl.pythonanywhere.com/{link_code}'

        return render_template('home.html', push_link=push_link, abbr="GO TO YOUR LINK !")

    return render_template('home.html', push_link='Generate a link !', abbr="Haha you didn't generated any link, get one buddy!")


@app.route('/<link_code>', methods=['GET', 'POST'])
def redirectToOriginalLink(link_code):
    if searchInDatabase(link_code) == True:
        if checkPass(link_code) == True:
            if request.method == "POST":
                passcode = request.form.get("passcode")
                if matchPassword(link_code, passcode) == True:
                    return redirect(getLink(link_code))
                return render_template('auth_redirect.html', input_message="Incorrect password !!!")
            return render_template('auth_redirect.html', input_message="Enter secret password")
        else:
            return redirect(getLink(link_code))
    else:
        return render_template('not_found.html')


@app.route('/report-a-problem', methods=['GET', 'POST'])
def redirectToReportPage():
    if request.method == "POST":
        problem = request.form.get("msg-box")
        submitProblem(problem)
    return render_template('report_a_problem.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
