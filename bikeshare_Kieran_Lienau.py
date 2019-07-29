# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:02:31 2019

@author: lienauki
"""
# UDACITY - Project 2: Analyze US Bikeshare Data
#written with ANACONDA
#tested in IPython Consol

import pandas as pd
import calendar
import pprint
import time
import numpy as np
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)

CITY_DATA = { 'c': 'chicago.csv',
             'n': 'new_york_city.csv',
             'w': 'washington.csv',
             'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'
             }

def choose_city():
    """
    Asks user to specify a city to analyse.

    Returns:
        (str) city - name of the city to analyse
    """

    print('\nHello and welcome to some statistics of US Bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: While loop to check whether input is valid

    while True:
        city=input("The data of which city should be evaluated first? Please make your choice: \nChicago (C), \nNew York City (N)\nWashington (W)?\n\n").lower()
        if city == 'chicago' or city == 'c':
           print("\nYour choice: Chicago\n")
        if city == 'new york city' or city == 'n':
           print("\nYour choice: New York City\n")
        if city == 'washington' or city == 'w':
            print("\nYour choice: Washington\n")
        if city not in ('chicago', 'c', 'new york city', 'n', 'washington', 'w'):
            print("\nInvalid input, please try again :)")
            continue
        else:
            break

    return city


def choose_month():
    """
    Month has to be chosen

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """

    # get user input for month (all, january, february, ... , june)

    while True:
        month=input("\nWould you like to analyze a specific month or should all months be displayed?\nPlease make your choice:\n\nJanuary (1), \nFebruary (2),\nMarch (3), \nApril (4),\nMay (5),\nJune (6),\nall months (all)?\n\n").lower()
        if month=='january' or month=='1':
            print ("\nYour choice: January\n")
            return 'january'
        elif month=='february' or month=='2':
            print ("\nYour choice: February\n")
            return 'february'
        elif month=='march' or month=='3':
            print ("\nYour choice:  March\n")
            return 'march'
        elif month=='april' or month=='4':
            print ("\nYour choice: April\n")
            return 'april'
        elif month=='may' or month=='5':
            print ("\nYour choice: May\n")
            return 'may'
        elif month=='june' or month=='6':
            print ("\nYour choice: June\n")
            return 'june'
        if month not in ('1', '2', '3', '4', '5', '6', 'january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("\nInvalid input, please try again :)")
            continue
        else:
            break

    return month


def choose_day():
    """
    Day has to be chosen

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input("\nWould you like to analyze a specific day of the week?\nPlease make your choice: \n\nMonday (1), \nTuesday (2),\nWednesday (3), \nThursday (4),\nFriday (5),\nSaturday (6),,\nSunday (7),\nall days of the week (all)?\n\n").lower()
        if day=='monday' or day=='1':
            print ("\nYour choice: Monday; Here you can see the statistics based on your filters:\n")
            return 'monday'
        elif day=='tuesday' or day=='2':
            print ("\nYour choice: Tuesday; Here you can see the statistics based on your filters:\n")
            return 'tuesday'
        elif day=='wednesday' or day=='3':
            print ("\nYour choice: Wednesday; Here you can see the statistics based on your filters:\n")
            return 'wednesday'
        elif day=='thursday' or day=='4':
            print ("\nYour choice: Thursday; Here you can see the statistics based on your filters:\n")
            return 'thursday'
        elif day=='friday' or day=='5':
            print ("\nYour choice: Friday; Here you can see the statistics based on your filters:\n")
            return 'friday'
        elif day=='saturday' or day=='6':
            print ("\nYour choice: Saturday; Here you can see the statistics based on your filters:\n")
            return 'saturday'
        elif day=='sunday' or day=='7':
            print ("\nYour choice: Sunday; Here you can see the statistics based on your filters:\n")
            return 'sunday'
        if day not in ('1','2','3','4','5','6','7','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
            print("\nInvalid input, please try again :)")
            continue
        else:
            break

    return day

    print('_'*70)


def load_choice(city, month, day):
    """
Data for the given filters (city, month, day) is loaded.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by; "all" = no filter
        (str) day - name of the day of week to filter by; "all" = no filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # loading the data from CSV into dataframe

    df = pd.read_csv(CITY_DATA[city])

    # converting timestamp (column 'Start Time') into datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # getting the name of the weekday (Monday, Tuesday,..) out of the timestamp

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # getting the month (January, February,...) out of the timestamp

    df['month'] = df['Start Time'].dt.month

    # set the filter to month as chosen
        # create the number of the month by index of the list
        # build a new data frame

    if month != 'all':
        months = ['buffer', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['month'] == month]

    # set the filter to weekday as chosen
        # build a new data frame

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n' + '_'*70 +'\n')
    print('\nCalculating the most frequent times of travel:....................\n')
    start_time = time.time()

    # display the most common month
        # Group by month and count the values
        # sort the values ascending and print the highest result

    month_group = df.groupby('month')['Start Time'].count()
    print("Most common month (number of starts):\n\n" + calendar.month_name[int(month_group.sort_values(ascending = True).index[-1])])

    most_common_weekday = df['day_of_week'].mode()[0]
    print('\n\nMost common day of the week:\n')
    print(most_common_weekday)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\n\nMost common hour:\n')
    print(most_common_hour)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most popular stations and trips:....................\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station=df['Start Station'].value_counts()[df['Start Station'].value_counts() == df['Start Station'].value_counts().max()]
    print('Most common start station:\n\n', most_common_start_station)

    # display most commonly used end station
    most_common_end_station=df['End Station'].value_counts()[df['End Station'].value_counts() == df['End Station'].value_counts().max()]
    print('\n\nMost common end station:\n\n', most_common_end_station)

    # display most frequent combination of start station and end station

    most_common_combination=df.groupby(['Start Station', 'End Station']).size().nlargest(3).sort_values(ascending=False)
    print('\n\nMost common three combinations of start station and end station:\n\n', most_common_combination)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating trip duration:....................\n')
    start_time = time.time()

    # display total travel time

    sum_travel_time = np.sum(df['Trip Duration'])
    print ('Total travel time:', '{:,.1f}'.format(sum_travel_time/(60*60*24)), " Days")

    # display mean travel time

    mean_travel_time = np.mean(df['Trip Duration'])
    print('Average travel time per trip:', '{:,.1f}'.format(mean_travel_time/60), " Minutes")

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats:....................\n')
    start_time = time.time()

    # Display counts of user types

    user_type = df.groupby('User Type')['User Type'].count().sort_values(ascending=False)
    print('\n',user_type)

    # Display counts of gender
    try:
      print("\n\n")
      gender_type = df.groupby('Gender')['Gender'].count().sort_values(ascending=False)
      print(gender_type)
      print('\n\n')
    except KeyError:
      print("\n\nThere was an error while looking for your desired information.")
    except:
      print("\n\nThere was an error while looking for your desired information.")

    labels ='male', 'female'
    try:
        counts_gender = df['Gender'].value_counts()
        colors = ["#1f77b4", 'lightskyblue']
        explode = (0.1, 0)
        plt.pie(counts_gender, labels=list(labels), explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=60)
        plt.title("Gender Distribution in selected months / days")
        plt.show()
    except KeyError:
      print("\n\nThere was an error while looking for your desired information.")

    # Display earliest, most recent, and most common year of birth

    try:
      earliest_birth_year = np.min(df['Birth Year'])
      print('\n\n\nEarliest birth year:\n')
      print('{:04.0f}'.format(earliest_birth_year))
    except KeyError:
      print("\n\nEarliest birth year:\nThere was an error while looking for your desired information.")
    except:
      print("\n\nThere was an error while looking for your desired information.")

    try:
      latest_birth_year = np.max(df['Birth Year'])
      print('\n\nLatest birth year:\n')
      print('{:04.0f}'.format(latest_birth_year))
    except KeyError:
      print("\n\nLatest Birth year:\nThere was an error while looking for your desired information.")
    except:
      print("\n\nThere was an error while looking for your desired information.")

    try:
      most_common_birth_year=df['Birth Year'].value_counts().idxmax()
      print('\n\nMost common birth year:\n')
      print('{:04.0f}'.format(most_common_birth_year))
    except KeyError:
      print("\n\nMost common birth year:\nThere was an error while looking for your desired information.")
    except:
      print("\n\nThere was an error while looking for your desired information.")

def show_dataframe(df):

    qty_rows = 0
    show = input("Would you like to see the first ten rows of the data frame used for the calculations?\nPlease type 'yes' or 'no':\n\n").lower()
    while True:
        if show == 'no':
            return
        if show == 'yes':
            print(df[qty_rows: qty_rows + 10])
            qty_rows = qty_rows + 10
            show = input("Would you like to see ten more rows of the data frame used for the calculations?\nPlease type 'yes' or 'no':\n\n").lower()
        else:
            break

def main():

    while True:
        city = choose_city()
        month = choose_month()
        day=choose_day()
        df = load_choice(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_dataframe(df)

        restart = input('\nRestart? Enter yes or no.\n').lower()
        if restart == 'yes':
            continue
        else:
            break

if __name__ == "__main__":
    main()
