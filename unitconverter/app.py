import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
        "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.34
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "mg": 0.001, "g": 1, "kg": 1000, "oz": 28.3495, "lb": 453.592
    }
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

st.title("Unit Converter")

conversion_type = st.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter value")

if conversion_type == "Length":
    from_unit = st.selectbox("From", ["mm", "cm", "m", "km", "inch", "ft", "yd", "mile"])
    to_unit = st.selectbox("To", ["mm", "cm", "m", "km", "inch", "ft", "yd", "mile"])
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From", ["mg", "g", "kg", "oz", "lb"])
    to_unit = st.selectbox("To", ["mg", "g", "kg", "oz", "lb"])
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["C", "F", "K"])
    to_unit = st.selectbox("To", ["C", "F", "K"])
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")
