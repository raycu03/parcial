from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime 
import threading
import csv

app= Flask('app')
@app.route('/',methods=['GET'])
def index():
	title="inicio"
	print(title)
	return render_template('index.html',title=title)

class archivo():
  def __init__(self):
    self.datos = "09052019.csv"#Nombre de la base de datos
    self.time= "time"
    self.temperatura="temperatura"
    self.humedad= "humedad"
    self.tiempo_orden="tiempo_orden"

  def veri(self):
    t = Observer()
    t.start()


da=archivo()

class Observer(threading.Thread):
   def run(self):
      print ("dato guardado")



@app.route('/log',methods=['GET'])	
def log():
  archivo.time = request.args.get('time')
  archivo.tempera= request.args.get('temperatura')
  archivo.humedad = request.args.get('humedad')
  archivo.tiempo_orden = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open('09052019.csv', 'a') as i:
        writer = csv.writer(i)
        writer.writerow([archivo.time,archivo.tempera,archivo.humedad,archivo.tiempo_orden])
  archivo.veri("")


  return ""


if __name__ == '__main__':
	app.debug= True 
	app.run(host="0.0.0.0")
