from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/v2/comprar")
def comprar():
    data = request.get_json(silent=True) or {}
    producto_id = data.get("producto_id")

    if producto_id is None:
        return jsonify({"error": "El campo producto_id es obligatorio."}), 400

    return (
        jsonify(
            {
                "mensaje": "Compra procesada exitosamente por el Microservicio Flask (v2)",
                "producto_id": producto_id,
                "cantidad": data.get("cantidad", 1),
                "status": "Aprobado",
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
