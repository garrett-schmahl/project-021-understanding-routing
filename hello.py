from flask import Flask  
app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return 'Hello World!'  

    
@app.route('/dojo')
def success():
  return "Dojo!"


@app.route('/say/<name>')
def hello(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:value>/<word>')
def repeatWord(value, word):
    return value * word


@app.errorhandler(404)
def function_name(error):
    return 'Sorry! No response. Try again.'


if __name__=="__main__":
    app.run(debug=True) 