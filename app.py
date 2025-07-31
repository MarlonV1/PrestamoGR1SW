from flask import Flask, render_template, request
from calculator import calcular_cuota

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        monto = float(request.form["monto"])
        tasa = float(request.form["tasa"])
        plazo = int(request.form["plazo"])
        cuota = calcular_cuota(monto, tasa, plazo)
        total = cuota * plazo
        interes = total - monto
        resultado = {
            "cuota": round(cuota, 2),
            "total": round(total, 2),
            "interes": round(interes, 2)
        }
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)