
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'yourHomework.py`', '# Dependencies and Setup\nimport matplotlib.pyplot as plt\nimport pandas as pd\nimport numpy as np\nimport requests\nimport time\nimport json\n\n# Import API key\nfrom api_keys import api_key\n\n# Incorporated citipy to determine city based on latitude and longitude\nfrom citipy import citipy\n\n# Output File (CSV)\noutput_data_file = "output_data/cities.csv"\n\n\n# Range of latitudes and longitudes\nlat_range = (-90, 90)\nlng_range = (-180, 180)')


# ## Generate Cities List

# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ## Perform API Calls

# In[ ]:


# Starting URL for Weather Map API Call
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + api_key 


# In[ ]:


Curl = url +"&q=" + city
Response = requests.get(Curl).json()


# In[ ]:


data=[]
Curl=url +"&q=" + city
#Loop through cities
for city in (cities):
    Curl=url +"&q=" +city
    Response = requests.get(Curl).json()
    lng=response["coord"]["lat"]
    lat=response["coord"]["lon"]



# In[ ]:


# hold data for the API 
city_data = []

#looping through cities to create API call for each city
for city in cities:
   # define city from API
   city_url=url + "&q=" + city
   #request data from API
   try:
       
       response= requests.get(city_url).json()
       
       city_lat = response["coord"]["lat"]
       city_lng = response["coord"]["lon"]
       city_max_temp = response["main"]["temp_max"]
       city_humidity = response["main"]["humidity"]
       city_wind = response["wind"]["speed"]
       city_clouds =response["clouds"]["all"]
       city_country =response["sys"]["country"]
       city_date =response["dt"]
       #append information to city_data
       city_data.append({
           "Date":city_date,
           "Country":city_country,
           "City":city,
           "Lat":city_lat,
           "Lng":city_lat,
           "Max Temp":city_max_temp,
           "Humidity":city_humidity,
           "Wind":city_wind,
           "Clouds":city_clouds
})

   except ValueError:
       print("City not found.Skipping city")


# In[ ]:


#Temperature (F) vs. Latitude
plt.scatter(Temp, Lat,  marker="o", facecolors="gold", edgecolors="skyblue") 

# Incorporate the other graph properties
plt.title("Temperature (F) vs. Latitude")
plt.xlabel("Temp")
plt.ylabel("Latitude")


# In[ ]:


#Humidity (%) vs. Latitude
plt.scatter(Hum, Lat,  marker="o", facecolors="gold", edgecolors="skyblue") 

# Incorporate the other graph properties
plt.title("Humidity (%) vs. Latitude")
plt.xlabel("Humidity")
plt.ylabel("Latitude")


# In[ ]:


#Cloudiness (%) vs. Latitude
plt.scatter(Cloud, Lat,  marker="o", facecolors="gold", edgecolors="skyblue") 

# Incorporate the other graph properties
plt.title("Cloudiness (%) vs. Latitude")
plt.xlabel("Cloudiness")
plt.ylabel("Latitude")



# In[ ]:


#Wind Speed (mph) vs. Latitude
plt.scatter(Wind, Lat,  marker="o", facecolors="gold", edgecolors="skyblue") 

# Incorporate the other graph properties
plt.title("Wind Speed (%) vs. Latitude")
plt.xlabel("Wind Speed")
plt.ylabel("Latitude")

