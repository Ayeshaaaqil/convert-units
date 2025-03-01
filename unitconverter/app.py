import streamlit as st

# Apply dark mode using a toggle switch
dark_mode = st.toggle("🌙 Dark Mode")

# Define CSS for light and dark mode
light_css = """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 8px;
        }
        .stSelectbox>div>div {
            background-color: white;
            color: black;
            border-radius: 5px;
        }
        .stNumberInput>div>div>input {
            background-color: white;
            color: black;
            border-radius: 5px;
        }
        .stSuccess {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
"""

dark_css = """
    <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .stButton>button {
            background-color: #444;
            color: white;
            border-radius: 5px;
            padding: 8px;
        }
        .stSelectbox>div>div {
            background-color: #333;
            color: white;
            border-radius: 5px;
        }
        .stNumberInput>div>div>input {
            background-color: #333;
            color: white;
            border-radius: 5px;
        }
        .stSuccess {
            background-color: #17a2b8;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
"""

# Apply selected mode styles
if dark_mode:
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.markdown(light_css, unsafe_allow_html=True)

# Length Converter
def length_converter(value, from_unit, to_unit):
    length_units = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
        "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.34
    }
    meters = value * length_units[from_unit]
    return round(meters / length_units[to_unit], 2)

# Weight Converter
def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "mg": 0.001, "g": 1, "kg": 1000, "oz": 28.3495, "lb": 453.592
    }
    grams = value * weight_units[from_unit]
    return round(grams / weight_units[to_unit], 2)

# Temperature Converter
def temperature_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return round((value * 9/5) + 32, 2)
    elif from_unit == "F" and to_unit == "C":
        return round((value - 32) * 5/9, 2)
    elif from_unit == "C" and to_unit == "K":
        return round(value + 273.15, 2)
    elif from_unit == "K" and to_unit == "C":
        return round(value - 273.15, 2)
    elif from_unit == "F" and to_unit == "K":
        return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == "K" and to_unit == "F":
        return round((value - 273.15) * 9/5 + 32, 2)
    else:
        return value

# Volume Converter
def volume_converter(value, from_unit, to_unit):
    volume_units = {
        "ml": 0.001, "l": 1, "m³": 1000, "gal": 3.785
    }
    liters = value * volume_units[from_unit]
    return round(liters / volume_units[to_unit], 2)

# Speed Converter
def speed_converter(value, from_unit, to_unit):
    speed_units = {
        "mps": 1, "kmph": 3.6, "mph": 2.237
    }
    meters_per_second = value / speed_units[from_unit]
    return round(meters_per_second * speed_units[to_unit], 2)

# Pressure Converter
def pressure_converter(value, from_unit, to_unit):
    pressure_units = {
        "Pa": 1, "atm": 101325, "bar": 100000, "psi": 6894.76
    }
    pascals = value * pressure_units[from_unit]
    return round(pascals / pressure_units[to_unit], 2)

# Streamlit UI
st.title("🔢 Unit Converter")

conversion_type = st.selectbox("🔄 Choose Conversion Type", ["Length", "Weight", "Temperature", "Volume", "Speed", "Pressure"])

value = st.number_input("📏 Enter Value", format="%.2f")

if conversion_type == "Length":
    from_unit = st.selectbox("From", ["mm", "cm", "m", "km", "inch", "ft", "yd", "mile"])
    to_unit = st.selectbox("To", ["mm", "cm", "m", "km", "inch", "ft", "yd", "mile"])
    if st.button("✅ Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From", ["mg", "g", "kg", "oz", "lb"])
    to_unit = st.selectbox("To", ["mg", "g", "kg", "oz", "lb"])
    if st.button("✅ Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["C", "F", "K"])
    to_unit = st.selectbox("To", ["C", "F", "K"])
    if st.button("✅ Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")

elif conversion_type == "Volume":
    from_unit = st.selectbox("From", ["ml", "l", "m³", "gal"])
    to_unit = st.selectbox("To", ["ml", "l", "m³", "gal"])
    if st.button("✅ Convert"):
        result = volume_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")

elif conversion_type == "Speed":
    from_unit = st.selectbox("From", ["mps", "kmph", "mph"])
    to_unit = st.selectbox("To", ["mps", "kmph", "mph"])
    if st.button("✅ Convert"):
        result = speed_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")

elif conversion_type == "Pressure":
    from_unit = st.selectbox("From", ["Pa", "atm", "bar", "psi"])
    to_unit = st.selectbox("To", ["Pa", "atm", "bar", "psi"])
    if st.button("✅ Convert"):
        result = pressure_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result} {to_unit}")
