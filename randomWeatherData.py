import random
import numpy as np
import pandas as pd

def bound(low, high, value):
  return max(low, min(high, value))

numRandomExamples = 2000

randomLatitudes = []
randomLongitudes = []
randomTemps = []
randomPressures = []
randomHumidities = []
randomDewPoints = []
randomUvi = []
randomClouds = []
randomWindSpeed = []
randomWindDeg = []
randomWindGust = []
randomPrices = []

probabilities = [0] * numRandomExamples 

# Intuitively, cheap places are sometimes good for building wind turbines, so we want to offset the price to make it more expensive
# Since each of these examples are negative examples
minimumPrice = 100000
priceMeanOffset = 50000 

for i in range(numRandomExamples):
  randomLatitudes.append(round(random.uniform(50, 60), 4))
  randomLongitudes.append(round(random.uniform(-8, 2), 4))
  randomTemps.append(round(max(0, np.random.normal(282.1, 2.1)), 2))
  randomPressures.append(round(max(0, np.random.normal(1015.8, 12.0)), 0))
  randomHumidities.append(round(bound(0, 100, np.random.normal(76.7, 9.5)), 0))
  randomDewPoints.append(round(np.random.normal(278.1, 2.6), 2))
  randomUvi.append(round(max(0, np.random.normal(0.013, 0.033)), 2))
  randomClouds.append(round(bound(0, 100, np.random.normal(78.7, 25.7)), 0))
  randomWindSpeed.append(round(max(0, np.random.normal(9.1, 3.7)), 2))
  randomWindDeg.append(round(max(0, np.random.normal(281.1, 46.8)), 0))
  randomWindGust.append(round(max(0, np.random.normal(16.3, 5.5)), 2))
  randomPrices.append(round(max(minimumPrice, np.random.normal(301648.6 + priceMeanOffset, 252317.9)), 0))

finalRandomData = {'latitude' : randomLatitudes, 'longitude' : randomLongitudes, 'temp' : randomTemps, 'pressure' : randomPressures, 'humidity' : randomHumidities, 'dew_point' : randomDewPoints, 'uvi' : randomUvi, 'clouds' : randomClouds, 'wind_speed' : randomWindSpeed, 'wind_deg' : randomWindDeg, 'wind_gust' : randomWindGust, 'price' : randomPrices, 'probability' : probabilities}

dfRandom = pd.DataFrame(data=finalRandomData)

dfRandom.to_csv(r'/users/stevenchen/Development/ICHACK22/randomWeatherAndPricesData.csv', index = True)
