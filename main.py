def getBetweenValue(min :float=None, max :float=None):
    if min < max:
        val = ((max-min)/2) + min
    else:
        val = ((min-max)/2) + max
    return val

def squareRute(x :float=None):
    return x**.5

data = [
    {
        "type": "Severe Thinness",
        "values": {
            "min": 2,
            "max": 16
        }
    },
    {
        "type": "Moderate Thinness",
        "values": {
            "min": 16,
            "max": 17
        }
    },
    {
        "type": "Mild Thinness",
        "values": {
            "min": 17,
            "max": 18.5
        }
    },
    {
        "type": "Normal",
        "values": {
            "min": 18.5,
            "max": 25
        }
    },
    {
        "type": "Overweight",
        "values": {
            "min": 25,
            "max": 30
        }
    },
    {
        "type": "Obese Class I",
        "values": {
            "min": 30,
            "max": 35
        }
    },
    {
        "type": "Obese Class II",
        "values": {
            "min": 35,
            "max": 40
        }
    },
    {
        "type": "Obese Class III",
        "values": {
            "min": 40,
            "max": 70
        }
    }
]

#bmi and height to kg
#bmi*(height**2)

#bmi and kg to height
#(kg/bmi)**.5

kg = float(input("Kg : "))
height = float(input("Height : ")) / 100

def bmi(kg, height):
    return kg/(height**2)

_bmi = bmi(kg, height)

bmi_category = {i["type"]: i["values"]["min"] < _bmi and _bmi < i["values"]["max"] for i in data}
for category, is_in_range in bmi_category.items():
    if is_in_range:
        print(f"The BMI of {round(_bmi)} is classified as: {category}")