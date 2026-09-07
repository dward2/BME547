def get_tach_limit(age):
    return 120


def is_tachycardic(hr_bpm, age, age_units):
    if age_units == "months":
        age = age / 12
    if age < 15:
        tach_limit = get_tach_limit(age)
    else:
        tach_limit = 100
    if hr_bpm > tach_limit:
        result = True
    else:
        result = False
    return result
