# Temperature

**blinkTemp.py**

> With a DHT.11 temperature sensor it will read the temperature and an LED will blink when a button is clicked.

**readTempDB.py**

> With a Waterproof DS18B20 temperture sensor this will read the temperature and write it to a sqlite3 database. It will read the temperature every minute and print out the data table. The green LED will turn on if the temperature is between 68 and 78, inclusive. The red LED will blink if the temperature is below 68 or above 78.

>First I create my sqlite3 database temperature.db and create the TempData table so that I would be able to store the temperature in that database. I then assign my GPIO pins for my LED's and set the GPIO up. I also assign a variable for how long my LED will blink. I set a curTemp variable so that I can test to see if the temperature is between 68 or 78 inclusive. In the readTemp method I read the temperature using my temperature sensor. Then I have a variable that connect's to my database and a cursor that points to my database. In my logTemp method I get the temperature from the readTemp method and store it in my TempData table that I created using sqlite3. Then I have a print_table method that selects all the data from my TempData table in my temperature database and print it. It will also clear the console everytime there is a new reading. I have a blink function to make the red LED blink until the temperature is between 68 and 78 (inclusive) again. I have a every_min_read method that will read, log, and print the temperature every minute. This function will also tell the program which light will light up.

**readTemperature.py**

> With a Waterproof DS18B20 temperture sensor this wll read the temperature and print it out in the console.

**temp.py**

> Using a DHT22 temperature sensor while true, it will read the temperature and print it out in the console.

**temperature.db**

> This is the temperature database for my readTempDB.py file.

**index.py**

> Run index.py to run the server to see data in graph form. To collect temperature run the readTempDB.py file as well.
