from flask import Flask, render_template, request, url_for, flash, redirect
from flask_cors import CORS 
import multiprocessing
import interpreter
app = Flask(__name__)
CORS(app)

@app.route("/execute", methods=('POST',))
def execute():
    code = request.form['code'].replace("\r", "")
    input_list = request.form["inputs"].replace("\r", "")
    header = request.form["header"].replace("\r", "")
    footer = request.form["footer"].replace("\r", "")
    
    manager = multiprocessing.Manager()
    ret = manager.dict()
    
    ret["out"] = ""
    ret["debug"] = ""
    
    proc =  multiprocessing.Process(target=interpreter.execute, args=(code, input_list, ret))
    proc.start()
    proc.join(time)
    
    if proc.is_alive():
      proc.kill()
          ret["debug"] = f"Code timed out after 60 seconds"
    return render_template('index.html', code=code, header=header, footer=footer, output=ret["out"], inputs=input_list, errors=ret["debug"])
        
