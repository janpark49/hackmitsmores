from flask import Flask, render_template
app = Flask(__name__)
global data=[]
@app.route()
def qpage():
    return render_template("qpage.html", ams = data[0], win=data[1], lose= data[2], imglnk=data[3], quest=data[4], ams1=data[5], ams2=data[6], ams3=data[7], ams4=data[8])

if __name__ == '__main__':
    app.run()