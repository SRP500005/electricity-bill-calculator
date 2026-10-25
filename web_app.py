from flask import Flask, request

from app import calculate_bill


app = Flask(__name__)


@app.get("/")
def home():
    return """
    <h1>Electricity Bill Calculator</h1>
    <form action="/calculate" method="post">
        <label>Consumption in kWh:</label>
        <input type="number" name="units" min="0" step="any" required>

        <label>Price per kWh in euros:</label>
        <input type="number" name="price" min="0" step="any" required>

        <button type="submit">Calculate</button>
    </form>
    """


@app.post("/calculate")
def calculate():
    try:
        units = float(request.form["units"])
        price = float(request.form["price"])

        total = calculate_bill(units, price)

        return f"<h1>Your electricity bill is €{total:.2f}</h1>"

    except ValueError:
        return "Enter valid, non-negative numbers.", 400