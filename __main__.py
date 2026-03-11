from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    with open('documentary.md','r', encoding="UTF-8") as f:
        txt = markdown.markdown(f.read(), extensions=["extra"])
    return render_template('index.html', content=txt)


if __name__ == "__main__":
    app.run()
