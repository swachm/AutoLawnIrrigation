This hack is designed to water the lawn based on the conditions: time of the day, city, and country. 
The software uses an algorithm to determine the wheater to water the lawn based on soil moisture and weather conditions. 

The original idea was to get an user input through an App which would use blutooth to pair the system with home wifi.

I saw the idea on whihc used on and off through rasbery and expanded on it to fully automate the lawn watering process.The prototype would use a raspberry pie 3, pneumatic valve and for completness a underground piping to all the desired locations. The raspberry pie would be used to run the algorithm and trigger the pnematic valves with 5Volt trigger. Once the relay switch is on it would open the valve to water the system.

Inputs:
- Weather Data (past 7days, currently, 24 hour, next 5 days)
- Time of the day
- soil moiture sensor(future expantion)
- City: The city where the system is installed
- Country: The country the system is installed

Output:
-Data loggin on Amazon Web Service
