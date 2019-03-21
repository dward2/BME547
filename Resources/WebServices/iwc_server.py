# iwc_server.py
# Ideal Weight Calculator Server
# David Ward, March 2019

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "Ideal Weight Server is On"


@app.route("/info", methods=["GET"])
def information():
#    info_string = ("This server calculates the ideal weight of a person"
#                   " based on their height, age, and gender.")
    info_string = "Information about server"
#    calc_info_string = ("The calculation can be accessed by POST to the "
#                        "'/calculate_iwc' endpoint with a JSON containing "
#                        "{'age': age, 'height_in': height_inches, "
#                        "'gender': male_or_female}")
    calc_info_string = "Information about calculation"
    out_dictionary = {"info": info_string, "calc_info": calc_info_string}
    return jsonify(out_dictionary)


@app.route("/calculate_iwc", methods=["POST"])
def calculate_iwc_request():
    in_data = request.get_json()
    age = float(in_data["age"])
    gender = in_data["gender"]
    height = float(in_data["height_in"])

    ideal_weight = calculate_iwc(gender, height)

    return jsonify({"input data": in_data,
                    "ideal weight in lb": ideal_weight})


def calculate_iwc(gender, height):
    """Calculates the ideal weight based on height and gender

    Uses G. J. Hamwi Formula (1964), taken from
    https://www.calculator.net/ideal-weight-calculator.html

    Args:
        gender:  (string) containing 'male' or 'female'
        height: (float) height in inches

    Returns:
        float:  ideal weight in lbs
    """
    if gender == 'female':
        ideal_weight_kg = 45.5 + 2.2 * (height - 60)
    else:
        ideal_weight_kg = 48.0 + 2.7 * (height - 60)
    ideal_weight_lb = ideal_weight_kg * 2.20462
    ideal_weight_lb = round(ideal_weight_lb,1)
    return ideal_weight_lb


if __name__ == '__main__':
    app.run()