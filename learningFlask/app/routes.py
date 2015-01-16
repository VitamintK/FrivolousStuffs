
from flask import Flask
from flask import render_template
app = Flask(__name__)

quotes = [
      {
          'author': 'Skylar',
          'quote': 'robot hands'
      },
      {
          'author': 'Rick',
          'quote': 'motorized hammer'
      },
      {
          'author': 'Laina',
          'quote': 'kitten incubator'
      }      
]


@app.route('/')
def index():
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
	app.run(debug=True)
