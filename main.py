from js import document

def calculate_money():
    input_value = document.querySelector(".convert-input input ").value

    from_unit = document.querySelector( ".from-unit").textContent.lower()
    to_unit = document.querySelector( ".to-unit").textContent.lower()

    if from_unit == "dollar" and to_unit == "azn":
        converted_value = float(input_value) * 1.7 


    symbol = "$"

    document.querySelector("#converted-value").value =  f"{converted_value}{symbol}"
    
    
convert_button = document.querySelector(".convert")
convert_button.onclick = lambda event: calculate_money()