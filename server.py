from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def loadAllPictures():
  filepath = 'picDB.txt'
  pictures=[]
  with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
      if line!='':
        fullPicInfo = line.strip().split(';')
        pictures.append(fullPicInfo[1])
      line = fp.readline()
      cnt += 1
  fp.close()
  return pictures

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test')
def test():
  parametri = ["Augums", "Svars", "Vecums"]
  images = loadAllPictures()
  return render_template("test.html", param=parametri, images=images)

if __name__ == '__main__':
  app.run(debug="true")
