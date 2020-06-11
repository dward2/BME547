# Installation Info for macOS

## SSL or Certificate Errors
Python 3.6 and higher for Mac may not come configured to use the 
standard root certificate authorities.  So, some folks may get a ssl error, 
other error, or just not be able to reach certain web services, such as 
MongoDB. 

To fix this, open a terminal window and make sure you are in your home
directory (`cd ~`), that you are not in a virtual environment, and enter the 
following command:

```
/Applications/Python\ 3.6/Install\ Certificates.command
```

If you installed Python 3.7 or 3.8, change 3.6 to 3.7 or 3.8 in the command 
above.

If you get a permission error while trying to install a package after entering
the above command, include `sudo` before the command, and be prepared to enter
your system password.

If you're getting an error like this in conda, try 
```sh
conda remove certifi
conda install certifi
```

Another link with possible solutions beyond the above might be found at this
link:
<https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore/42107877#42107877?newreg=819ef0d3d63740389ddd7206c106b4a0>
