# Surge_pricing

## Introduction

Companies like Uber, Lyft, and other taxi services, increase taxi fares when there are more ride requests in a particular area. They do this in order to make sure that the cabs are available for those people who are willing to pay the higher fare. Let us consider a common scenario where a a person pays $20 to watch a game and then pays $80 for a cab ride to go back home makes anyone upset.

This leads to the goal of the project.I’m showing the real-time price surge in different locations in a map. The price surge is shown as a multiplier like is it 1.8 times the normal fare or twice the normal fare. The multiplier is based on the number of pickup requests at that particular location.
So if a ride usually costs 20$ at a place during off-peak hours, it may cost $30 if the multiplier is 1.5 and the multiplier can keep on increasing like 1.8 or twice the normal fare if the number of requests is also increasing.

How is this useful for drivers and passengers?
The profit ratio between the driver and a cab company is 80:20. So a driver gets 80% of the fare. If the driver knows that there is a price surge in a particular location then he could go there to get a pickup request as he would get paid more.
Users can decide whether they are willing to pay the higher fare or wait and request at a later time or request the ride at a place nearby where there is no price surge.
Companies can also use this data to introduce features like low fares during off-peak hours and direct drivers to the place where there is a price surge in order to fulfill more pickup requests.



[Presentaion Link](https://docs.google.com/presentation/d/1k4JkmKybe1vA3XIKXbkomEsgG9qJASuMiKjh6ghnXZA/edit?usp=sharing)

<hr/>


## Architecture

## Dataset

I'm using the taxi trip dataset from the City of Chicago [website.](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew) It is about 75GB in size and has more than 200 million records. The dataset contains the taxi trip records from 2013 to present. I am using this dataset to sumlate my real time data.

## Engineering challenges
### Clustering Locations
### Redis database access