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
        city = input('please choose from the 3 cities : chicago, new york city or washington: ').lower()
        if city not in CITY_DATA:
            print("sorry you did not choose from the options were given, please try again") 
        else:
            print("Nice..your choice is, {}".format(city))
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('So please choose from the first 6 months, or choose all: ').lower()
        months = ['january','february','march','abril','may','june']
        if month not in months and month !='all':
            print("incorrect answer, please Try again..")
        else:
            print("okay you chose , {}".format(month))
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday
    while True:
        day = input('NOW please choose any day you prefer, or choose all: ').lower()
        days = ['saturday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day not in days and day != "all":
            print("invalid choice, please try again..")
        else:
            print("your choice is.. {}".format(day))
            print("Thank you, you will get your data in seconds ..")
            break
    

    print('-'*40)
    return city, month, day
#-----------------------------------------

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])  #convert start time into datetime
    
    df['month'] = df['Start Time'].dt.month      # extract month from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name  # extract day from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour   #extract hour from Start Time to create new columns                                                     
    
    if month != 'all':            
        # use the index of the months list to get the corresponding int                                     
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1         
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

#---------------------------------------------
def display_raw_data(city):
    response = input("would you like to see the row data? , please answer with(yes/no)".lower())
    if response == "yes":
        print(df[CITY_DATA].head())



#------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is : ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is : ", popular_day )

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is : ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#--------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start station is : ", popular_start_station)

    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common end station is : ", popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"] + "to" + df["End Station"]
    comb = df["trip"].mode()[0]
    print("The most frequent combination of start station and end station is : ", comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#----------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is : ", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average of the travel time is : ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("The counts of user type is : ", count_user_type)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print("The counts of gender is : ", count_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("The most recent year of birth is : ", df['Birth Year'].max())
        print("The earliest year of bith is : ", df['Birth Year'].min())
        print("The most common year of birth is : ", df['Birth Year'].mode())


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
