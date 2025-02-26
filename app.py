from flask import Flask, render_template, request

app = Flask(__name__)

def length_converter(value, from_unit, to_unit):
    length_units = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.34}
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {"mg": 0.001, "g": 1, "kg": 1000, "oz": 28.3495, "lb": 453.592}
    grams = value * weight_units[from_unit]
    return grams / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        conversion_type = request.form['conversion_type']

        if conversion_type == 'length':
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == 'weight':
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == 'temperature':
            result = temperature_converter(value, from_unit, to_unit)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
