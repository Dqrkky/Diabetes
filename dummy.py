import random
def calculate_humalog_dose(current_bg, target_bg, tdd, carbs, carb_ratio):
    """Calculate Humalog correction and meal bolus doses."""
    isf = 1800 / tdd  # Insulin Sensitivity Factor (ISF)
    correction_needed = current_bg - target_bg  # Blood sugar to correct
    correction_dose = correction_needed / isf if correction_needed > 0 else 0  # Only correct if BG is high

    meal_dose = carbs / carb_ratio if carbs > 0 else 0  # Meal bolus insulin

    total_dose = correction_dose + meal_dose  # Total Humalog dose
    return round(correction_dose, 1), round(meal_dose, 1), round(total_dose, 1)

data = [
    {
        "current_bg": 220,
        "target_bg": 100,
        "tdd": 30,
        "carbs": 50,
        "expected_output": {
            "correction_dose": 2.0,
            "meal_dose": 3.0,
            "total_dose": 5.0
        }
    },
    {
        "current_bg": 180,
        "target_bg": 120,
        "tdd": 20,
        "carbs": 40,
        "expected_output": {
            "correction_dose": 0.7,
            "meal_dose": 1.6,
            "total_dose": 2.3
        }
    },
    {
        "current_bg": 250,
        "target_bg": 100,
        "tdd": 25,
        "carbs": 80,
        "expected_output": {
            "correction_dose": 2.1,
            "meal_dose": 4.0,
            "total_dose": 6.1
        }
    }
]

def generate_test_data(num_cases=10):
    test_data = []
    for _ in range(num_cases):
        current_bg = random.randint(40, 500)  # Random blood sugar between 80 and 300 mg/dL
        target_bg = random.randint(70, 130)  # Target BG between 70 and 130 mg/dL
        tdd = random.randint(16, 18)  # Total daily insulin dose between 10 and 50 units
        carbs = random.randint(10, 100)  # Random carbs from 10 to 100 grams
        # Calculate the doses based on the values
        test_data.append({
            "current_bg": current_bg,
            "target_bg": target_bg,
            "tdd": tdd,
            "carbs": carbs
        })
    
    return test_data
insulin_concentration = 1  # mg per unit (for U-100 insulin)
data += generate_test_data()
for idx, test_case in enumerate(data):
    current_bg = test_case["current_bg"]
    target_bg = test_case["target_bg"]
    tdd = test_case["tdd"]
    carbs = test_case["carbs"]

    # Calculate carb ratio
    carb_ratio = 500 / tdd

    # Calculate the actual Humalog doses
    correction, meal, total = calculate_humalog_dose(current_bg, target_bg, tdd, carbs, carb_ratio)

    # Convert the doses from units to mg
    correction_mg = correction * insulin_concentration
    meal_mg = meal * insulin_concentration
    total_mg = total * insulin_concentration
    
    # Print the results
    tab = " " * 4
    print(f"Test Case {idx + 1}:\n{tab}Current BG: {current_bg},\n{tab}Target BG: {target_bg},\n{tab}TDD: {tdd},\n{tab}Carbs: {carbs}\nCalculated: \n{tab}Correction Dose: {correction} units ({correction_mg:.2f}/mg),\n{tab}Meal Dose: {meal} units ({meal_mg:.2f}/mg),\n{tab}Total Dose: {total} units ({total_mg:.2f}/mg)")
    print("-" * 50)