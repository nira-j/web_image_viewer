import os
from flask import Flask
from flask import render_template

app=Flask("myapp")

@app.route("/")
def home():
    os.chdir(r"C:\Users\niraj\Desktop\image-gallery-master\static\img")
    img=os.listdir()
    li_img=[]
    for i in img:
        li="static/img/"+i
        li_img.append(li)
    return render_template("index.html", navi=li_img)

app.run(debug=True)