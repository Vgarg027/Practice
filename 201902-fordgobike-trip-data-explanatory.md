# (Effects of Start and End station ,Age,Gender,User Type in the trip durations in the 201902-fordgobike-trip data set)
## by (Ahmed Abd el Hady Elsheikh)

## Investigation Overview

> In this investigation, I wanted to look at the effect of variables provided in the data set(Start and End station ,Age,Gender,User Type) in the trip durations .

## Dataset Overview

> There are 183412 trips done by 4646 bikes in the dataset with the following statistic outcomes:

16 variables: 9 numerical, 2 datetime, 4 object type and 1 is boolean type.
(7 Added columns: month, day_of_week, hour, year, combined_stations,age,id)

Most common month: 2,
Most common day of week: Thursday,
Most Popular Start Hour: 17

============================================================
most commonly used start station: Market St at 10th St,
most commonly used end station: San Francisco Caltrain Station 2(Townsend St at 4th St),
most frequent combination of start station and end station trip:
start: Berry St at 4th St end: San Francisco Ferry Building (Harry Bridges Plaza)

============================================================

Subscriber 163544 Customer 19868

============================================================

Male 130651,
Female 40844,
Other 3652

============================================================

Most common year of birth: 1988.0,
Most recent year of birth: 2001.0,
Earliest year of birth: 1920.0


```python
# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

%matplotlib inline

# suppress warnings from final output
import warnings
warnings.simplefilter("ignore")
```


```python
# load in the dataset into a pandas dataframe
df=pd.read_csv('201902-fordgobike-tripdata.csv')
```


```python
df['age']=2019-df['member_birth_year']
df=df[df['age']<=100]
df=df.dropna()
df.bike_share_for_all_trip=(df.bike_share_for_all_trip =='Yes')
```


```python
"""Displays statistics on the most frequent times of travel."""
df['start_time'] = pd.to_datetime(df['start_time'])
# display the most common month
df['month'] = df['start_time'].dt.month
common_month = df['month'].mode()[0]
# display the most common day of week
df['day_of_week'] = df['start_time'].dt.day_name()
common_day_of_week = df['day_of_week'].mode()[0]
# display the most common start hour
df['hour'] = df['start_time'].dt.hour
popular_hour = df['hour'].mode()[0]
df['year']=df.start_time.dt.year

"""Displays statistics on the most popular stations and trip."""
# display most commonly used start station
common_start_station=df['start_station_name'].mode()[0]
# display most commonly used end station
common_end_station=df['end_station_name'].mode()[0]
  
# display most frequent combination of start station and end station trip
df['combined_stations']='start: '+df['start_station_name']+' '+'end: '+df['end_station_name']
df = df.assign(id=(df['start_station_name'] + '_' + df['end_station_name']).astype('category').cat.codes)

common_combined_stations=df['combined_stations'].mode()[0]

"""Displays statistics on bikeshare users."""
# Display counts of user types
user_types = df['user_type'].value_counts()
# Display counts of gender
while True:
    try:
        gender_type=df['member_gender'].value_counts()
        break
    except:
        
        break

# Display earliest, most recent, and most common year of birth
while True:
    try:
        common_yob=df['member_birth_year'].mode()[0]
        most_recent_yob=df['member_birth_year'].max()
        earliest_yob=df['member_birth_year'].min()
        break
    except:
        break

ordinal_var_dict = {'day_of_week': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']}

for var in ordinal_var_dict:
    ordered_var = pd.api.types.CategoricalDtype(ordered = True,
                                                categories = ordinal_var_dict[var])
    df[var] = df[var].astype(ordered_var)
```

## (Distribution of trips duration )

> long tail in the distribution in the left graph so we will make a log scale in the right graph ,The log scale graphs show that there is one peak in the distribution of the duration sec. at 600 sec. ,the number of trips increased from 0 to 600 sec. and then decreased from 600 to 2000 sec.


```python
plt.figure(figsize = [20, 5])
# HISTOGRAM ON LEFT: full data without scaling
plt.subplot(1, 2, 1)
binsize = 500
bins = np.arange(0, df['duration_sec'].max()+binsize, binsize)
default_color = sb.color_palette()[0]
plt.hist(data = df, x = 'duration_sec', color = default_color,bins=bins)
plt.xlabel('duration_sec')
plt.ylabel('Number of Trips')
plt.xlim(-500,10000)
plt.title('Distribution for trip durartion (sec.)')

plt.subplot(1, 2, 2)
# log scalling for the distribution of the duration_sec againest requency of trips
binsize = 0.05
bins = 10 ** np.arange(2.4, np.log10(df['duration_sec'].max()) + binsize, binsize)
default_color = sb.color_palette()[0]
plt.hist(data = df, x = 'duration_sec', color = default_color,bins=bins)
plt.xlabel('duration_sec')
plt.ylabel('Number of Trips')
plt.xscale('log')
plt.xticks([500, 1e3, 2e3, 5e3, 1e4], [500, 1000, 2000, 5000, 10000])
plt.xlim(-500,10000)
plt.title('Distribution for trip durartion (sec.) Log scalled')
plt.show()
```


    
![png](output_7_0.png)
    


## (Distribution of age and the relation between age and trips duration )

> From the below graphs , the left graph (Distribution of age) shows that the ages of most subscribers and customers are between 20 to 40 years old that make most frequent trips , and from the right graph ,it shows that the more trips duration is done by by the younger ages, so i can say that the older ages will reduce the trip duration.


