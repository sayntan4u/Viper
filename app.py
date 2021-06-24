from flask import Flask, render_template, request
from phoenix import Phoenix

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html")

@app.route('/runCode',methods = ['POST'])
def runCode():
  code = request.form['code']
  lang = request.form['lang']

  p1= Phoenix(code,lang) 
  out=""
  if(lang == "C" or lang == "C++"):
    out = p1.process_c_cpp()
  elif(lang == "Java"):
    pass
  elif(lang == "Python"):
    out = p1.process_python()
  
  return out

  

if __name__ == '__main__':
   app.run(debug = True)