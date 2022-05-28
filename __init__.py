from flask import Flask, render_template, redirect, request
from random_gen import randomLinkCode
from db import pushToDatabase, searchInDatabase, getLink
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def runHome():
    if request.method == "POST":
        link_code = randomLinkCode()
        original_link = request.form.get("og-link")

        if len(original_link) <= 0:
            return render_template('home.html', push_link='Put a link !!')

        if searchInDatabase(link_code) == True:
            link_code = randomLinkCode()

        if re.search("^https://", original_link):
            pushToDatabase(link_code, original_link)
        else:
            pushToDatabase(link_code, f"https://{original_link}")

        push_link = f'http://192.168.43.150:5000/{link_code}'

        return render_template('home.html', push_link=push_link)

    return render_template('home.html', push_link='Generate a link !')


@app.route(f'/<link_code>')
def redirectToOriginalLink(link_code):
    if searchInDatabase(link_code) == True:
        return redirect(getLink(link_code))
    else:
        return render_template('notfound.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
