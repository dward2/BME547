from flask import Flask, request


app = Flask(__name__)


@app.route("/process_patient/<net_id>", methods=["POST"])
def function_to_break(net_id):
    """
    in_json = {"name": "David Ward",
               "heart_rates": [60, 64, 62],
               "email":  "daw74@duke.edu",
               "balance": 145.35,
               }
    Returns:

    """
    in_data = request.get_json()
    patient_name = in_data["name"]
    first_name, last_name = patient_name.split(" ")
    balance = in_data["balance"]
    balance = balance + 25.00
    heart_rates = in_data["heart_rates"]
    average_heart_rate = sum(heart_rates) / len(heart_rates)
    email = in_data["email"]
    at_location = email.find("@")
    patient_id = email[:at_location]
    domain = email[at_location+1:]
    top_level = domain.split(".")[1]
    out_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "new_balance": balance,
        "average_heart_rate": average_heart_rate,
        "net_id": patient_id,
        "domain": domain,
        "top_level": top_level
    }
    return out_dict


if __name__ == '__main__':
    app.run()
