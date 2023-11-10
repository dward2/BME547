# Import statements
import tkinter as tk
from tkinter import ttk

WT_UNITS = ["g", "kg", "lb", "oz"]
CONV_TO_KG = [0.001, 1.0, (1.0 / 2.20462), (1 / (16.0 * 2.20462))]
CONV_FROM_KG = [1000.0, 1.0, 2.20462, (2.20462 * 16.0)]


def validate_entry_is_float(new_value):
    try:
        in_temp = float(new_value)
    except ValueError:
        return False
    else:
        return True


def C_to_F(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def make_temp_conversion(starting_unit, temperature):
    try:
        temp = float(temperature)
    except ValueError:
        return "Error"
    if starting_unit == "C":
        f = C_to_F(temp)
        answer = "{}".format(round(f, 2))
    else:
        c = F_to_C(temp)
        answer = "{}".format(round(c, 2))
    return answer


def make_wt_conversion(starting_unit, ending_unit, weight):
    try:
        wt = float(weight)
    except ValueError:
        return "Error"
    # Convert weight from starting unit to "kg"
    kg = weight * CONV_TO_KG[WT_UNITS.index(starting_unit)]
    # Convert weight from "kg" to ending unit
    answer = kg * CONV_FROM_KG[WT_UNITS.index(ending_unit)]
    return answer


def main_window():

    def close_btn_cmd():
        root.destroy()

    def t_radio_change_cmd():
        new_temp = temp_choice.get()
        if new_temp == "C":
            in_unit_label_t.configure(text="C")
            out_unit_label_t.configure(text="F")
        else:
            in_unit_label_t.configure(text="F")
            out_unit_label_t.configure(text="C")
        temp_entry_cmd(temp_value.get())

    def temp_entry_cmd(new_value):
        valid_entry = validate_entry_is_float(new_value)
        if valid_entry:
            starting_unit = temp_choice.get()
            starting_temperature = float(new_value)
            answer = make_temp_conversion(starting_unit, starting_temperature)
            answer_label_t.configure(text=answer)
        return valid_entry

    def wt_entry_cmd(new_value):
        valid_entry = validate_entry_is_float(new_value)
        if valid_entry:
            starting_unit = wt_choice_in.get()
            starting_wt = float(new_value)
            ending_unit = wt_choice_out.get()
            answer = make_wt_conversion(starting_unit, ending_unit, starting_wt)
            answer_label_wt.configure(text=answer)
        return valid_entry

    def wt_units_change(e):
        wt_entry_cmd(wt_value.get())

    # *** Define root window ***
    root = tk.Tk()
    root.title("Converter")

    # *** Add Widgets ***
    # Title
    title_label = ttk.Label(root, text="Unit Conversion",
                            font=("Segoe UI", 10, "bold"))
    title_label.grid(column=0, row=0, columnspan=2)

    # Frame for Temperature Conversion
    temp_frame = ttk.LabelFrame(root, text="Temperature", borderwidth=10)
    temp_frame.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)

    # Add Label and Radio buttons for Units Input
    ttk.Label(temp_frame, text="Input Units:").grid(column=0, row=0,
                                                    columnspan=2)
    temp_choice = tk.StringVar()
    temp_choice.set("C")
    c_btn = ttk.Radiobutton(temp_frame, text="C", variable=temp_choice,
                            value="C", command=t_radio_change_cmd)
    c_btn.grid(column=0, row=1)
    f_btn = ttk.Radiobutton(temp_frame, text="F", variable=temp_choice,
                            value="F", command=t_radio_change_cmd)
    f_btn.grid(column=1, row=1)

    # Entry and output temperatures
    callback_t = root.register(temp_entry_cmd)
    temp_value = tk.IntVar()
    temp_entry = ttk.Entry(temp_frame, width=10, textvariable=temp_value,
                           justify="right", validate='key',
                           validatecommand=(callback_t, "%P"))
    temp_entry.grid(column=0, row=2, sticky=tk.E, pady=(10, 5))
    in_unit_label_t = ttk.Label(temp_frame, text="C")
    in_unit_label_t.grid(column=1, row=2, sticky=tk.W, pady=(10, 5))
    answer_label_t = ttk.Label(temp_frame, text="###")
    answer_label_t.grid(column=0, row=3, sticky=tk.E)
    out_unit_label_t = ttk.Label(temp_frame, text="F")
    out_unit_label_t.grid(column=1, row=3, sticky=tk.W)

    # Frame for Weight Conversion
    wt_frame = ttk.LabelFrame(root, text="Weight", borderwidth=10)
    wt_frame.grid(column=1, row=1, sticky=tk.N, padx=5, pady=5)

    # Input Units
    ttk.Label(wt_frame, text="Input Units").grid(column=0, row=0, columnspan=2)
    wt_choice_in = tk.StringVar()
    wt_choice_in.set("kg")
    wt_selector_in = ttk.Combobox(wt_frame, values=WT_UNITS,
                                  textvariable=wt_choice_in,
                                  state=["readonly"])
    wt_selector_in.bind("<<ComboboxSelected>>", wt_units_change)
    wt_selector_in.grid(column=0, row=1, columnspan=2)

    # Output Units
    ttk.Label(wt_frame, text="Output Units").grid(column=0, row=2,
                                                  columnspan=2,
                                                  pady=(5, 0))
    wt_choice_out = tk.StringVar()
    wt_choice_out.set("lb")
    wt_selector_out = ttk.Combobox(wt_frame, values=WT_UNITS,
                                   textvariable=wt_choice_out,
                                   state=["readonly"])
    wt_selector_out.bind("<<ComboboxSelected>>", wt_units_change)
    wt_selector_out.grid(column=0, row=3, columnspan=2)

    # Entry and output weights
    callback_wt = root.register(wt_entry_cmd)
    wt_value = tk.IntVar()
    wt_entry = ttk.Entry(wt_frame, width=10, textvariable=wt_value,
                         justify="right", validate='key',
                         validatecommand=(callback_wt, "%P"))
    wt_entry.grid(column=0, row=4, sticky=tk.E, pady=(15, 5))
    in_unit_label_wt = ttk.Label(wt_frame, textvariable=wt_choice_in)
    in_unit_label_wt.grid(column=1, row=4, sticky=tk.W, pady=(15, 5))

    answer_label_wt = ttk.Label(wt_frame, text="###")
    answer_label_wt.grid(column=0, row=5, sticky=tk.E)
    out_unit_label_wt = ttk.Label(wt_frame, textvariable=wt_choice_out)
    out_unit_label_wt.grid(column=1, row=5, sticky=tk.W)

    # Close button
    close_button = ttk.Button(root, text="Close", command=close_btn_cmd)
    close_button.grid(column=1, row=2, sticky=tk.E)

    # *** Run initial conversions ***
    temp_entry_cmd(temp_value.get())
    wt_entry_cmd(wt_value.get())

    # *** Display Root Window and Start GUI ***
    root.mainloop()


if __name__ == "__main__":
    main_window()
