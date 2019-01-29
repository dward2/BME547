def test_celsius_from_fahrenheit():
    from temp_conversion import celsius_from_fahrenheit

    result = celsius_from_fahrenheit(20)
    assert result == 68


def test_detect_fever():
    from temp_conversion import detect_fever

    input_temps = [98, 99, 100, 102, 95]
    (max_temp, is_fever) = detect_fever(input_temps)

    assert max_temp == 102
