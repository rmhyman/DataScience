from pandas import *
from ggplot import *
def unit_to_int(unit):
    unit = int(unit[1:4])
    return unit
def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    turnstile_weather.is_copy = False
    turnstile_weather['UNIT'] = turnstile_weather['UNIT'].apply(unit_to_int)
    #print turnstile_weather['UNIT'].describe()
    print turnstile_weather['ENTRIESn_hourly'].describe()
    #print turnstile_weather['Hour'].describe()
    plot = ggplot(turnstile_weather, aes(x='ENTRIESn_hourly')) + geom_histogram()
    #plot = ggplot(turnstile_weather, aes('UNIT','ENTRIESn_hourly',color='rain')) + geom_point() + ggtitle('Number of Entries per Unit Based on Rain Conditions')
    #plot = ggplot(turnstile_weather, aes('Hour','ENTRIESn_hourly')) + geom_point() + ggtitle('Plot of Entries at various times of the day')
    #plot = ggplot(turnstile_weather, aes(x='Hour',weight='ENTRIESn_hourly')) + geom_bar(binwidth = 10)
    
    return plot
