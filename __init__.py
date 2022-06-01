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
            return render_template('home.html', push_link='Put a link !!', abbr="Haha still you didn't generated any link, get one buddy!")

        if searchInDatabase(link_code) == True:
            link_code = randomLinkCode()

        if re.search("^https://", original_link) or re.search("^http://", original_link):
            pushToDatabase(link_code, original_link)
        else:
            pushToDatabase(link_code, f"https://{original_link}")

        push_link = f'http://127.0.0.1:5000/{link_code}'

        return render_template('home.html', push_link=push_link, abbr="GO TO YOUR LINK !")

    return render_template('home.html', push_link='Generate a link !', abbr="Haha you didn't generated any link, get one buddy!")


@app.route(f'/<link_code>')
def redirectToOriginalLink(link_code):
    if searchInDatabase(link_code) == True:
        return redirect(getLink(link_code))
    else:
        return render_template('notfound.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
