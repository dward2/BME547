# Frequently Asked Questions

### Do we need to write unit tests a client function that makes a server request?
If you are making a request to a server of yours that may not be "on" during
testing, **No**, a unit test is not required.  However, it should be handled
the same as a server flask handler function.  It does not need to be tested, 
but make sure the client function only does a minimal amount of work:
   * it gets the data needed to make a server request, 
   * it makes the server request, and
   * gets the response


### Do we need to write unit tests for GUI widget command sub-functions?
**No**, as they cannot be easily be tested outside a working GUI.  The GUI
widget command sub-function should do only three things:  
   * get any needed data from the GUI
   * call an outside function to do the necessary work
   * receive the results of that outside function and update the GUI as needed.  

For example, a sub-function might look like this:

    def ok_button_cmd():
        hdl_value = hdl_entrybox_text.get()  # Gets entered value of an entry box from a StringVar()
        answer = analyze_hdl(hdl_value)      # Calss a testable external function to do calculations. 
        result_label[“text”] = answer        # Updates GUI with answer from external function.
        return



