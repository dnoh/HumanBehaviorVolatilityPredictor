# HumanBehaviorVolatilityPredictor
### Using Machine Learning models to predict the volatility of human behavior datasets.

* Model List
  * Arima

* How to run:
  * Clone repository
  * Download desired libraries and dependencies
  * Run command is python3 driver.py
  * When asked "What Model?", choose from the list of models above.
  * Starting Point is the index to begin the predicitions on
  * Window Size is the size of the predicition Window
  * file is a file you choose that is saved in the data folder
  
  
Example Command:
<code> python3 driver.py </code> \n
<code> Arima </code>
<code> 0 </code>
<code> 14 </code>
<code> retail_sales.csv </code>
  
This will return a csv file with the data predictions and the percent errors. 


