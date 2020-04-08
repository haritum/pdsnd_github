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
    icity = 0
    while (icity not in [1,2,3]):
        print(" [options: -- city --]: \n 1 = chicago \n 2 = new york city \n 3 = washington")
        icity = input(' Enter the city of your interest:')
        icity = int(icity)
        if (icity == 1): city = 'chicago'
        if (icity == 2): city = 'new york city'
        if (icity == 3): city = 'washington'
        try:
            print(" Let us start exploring US bikeshare data in:",city)
        except:
            print(" Please choose the correct city; icity=[1-3]!")
        print("\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    imonth = 0
    while (imonth not in [-1,1,2,3,4,5,6]):
        print(" [options: -- month --]: \n 1 = january \n 2 = february \n 3 = march \n 4 = april \n 5 = may \n 6 = june \n -1 = all")
        imonth = input(' Enter the month of your interest:')
        imonth = int(imonth)
        if (imonth == 1): month = 'january'
        if (imonth == 2): month = 'february'
        if (imonth == 3): month = 'march'
        if (imonth == 4): month = 'april'
        if (imonth == 5): month = 'may'
        if (imonth == 6): month = 'june'
        if (imonth == -1): month = 'all'
        try:
            print(" Let us start exploring US bikeshare data during:",month)
        except:
            print(" Please choose the correct month; imonth=[1-6 or -1]!")
        print("\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    iday = 0
    while (iday not in [-1,1,2,3,4,5,6,7]):
        print(" [options: -- day --]: \n 1 = monday \n 2 = tuesday \n 3 = wednesday \n 4 = thursday \n 5 = friday \n 6 = saturday \n 7 = sunday \n -1 = all")
        iday = input(' Enter the day of your interest:')
        iday = int(iday)
        if (iday == 1): day = 'monday'
        if (iday == 2): day = 'tuesday'
        if (iday == 3): day = 'wednesday'
        if (iday == 4): day = 'thursday'
        if (iday == 5): day = 'friday'
        if (iday == 6): day = 'saturday'
        if (iday == 7): day = 'sunday'
        if (iday == -1): day = 'all'
        try:
            print(" Let us start exploring US bikeshare data on:",day)
        except:
            print(" Please choose the correct day; iday=[1-7 or -1]!")
        print("\n")


    print(' We are going to explore bikeshare data in the US city of:',city)
    print('                                                       in:',month)
    print('                                                       on:',day)

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

    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
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

    if city == 'washington':
        df['Gender'] = 'NaN'
        df['Birth Year'] = 'NaN'

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # TO DO: display the most common month
    cmonth = df['month'].mode()[0] - 1
    print(' >> Most common month is:',months[cmonth])

    # TO DO: display the most common day of week
    cdow = df['day_of_week'].mode()[0]
    print(' >> Most common day of week is:',cdow)

    # TO DO: display the most common start hour
    chour = df['hour'].mode()[0]
    print(' >> Most common start hour is:',chour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    csstation =  df['Start Station'].mode()[0]
    print(' >> Most common start station is:',csstation)

    # TO DO: display most commonly used end station
    cestation =  df['End Station'].mode()[0]
    print(' >> Most common end station is:',cestation)

    # TO DO: display most frequent combination of start station and end station trip
    fcombo = df.groupby(['Start Station','End Station']).size().idxmax()
    print(' >> Most frequent start-end station combination is:',fcombo[0],'-',fcombo[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime = df['Trip Duration'].sum()
    print(" >> Total travel time is:",total_traveltime,'s')

    # TO DO: display mean travel time
    mean_traveltime = df['Trip Duration'].mean()
    print(" >> Mean travel time is:",mean_traveltime,'s')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    nuser = df['User Type'].value_counts(dropna=False)
    print(' >> Types of users:',nuser)

    # TO DO: Display counts of gender
    ngender = df['Gender'].value_counts(dropna=False)
    print(' >> Gender segregation:',ngender)


    # TO DO: Display earliest, most recent, and most common year of birth
    early_yob  = df['Birth Year'].min()
    recent_yob = df['Birth Year'].max()
    common_yob = df['Birth Year'].mode()
    print(' >> Earliest customer\'s year of birth:',early_yob)
    print(' >> Recent customer\'s year of birth:',recent_yob)
    print(' >> Most common customer\'s year of birth:',common_yob)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print (df.head(5))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
