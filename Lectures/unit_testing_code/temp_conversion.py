def celsius_from_fahrenheit(temp_c):
    """ Converts temperature from degrees F to degrees C

    :param temp_c: float with the temperature in degrees Celsius
    :return: float of temperature in degrees Fahrenheit
    """
    temp_f = temp_c * 1.8 + 32

    return temp_f


def detect_fever(temp_list_f):
    """ Return the highest temperature and whether it is a fever

    :param temp_list_f: list of temperatures in degrees Fahrenheit
    :return: tuple with highest temperature and boolean for fever
    """
    largest_temp = max(temp_list_f)
    fever_threshold = 100.5
    if largest_temp > fever_threshold:
        fever = True
    else:
        fever = False

    return largest_temp, fever



