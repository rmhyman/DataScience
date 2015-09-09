from pandas import *
from ggplot import *
def unit_to_int(unit):
    unit = int(unit[1:4])
    return unit

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    turnstile_weather.is_copy = False
    '''
    print turnstile_weather['UNIT'].head()
    for entry in turnstile_weather['UNIT']:
        entry = entry[1:3]
    print turnstile_weather['UNIT'].head()
    '''
    #print turnstile_weather['UNIT'].head()
    turnstile_weather['UNIT'] = turnstile_weather['UNIT'].apply(unit_to_int)
    #print turnstile_weather['UNIT'].describe()
    #print turnstile_weather['ENTRIESn_hourly'].describe()
    #print turnstile_weather['Hour'].describe()
    #plot = ggplot(turnstile_weather, aes('meantempi')) + geom_histogram(binwidth=10)
    #plot = ggplot(turnstile_weather, aes('Hour','ENTRIESn_hourly',color='UNIT')) + geom_point() + geom_line() + ggtitle('Hourly Entries per Unit')
    plot = ggplot(turnstile_weather, aes('Hour','ENTRIESn_hourly')) + geom_point() + ggtitle('Plot of Entries at various times of the day')
    #plot = ggplot(turnstile_weather, aes(x='Hour',weight='ENTRIESn_hourly')) + geom_bar(binwidth = 10)
    return plot
