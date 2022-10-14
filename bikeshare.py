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
    print('Hello!Hello! Let\'s explore some US bikeshare data!')
    # gets user input for city (chicago, new york city, washington).
    
    while True:
        city = ''
        city=input('\nwhich city data would you like to view : chicago, new york city, washington?\n')
        city = city.lower() 
        if city not in CITY_DATA:
            print("sorry!!! Invalid input, try again")   
            
        else:
          break
          print("You have chosen" ' ' + city.title() +" as your city.Let\'s get started *_*.")
    
    # gets user input for month (all, january, february, ... , june)
    while True:
        month = input('select month between January and June ')
        month = month.lower()
        months = {'all': 0, 'january':1,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, }
        if month not in months:
            print("Sorry!! Invalid Input, Try again ")
            
        
        else:
            break
            
    # gets user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Which day of the week would you like to view?\n')
        day=day.lower()
        days= {'all': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
        if day not in days:
              print("\nSorry!!!Invalid input! Try again")
        else: 
            break
            print('-'*40)
    return city, month, day      
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filtering by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

        # filtering by day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
       
    start_time = time.time()

    # displays the most common month
    common_month =df['month'].mode()[0]
    print('most common month:', common_month)

    #  displays the most common day of week
    common_day =df['day_of_week'].mode()[0]
    print('most common day:', common_day)



    #  displays the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    common_hour =df['hour'].mode()[0]
    print('most common hour:', common_hour)            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    #  displays most commonly used start station
    common_start_station =df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)
    

    # displays most commonly used end station
    common_end_station =df['End Station'].mode()[0]
    print('Most Commmon End Station:', common_end_station)
    
    # displays most frequent combination of start station and end station trip
    common_start_end_station =df['Start Station'] +' - '+df['End Station'].mode()[0]
    print('Most Frequent Start and End Station:', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  displays total travel time
    total_travel_time =df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')
    
    # displays mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    print('Mean Travel time:', mean_travel_time, 'seconds')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Displays counts of user types
    user_types = df['User Type'].value_counts()
    
    #  Displays counts of gender
    try:
        gender =df['Gender'].value_counts()
        print('Counts of gender')
    except:
        print('NO gender found')
     
       

    # Displays earliest, most recent, and most common year of birth
    try:
        earliest =int(df['Birth Year'].min())
        print('Earliest Year of Birth:', earliest)
        recent =int(df['Birth Year'].max())
        print('Most Recent Year of birth:', recent)
        common_birth_year =int(df['Birth Year'].mode()[0])
        print('Most Common Year of Birth:', common_birth_year)
    except:
        print('NO birth years found')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def raw_data(df):
    """ Displays the raw data five rows at a time"""
    n = 0
    while True:
        raw = input('Would like to see raw data? Type \'yes\' or \'no\'')
        raw = raw.lower()
        if raw != 'yes':
            print('That how the raw data looks like. Lets continue *_*')
            break
        else:
            n = n + 5
            print(df.iloc[n: n + 5])
    print('-' * 40)
 
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
                  
