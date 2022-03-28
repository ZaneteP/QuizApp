from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

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
  images = ["https://icatcare.org/app/uploads/2018/06/Layer-1704-1200x630.jpg", "https://firstvet.com/uploaded/images/articles/_1200x630_crop_center-center_82_none/Cat-vomitingdiarrhea.jpg?mtime=1562592055", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu5OeYesxZYjS_ZcFUoN80NP1OFrJ7tud8RA&usqp=CAU"]
  return render_template("test.html", param=parametri, pictures=images)

if __name__ == '__main__':
  app.run(debug="true")
