def convert(choice, temp):
    match choice:
            case 1:
                return f"{temp+273.15} K"
            case 2:
                t=(temp*(9/5))+32
                return f"{t} °F"
            case 3:
                return f"{temp-273.15} °C"
            case 4:
                t=((temp-273.15)*(9/5))+32
                return f"{t} °F"
            case 5:
                t=(temp-32)*(5/9)
                return f"{t} °C"
            case 6:
                t=((temp - 32) * (5 / 9))+273.15
                return f"{t} K"
            case default:
                return "Error!"

ch=int(input("TEMPERATURE CONVERTER\nPress:\n1 to convert Celsius to Kelvin\n"
             "2 to convert Celsius to Fahrenheit\n"
             "3 to convert Kelvin to Celsius\n"
             "4 to convert Kelvin to Fahrenheit\n"
             "5 to convert Fahrenheit to Celsius\n"
             "6 to convert Fahrenheit to Kelvin\n"))
tp=float(input("Enter the temperature to be converted: "))
st=convert(ch, tp)
print(f"The required temperature is: {st}")