def getBetweenValue(min :float=None, max :float=None):
    if min < max:
        val = ((max-min)/2) + min
    else:
        val = ((min-max)/2) + max
    return val

def squareRute(x :float=None):
    return x**.5

c = [
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

kg = input("Kg : ")
height = input("Height : ")
kg = float(kg)
height = float(height)

bmi = kg/(height**2)

print([g for g in [{f: c[f]} if c[f] == True else None for f in c] if g != None][0])