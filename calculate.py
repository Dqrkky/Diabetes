def calculate_humalog_dosage(current_bg, target_bg, tdd):
    # Calculate the Insulin Sensitivity Factor (ISF) using the 1800 Rule
    # ISF tells you how much 1 unit of insulin will lower your blood sugar.
    isf = 1800 / tdd  # 1800 Rule is used for rapid-acting insulin (like Humalog)

    # Calculate the difference between the current blood sugar (BG) and target BG
    correction_needed = current_bg - target_bg

    # Calculate the required Humalog dose to correct the blood sugar
    humalog_dose = correction_needed / isf

    # Return the final dose, ensuring it's not negative (min 0 units)
    # Round the dose to 1 decimal place for precision
    return max(0, round(humalog_dose, 1))

current_bg = 500
target_bg = 200
tdd = 16
print(calculate_humalog_dosage(current_bg, target_bg, tdd))