```python
plt.figure(figsize = [20, 5])
plt.subplot(1, 2, 1)
# find the distribution of ages
binsize = 1
bins = np.arange(0, df['age'].astype(float).max()+binsize, binsize)
default_color = sb.color_palette()[0]
plt.hist(data = df, x = 'age', color = default_color,bins=bins)
plt.title('Distribution of ages')
plt.xticks(rotation=90);

# show the colleration between the age and duration_sec

plt.subplot(1, 2, 2)
plt.scatter(df['age'], df['duration_sec'], alpha = 0.25 )
plt.xlim([-5, 90])
plt.ylim([500, 7000])
plt.xlabel('Age (years)')
plt.ylabel('Duaration (sec)')
plt.title('Explore the age varable againest the trip duration (sec.)')
plt.show()
```


    
![png](output_9_0.png)
    


## (Distribution of user types , the relation between user types and trips duration, and the relation between user types and both age and trip duration )

> From the below graphs , the left graph (Distribution of user types) shows that the subscriber user type used to make most of the trips , and from the right graph ,it shows that the trip durations spent from customer user type is pretty higher than subscriber user type, so i can say that if we increased the subscriber user type will reduce the trip duration, when we look at the scatter plots that shows the relation between user types and both age and trip duration we can say that subscriber user type has older ages than customer , which reflected on the effect of the trip duration, where if subscriber user type with older age increased the trip duration will decrease , which give us a strong indecation that the combined station or the distance between the start station and end station has a strong effect on trip duration.


```python
plt.figure(figsize = [20, 5])
plt.subplot(1, 2, 1)
#Distribution of user_types
default_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'user_type', color = default_color);
plt.title('Distribution of user type')

#plot a box plot between Categorical variale the user_type and the continous quantitative variable duration_sec
plt.subplot(1, 2, 2)
base_color = sb.color_palette()[1]
sb.boxplot(data = df, x = 'user_type', y = 'duration_sec', color = base_color)
plt.ylim([-10, 2500])
plt.xlabel('User Type')
plt.ylabel('Duration (sec)')
plt.title('The relation between the user type and trip duration (Sec.)')
plt.show()

#Create scatter plot that show the relation between user type and both(age and trip duration (sec.))
user_type = sb.FacetGrid(data = df, col = 'user_type', col_wrap = 2, size = 5,xlim = [10, 90], ylim = [-500, 9000])
user_type.map(plt.scatter, 'age', 'duration_sec', alpha=0.25)
user_type.set_xlabels('Age (year)')
user_type.set_ylabels('Duration (sec)')
##plt.title(' The relation between user type and both(age and trip duration (sec.)')
plt.show()
```


    
![png](output_11_0.png)
    



    
![png](output_11_1.png)
    


## (Distribution of member gender , the relation between member gender and trips duration, and the relation between member gender and both age and trip duration )

>From the below graphs , the left graph (Distribution of member gender) shows that the male gender used to make most of the trips , and from the right graph ,it shows that the trip durations spent from female gender is  higher than male gender, so i can say that if we increased the male gender will reduce the trip duration, when we look at the scatter plots that shows the relation between user types and both age and trip duration we can say that subscriber user type has older ages than customer , which reflected on the effect of the trip duration, where if subscriber user type with older age increased the trip duration will decrease , which give us a strong indecation that the combined station or the distance between the start station and end station has a strong effect on trip duration.



```python
plt.figure(figsize = [20, 5])
plt.subplot(1, 2, 1)
#Distribution of member_gender 
default_color = sb.color_palette()[0]
plt.title('Distribution of Member Gender')
freq=df.member_gender.value_counts()
gen_order=freq.index
sb.countplot(data = df, x = 'member_gender', color = default_color,order=gen_order);

plt.subplot(1, 2, 2)
#plot a box plot between Categorical variale the member_gender and the continous quantitative variable duration_sec
base_color = sb.color_palette()[1]
sb.boxplot(data = df, x = 'member_gender', y = 'duration_sec', color = base_color,order=gen_order)
plt.ylim([-10, 2000])
plt.xlabel('Gender')
plt.ylabel('Duration (sec)')
plt.title('The relation between the member gender and trip duration (Sec.)')
plt.show()

#Create scatter plot that show the relation between member gender and both(age and duration_sec)
gender = sb.FacetGrid(data = df, col = 'member_gender', col_wrap = 2, size = 5,xlim = [10, 90], ylim = [-500, 9000])
gender.map(plt.scatter, 'age', 'duration_sec', alpha=0.25)
gender.set_xlabels('Age (year)')
gender.set_ylabels('Duration (sec)')
#plt.title(' The relation between member gender and both(age and duration_sec)')
plt.show()

```


    
![png](output_13_0.png)
    



    
![png](output_13_1.png)
    


## (Distribution of days of the week , the relation between days of the week and trips duration)

>From the below graphs , the left graph (Distribution of day of the week) shows that the lowest number of trips occured in the week-end (Saturday, Sunday)  , and from the right graph ,it shows that the trip durations in the week-end is  higher than the rest of the days in the week, so i can say that in the week_end the useres used to make long distance trip more than the rest of the week.



```python
plt.figure(figsize = [20, 5])
plt.subplot(1, 2, 1)
# plotting the day of week againest the frequency of trips
default_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'day_of_week', color = default_color);
plt.title('Distribution of day of the week')
plt.xticks(rotation=30);

plt.subplot(1, 2, 2)
#plotting the relation between the day of week and the trip duration
sb.barplot(data=df,x='day_of_week',y='duration_sec',color = default_color);
plt.title('The relation of day of week and the durartion of the trip')
plt.xticks(rotation=30);
```


    
![png](output_15_0.png)
    

