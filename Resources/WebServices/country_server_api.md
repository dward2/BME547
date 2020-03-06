# Country Server API
This server contains data for all of the countries of the world.  Data includes
* population
* area (in square miles)
* gdp (gross domestic product in $ per capita)
* literacy (percent of population)

The countries are grouped into regions.

URL:  <http://vcm-7631.vm.duke.edu:5000>  
  Note:  Server is not always active.  To check, click on the link above.
  If a window opens saying "Server On", then the server is active.  If you 
  receive an error, it is not.  Contact Dr. Ward to activate the server.

### List of Regions
`GET URL/regions`

Returns:  List of strings containing the names of the regions.

### List of All Countries and their Country Codes
`GET URL/countries`

Returns:  List of dictionaries for all countries in database with a format
as shown by the following example:  
  `{'country': 'American Samoa', 'country_code': 'AmericanSamoa'}`

### List of All Countries and their Country Codes in a Region
`Get URL/region/<region_name>`  
    where `<region_name>` is one of the region names returned by 
    ` GET URL/regions`.
    
Returns:  List of dictionaries for all countries in the specified region with
a format as shown by the following example:  
  `{'country': 'American Samoa', 'country_code': 'AmericanSamoa'}`

    
### List of Properties
`GET URL/properties`

Returns:  List of strings containing the names of the properties available for 
each country.

### Country Data
`GET URL/<country_code>`  
   where `<country_code>` is the country_code for the country of interest 
   returned by one of the calls above.
   
Returns:  A dictionary containing data for the country with a format as shown
by the following example:  
```
{'area': '2381740', 
 'country': 'Algeria', 
 'country_code': 'Algeria', 
 'gdp': '6000', 
 'literacy': '70', 
 'population': '32930091', 
 'region': 'AFRICA_NORTHERN'}
 ```

### Single Property for a Country
`GET URL/<country_code>/<property>`  
where `<country_code>` is the country_code for the country of interest returned
by one of the calls above, and `<property>` is one of the properties returned
by `GET URL/properties`.

Returns:  A dictionary containing the country name and property of interest
as shown by the following example:
`{'country': 'Algeria', 'population': '32930091'}`

### Compare Properties Of Two Countries
`POST URL/compare`

JSON Parameter:  `{'one': <country_name_1_str>, 'two': <country_name_2_str>}`  
where `<country_name_1_str>` and `<country_name_2_str>` are strings that 
contain the country names (the full name, not the country_code) of the two
countries to be compared.

Returns:  A string containing a table comparing the two countries in a format
as shown by the following example:
```
  name        Afghanistan           Albania             
  pop.        31056997              3581655              
  area        647500                28748                
  gdp         700                   4500                 
  literacy    36                    86.5                 
```
