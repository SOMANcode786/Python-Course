import streamlit as st

def convert(value, from_unit, to_unit, conversion_dict):
    return round(value * (conversion_dict[to_unit] / conversion_dict[from_unit]), 2)

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    st.markdown("""
        <style>
            div[data-testid="stSelectbox"] label {
                cursor: pointer;
            }
            div[data-testid="stSelectbox"] select {
                cursor: pointer;
            }
            h2 {
                color: #007BFF;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🌟 Unit Converter")
    
    conversion_types = {"Length": {
        "Metre": 1, "Kilometre": 0.001, "Centimetre": 100, "Millimetre": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    }, "Weight": {
        "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274
    }, "Temperature": {
        "Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1
    }}
    
    option = st.selectbox("Select Conversion Type:", list(conversion_types.keys()))
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        from_unit = st.selectbox("From:", list(conversion_types[option].keys()), key='from_unit')
    
    with col2:
        st.write("=")
    
    with col3:
        to_unit = st.selectbox("To:", list(conversion_types[option].keys()), key='to_unit')
    
    if value > 0:
        if option == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = round((value * 9/5) + 32, 2)
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = round((value - 32) * 5/9, 2)
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = round(value + 273.15, 2)
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = round(value - 273.15, 2)
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = round((value - 32) * 5/9 + 273.15, 2)
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = round((value - 273.15) * 9/5 + 32, 2)
            else:
                result = value
        else:
            result = convert(value, from_unit, to_unit, conversion_types[option])
        
        st.markdown(f"<h2 style='text-align: center;'>{value} {from_unit} = {result} {to_unit}</h2>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()