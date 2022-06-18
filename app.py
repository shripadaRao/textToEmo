import text2emotion as te
import os
from flask import Flask, render_template
from flask import request

def printEmo(text):
    emo = te.get_emotion(text)
    return emo


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  
    if request.method == 'POST':
      form = request.form
      result = []
      bert_abstract = form['paragraph']
      result.append(printEmo(bert_abstract))
      result.append(form['paragraph'])

      return render_template("index.html",result = result)

    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

