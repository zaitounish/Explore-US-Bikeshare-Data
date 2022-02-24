# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:25:58 2022
@author: Taher
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        state = input("Would you like to see data for chicago, new york city, or washington \n")
        stateNames = ['chicago', 'new york city', 'washington']
        if state not in stateNames :
            print("sorry wrong state try again \nPlease choose from", stateNames, " !")
            continue
        else:
            break
   

    
    
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Which month would you like to filter by? January, February, March, April, May, June or type "'all'" if you do not have any preference?\n").title()
        months = ["January", "February", "March", "April", "May", "June", "all"]
        if month not in months :
            print("sorry wrong input \nPlease choose from", months, " !")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
     

    while True:
        day = input("Are you looking for a particular day? If so kindly enter the day as follows: Sunday , Monday, Tuesday, Wednesday , Thursday , Friday , Saturday or type "'all'" if you do not have any preference.\n").title()
        days = ["Sunday" , "Monday", "Tuesday", "Wednesday" , "Thursday" , "Friday" , "Saturday"]
        if day not in days :
            print("sorry wrong input \nPlease choose from", days, " !")
            continue
        else:
            break
                  
    print('-'*40)
    return state, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month_name
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour
    
    df = df[df['month'] == month]
    
    df = df[df['day_of_week'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    mc_month = df['month'].value_counts().idxmax()
  
    print ("the most common month is: ".title(), mc_month)


    # TO DO: display the most common day of week

    mc_day = df['day_of_week'].value_counts().idxmax()
  
    print ("the most common day of week is: ".title(), mc_day)


    # TO DO: display the most common start hour

    mc_hour = df['hour'].value_counts().idxmax()
  
    print ("the most common hour is: ".title(), mc_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    mc_sstation = df['Start station'].value_counts().idxmax()
  
    print ("the most commonly used start station is: ".title(), mc_sstation)



    # TO DO: display most commonly used end station

    mc_estation = df['End Station'].value_counts().idxmax()
  
    print ("the most commonly used end station is: ".title(), mc_estation)

    # TO DO: display most frequent combination of start station and end station trip
    mcf_sestation = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print ("the most frequent combination of start station and end station trip is: ".title(), mcf_sestation)
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_trtime = df['Trip Duration'].value_counts().sum()

    print ("the total Trip Duration is: ".title(), total_trtime)


    # TO DO: display mean travel time
    mean_trtime = df['Trip Duration'].value_counts().mean()

    print ("the mean Trip Duration is: ".title(), mean_trtime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts().counts()
    
    print ("counts of user type is: ".title(), user_types)
    
    
        # TO DO: Display counts of gender
    
    cof_gender = df['Gender'].value_counts().counts()
    
    print ("counts of gender is: ".title(), cof_gender)
    
        # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest_year_of_birth = int(df['Birth Year'].min())
    print ("the earliest year of birth is: ".title(), earliest_year_of_birth)
    
    most_recent_year_of_birth = int(df['Birth Year'].max())
    print ("the most recent year of birth is: ".title(), most_recent_year_of_birth)
    
    most_common_year_of_the_birth = int(df['Birth Year'].value_counts().idxmax())
    print ("the most common year of the birth is: ".title(), most_common_year_of_the_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
