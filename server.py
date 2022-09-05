from flask import Flask, render_template


app= Flask(__name__)



@app.route("/")
def root():
    return render_template("chessboard.html",rows=8,cols=8,light="light",dark="dark")

@app.route("/4")
def size4():
    return render_template("chessboard.html",rows=4,cols=8,light="light",dark="dark")

@app.route("/<x>/<y>")
def sizeXY(x,y):
    return render_template("chessboard.html",rows=int(x),cols=int(y),light="light",dark="dark")


@app.route("/<x>/<y>/<color1>/<color2>")
def sizeXY_Color(x,y,color1,color2):
    return render_template("chessboard.html",rows=int(x),cols=int(y),light=color1,dark=color2)


if(__name__=="__main__"):
    app.run(debug=True)