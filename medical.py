#Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sms

df = pd.read_csv('nsa.csv')
#Changine panda dataframe display settings to help understand the database

pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)
pd.set_option('display.precision',2)


#Exploring the data

#print(df.describe())
#print(df.shape)
#print(len(df))
#print(df.head())
#print(df.info)
#print(df.isnull().sum(axis=0))
#print(df.duplicated())

#Notes from exploring:

#minimum age is -1 and some ages are plain 0
#handcap ranges from 0 to 4 when it should represent a 0,1 boolean statement
#Patient ID,Appointment ID columns are nonvital
#appointment day needs to be cleaned nonvital hour data
#schedueled day has a nonvital default time of zero
#some schedueled days are in the past, which is ofcourse a mistake
#some rows in 'Neighbourhoood column are not fully in english'


#Data Wrangling

#adjusting the age and handcap values
df.loc[df['Age']<1,'Age']=1

df.loc[df['Handcap']>1,'Handcap']=1

df['Neighbourhood'] = df["Neighbourhood"].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))


#I was intending to make a relation between the
#duration between the appointment day and scheduled day but couldnt finish it due
#to the lack of time

#getting rid of nonvital time data inside both appointment-day and schedueled-day
# listx=[]
# for x in range(len(df)):
# 	listx.append(df.loc[x,'ScheduledDay'][:len('0000-00-00')])
# df['ScheduledDay'] = listx
# df['ScheduledDay']=pd.to_datetime(df['ScheduledDay'])

# listy=[]
# for y in range(len(df)):
# 	listy.append(df.loc[y,'AppointmentDay'][:len('0000-00-00')])
# df['AppointmentDay']= listy
# df['AppointmentDay']=pd.to_datetime(df['AppointmentDay'])

#creating a new time to appointment column
#df['TimeToAppointment'] = (df['AppointmentDay']-df['ScheduledDay']).dt.days


#deleting nonvital patientId, appointmentID and gender columns
df.drop('PatientId',axis =1,inplace=True)
df.drop('AppointmentID',axis=1,inplace=True)
df.drop('Gender',axis=1,inplace=True)



#Visualizing
fig,ax=plt.subplots(4,2)

#1-AGE: 

#turning the no-show boolean values into 0,1 so we can multiply with years before summing
df.loc[df['No-show']=='Yes',['No-show']]=1
df.loc[df['No-show']=='No',['No-show']]=0

#This approach creates filtered columns for each case
#And then multiply the age with the integer value
#of the boolean 'no-show'
onethrty=((df['Age'][df['Age']<=30][df['Age']>0]*df['No-show']).dropna()>0).sum()
thrtysixty=((df['Age'][(df['Age']<=60)][df['Age']>30]*df['No-show']).dropna()>0).sum()
sixtyninty=((df['Age'][(df['Age']<=90)][df['Age']>60]*df['No-show']).dropna()>0).sum()
nintyonetw=((df['Age'][(df['Age']<=120)][df['Age']>90]*df['No-show']).dropna()>0).sum()

#plotting solely;each sum as an individual value in a collective bar plot
ranges=['30','60','90','120']
ages=[onethrty,thrtysixty,sixtyninty,nintyonetw]
ax[0,0].bar(ranges,ages)
ax[0,0].set_title('Age range & not showing up')

#2-Neighbourhood:

df['YesNeighbourhood'] = np.where(df['No-show']==1, df['Neighbourhood'], None)
ax[0,1].bar(df['YesNeighbourhood'].value_counts()[1:4].index,df['YesNeighbourhood'].value_counts()[1:4])
ax[0,1].set_title('Neighbourhood & not showing up')

#3-Scholarship,Diseases and recieving an SMS
df['YesScholarship']=np.where(df['No-show']==1, df['Scholarship'], None)
df.loc[df['YesScholarship']==1,['YesScholarship']]='No'
df.loc[df['YesScholarship']==0,['YesScholarship']]='Yes'
ax[1,0].bar(df['YesScholarship'].value_counts().index,df['YesScholarship'].value_counts())
ax[1,0].set_title('Scholarship and Showing Up')

df['YesHipertension']=np.where(df['No-show']==1, df['Hipertension'], None)
df.loc[df['YesHipertension']==1,['YesHipertension']]='No'
df.loc[df['YesHipertension']==0,['YesHipertension']]='Yes'
ax[1,1].bar(df['YesHipertension'].value_counts().index,df['YesHipertension'].value_counts())
ax[1,1].set_title('Hipertension and Showing up')

df['YesDiabetes']=np.where(df['No-show']==1, df['Diabetes'], None)
df.loc[df['YesDiabetes']==1,['YesDiabetes']]='No'
df.loc[df['YesDiabetes']==0,['YesDiabetes']]='Yes'
ax[2,0].bar(df['YesDiabetes'].value_counts().index,df['YesDiabetes'].value_counts())
ax[2,0].set_title('Diabetes and Showing up')

df['YesAlcoholism']=np.where(df['No-show']==1, df['Alcoholism'], None)
df.loc[df['YesAlcoholism']==1,['YesAlcoholism']]='No'
df.loc[df['YesAlcoholism']==0,['YesAlcoholism']]='Yes'
ax[2,1].bar(df['YesAlcoholism'].value_counts().index,df['YesAlcoholism'].value_counts())
ax[2,1].set_title('Alcoholism and showing up')

df['YesHandcap']=np.where(df['No-show']==1, df['Handcap'], None)
df.loc[df['YesHandcap']==1,['YesHandcap']]='No'
df.loc[df['YesHandcap']==0,['YesHandcap']]='Yes'
ax[3,0].bar(df['YesHandcap'].value_counts().index,df['YesHandcap'].value_counts())
ax[3,0].set_title('Handcap and Showing up')

df['YesSMS_received']=np.where(df['No-show']==1, df['SMS_received'], None)
df.loc[df['YesSMS_received']==1,['YesSMS_received']]='No'
df.loc[df['YesSMS_received']==0,['YesSMS_received']]='Yes'
ax[3,1].bar(df['YesSMS_received'].value_counts().index,df['YesSMS_received'].value_counts())
ax[3,1].set_title('Recieving SMS and Showing up')



fig.tight_layout()

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
