# Explore US Bikeshare Data

# Introduction

This project explores data related to bike share systems in three major cities in the United States: Chicago, New York City, and Washington. The data will be imported and analyzed using Python to answer interesting questions about it through computing descriptive statistics. Furthermore, an interactive terminal experience will be created to present these statistics using raw input. The purpose of this project is to gain insights into bike share systems in these cities and present the findings in an accessible way.

## Software used
Python 3, NumPy, and pandas are installed using Anaconda.
A text editor.
A terminal application.

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time
* End Time 
* Trip Duration 
* Start Station
* End Station
* User Type

## Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

### 1 Popular time of travel
* Most common month
* Most common day of the week
* Most common hour of the day

### 2 Popular stations and trip
* Most common start station
* Most common end station
* Most common trip from start to end

### 3 Trip duration
* Total travel time
* Average travel time

### 4 User info
* Counts of each user type
* Counts of each gender (only available for NYC and Chicago)
* Earliest, most recent, most common year of birth (only available for NYC and Chicago)


## An Interactive Experience
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

* Would you like to see data for Chicago, New York, or Washington?
* Would you like to filter the data by month, day, or not at all?
* (If they chose month) Which month - January, February, March, April, May, or June?
* (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit
