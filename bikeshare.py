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
        city = input('\nPlease select a city: chicago, new york city, washington\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Invalid input, please select a city: chicago, new york city, washington ')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease select a month: january, february, march, april, may, june, all\n')
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Invalid input, please select a month: january, february, march, april, may, june or all.')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('\nPlease select a day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all\n').lower()
      if day not in ('sunday, monday, tuesday, wednesday, thursday, friday, saturday, all'):
            print("Invalid input, please select a day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all .")
            continue
      else:
            break

    print('-'*40)
    return city, month, day
#################



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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    print('the most common month:', mode_month)

    # TO DO: display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('the most common day of week:', mode_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mode_hour = df['hour'].mode()[0]
    print('the most common start hour:', mode_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('nmost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days =  total_travel_time.days
    hours = total_travel_time.seconds // (60*60)
    minutes = total_travel_time.seconds % (60*60) // 60
    seconds = total_travel_time.seconds % (60*60) % 60
    print(f'total travel time: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # TO DO: display mean travel time
    mean_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days =  mean_travel_time.days
    hours = mean_travel_time.seconds // (60*60)
    minutes = mean_travel_time.seconds % (60*60) // 60
    seconds = mean_travel_time.seconds % (60*60) % 60
    print(f'mean travel time: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        most_early= int(df['Birth Year'].min())
        print('earliest year of birth:',most_early)
        most_recent= int(df['Birth Year'].max())
        print('most recent year of birth:',most_recent)
        most_common= int(df['Birth Year'].mode()[0])
        print('most common year of birth:',most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view the first five rows of the raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view the first five rows of the raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    