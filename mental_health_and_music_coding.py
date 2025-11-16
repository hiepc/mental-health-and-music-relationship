#DATASET
import pandas as pd

data = pd.read_csv("mxmh_survey_results.csv")

#Age
Age = data["Age"]
print(Age)

#Primary Streaming Service
Primary_Streaming_Service = data["Primary streaming service"]
print(Primary_Streaming_Service)

#Hours Per Day
Hours_Per_Day = data["Hours per day"]
print(Hours_Per_Day)

#While Working
While_Working = data['While working']
print(While_Working)

#Instrumentalist
Instrumentalist = data["Instrumentalist"]
print(Instrumentalist)

#Composer
Composer = data["Composer"]
print(Composer)

#Fav genre
Fav_genre = data["Fav genre"]
print(Fav_genre)

#Exploratory
Exploratory = data["Exploratory"]
print(Exploratory)

#Foreign languages
Foreign_languages = data["Foreign languages"]
print(Foreign_languages)

#BPM
BPM = data["BPM"]
print(BPM)

#Frequency[Classical]
Frequency_Classical = data["Frequency [Classical]"]
print(Frequency_Classical)

#Frequency[Country]
Frequency_Country = data["Frequency [Country]"]
print(Frequency_Country)

#Frequency[EDM]
Frequency_EDM = data["Frequency [EDM]"]
print(Frequency_EDM)

#Frequency[Folk]
Frequency_Folk = data["Frequency [Folk]"]
print(Frequency_Folk)

#Frequency[Gospel]
Frequency_Gospel = data["Frequency [Gospel]"]
print(Frequency_Gospel)

#Frequency[Hip hop]
Frequency_Hip_hop = data["Frequency [Hip hop]"]
print(Frequency_Hip_hop)

#Frequency[Jazz]
Frequency_Jazz = data["Frequency [Jazz]"]
print(Frequency_Jazz)

#Frequency[K pop]
Frequency_K_pop = data["Frequency [K pop]"]
print(Frequency_K_pop)

#Frequency[Latin]
Frequency_Latin = data["Frequency [Latin]"]
print(Frequency_Latin)

#Frequency[Lofi]
Frequency_Lofi = data["Frequency [Lofi]"]
print(Frequency_Lofi)

#Frequency[Metal]
Frequency_Metal = data["Frequency [Metal]"]
print(Frequency_Metal)

#Frequency[Pop]
Frequency_Pop = data["Frequency [Pop]"]
print(Frequency_Pop)

#Frequency[R&B]
Frequency_RNB = data["Frequency [R&B]"]
print(Frequency_RNB)

#Frequency[Rap]
Frequency_Rap = data["Frequency [Rap]"]
print(Frequency_Rap)

#Frequency[Rock]
Frequency_Rock = data["Frequency [Rock]"]
print(Frequency_Rock)

#Frequency[Video game music]
Frequency_VGM = data["Frequency [Video game music]"]
print(Frequency_VGM)

#Anxiety
anxiety = data["Anxiety"]
print(anxiety)

#Depression
depression = data["Depression"]
print(depression)

#Insomnia
insomnia = data["Insomnia"]
print(insomnia)

#OCD
OCD = data["OCD"]
print(OCD)

#Music effects
music_effects = data["Music effects"]
print(music_effects)

#LOOPS AND CONDITIONALS

for BPM in BPM  :
    if BPM > 0:
        print(BPM)
        
for music_effects in music_effects:
    if music_effects == "Improve":
        print(music_effects)
    elif music_effects == "Worsen":
        print(music_effects)
    

#Dorcas Bola, Alice Rancu, Olivia Leiva, Carole Hiep
# Extract data and observe the data in a graph

#<<<<<<< HEAD
#------------------------------------------------------------------------------------
##array using different colors and line styles

#=======
#1 plot of any type containing data from more than 1 array using different 
#colors and line styles

import pandas as pd
import matplotlib.pyplot as plt

x = Hours_Per_Day
y1 = anxiety
y2 = depression
width = 0.16

plt.bar(x - width, y1, width, color='skyblue', label='anxiety', hatch='dotted')
plt.bar(x + width, y2, width, color='salmon', label='depression', hatch='\\')

# Add labels
plt.xlabel('Hours of Music Listened per Day')
plt.ylabel('Mental Health Conditions Rated from 1-10')
plt.title('Self-Reporded Mental Health Conditions Based on Hours of Music Listened per Day')
plt.legend()
plt.show()
#<<<<<<< HEAD
#Comment explination: This is a bar plot containing data from anxiety and depression. 
#It shows how anxiety and depression are affected depending on the hours of music.
#Anxiety and depression are differentiated by colors and design.

#------------------------------------------------------------------------------------

##histogram

#Comment: This is a bar plot containing data from anxiety and depression. 
#It shows how anxiety and depression are affected depending on the hours of music.
#Anxiety and depression are differentiated by colors and design.

#histogram

import pandas as pd
import matplotlib.pyplot as plt

x = insomnia
plt.title("Self-Reported Insomnia")
#<<<<<<< HEAD
plt.xlabel("Insomnia on a scale from 1-10")
plt.ylabel("Number of reported cases")
plt.hist(x)
plt.show()
#Comment explination: This plot represents the number of responses to having insomnia and putting it on a 
#scale from 1-10 to see how many reported cases are high and low in insomnia cases.

plt.xlabel("Insomnia on a Scale from 1-10")
plt.ylabel("Number of Participants")
plt.hist(x)
plt.show()
#Comment: Each participant have to rate their insomnia on a scale from 1-10. 
#This plot (historgram) displays the frequency of each rating. 


#------------------------------------------------------------------------------------


##scatter plot
#=======
#scatter plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('mxmh_survey_results.csv')


print(data.describe())

#<<<<<<< HEAD
#sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
#=======
#<<<<<<< Updated upstream


sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")

#>>>>>>> e185ceedd278cb7e5044274aede013cfe2876db2

g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
plt.title("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Hours per day")
g.fig.suptitle("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)

#Comment explination: This plot represents the number of hours listened to daily based off of the age group
#as well as if there are any effects whatsoever on peope if they are improvements, if they worsen or if there is no change.

#------------------------------------------------------------------------------------

##pie plot
import matplotlib.pyplot as plt



g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)
#=======

print(data["Frequency [Classical]"].value_counts())

g.fig.suptitle("")
g = sns.relplot()

plt.title("The frequency listened to Classical music")

plt.pie(data["Frequency [Classical]"].value_counts(), labels=["Rarely", "Sometimes", "Never", "Very Frequently"] )
plt.show()
#Comment explanation: This plot represents the amout of times(frequency) someone listens to a specific genre (classical)
# it is split into four categories rarely (the biggest area), sometimes (the second biggest), never (second smallest) and very frequently (the smallest).

#------------------------------------------------------------------------------------

##bar plot
#explanation: To make the bar plot of the hours per day of listenning to music by the different streaming services, we first calculated their own individual mean then repsted the plot with bars.
import pandas as pd

spotify_user = data[data['Primary streaming service'] == 'Spotify']
mean_hours_per_day_s = spotify_user['Hours per day'].mean()
print('Mean of Spotify users:', mean_hours_per_day_s)

apple_music_user = data[data['Primary streaming service'] == 'Apple Music']
mean_hours_per_day_a = apple_music_user['Hours per day'].mean()
print('Mean of Apple Music users:', mean_hours_per_day_a)

youtube_music_user = data[data['Primary streaming service'] == 'YouTube Music']
mean_hours_per_day_y = youtube_music_user['Hours per day'].mean()
print('Mean of YouTube Music users:', mean_hours_per_day_y)

pandora_user = data[data['Primary streaming service'] == 'Pandora']
mean_hours_per_day_p = pandora_user['Hours per day'].mean()
print('Mean of Pandora users:', mean_hours_per_day_p)

no_streaming_service_user = data[data['Primary streaming service'] == 'I do not use a streaming service.']
mean_hours_per_day_i = no_streaming_service_user['Hours per day'].mean()
print('Mean of no streaming services:', mean_hours_per_day_i)

#Comment: In this scatter plot, each dot represents a single observation. 
#This plot allows us to determine if there's a relationship between the age of a person and the number of hours of music listened in a day.

import matplotlib.pyplot as plt

Streaming_service = ['Spotify', 'Pandora', 'YouTube Music', 'Apple Music', 'None']
Means_of_hours_per_day = [3.8373, 2.1364, 3.2207, 3.5588, 2.9542]

plt.bar(Streaming_service, Means_of_hours_per_day, color = 'hotpink')
plt.title('Streaming service by Hours per day')
plt.xlabel('Streaming service')
plt.ylabel('Hours per day')
plt.show()

#------------------------------------------------------------------------------------

##grid plot
#explanation: This plot uses a data sample of the age of the participants by their auto-evaluation of the level of their different mental disorder: anxiety, insomnia, depression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('mxmh_survey_results.csv')
data_sample= data.sample(100)

print(data_sample['Age'],data_sample['Anxiety'].describe())


plt.scatter(data_sample['Age'],data_sample['Anxiety'], color ='green')
plt.scatter(data_sample['Age'],data_sample['Depression'], color ='pink')
plt.scatter(data_sample['Age'],data_sample['Insomnia'], color ='red')

plt.title('The mental health by the age')
plt.ylabel('Mental health')
plt.xlabel('Age')


plt.plot(data_sample['Age'] ,data_sample['Anxiety'], linestyle = '')
plt.legend()
plt.grid()
plt.show()

#------------------------------------------------------------------------------------

##one plot two subplots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('mxmh_survey_results.csv')

fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(14,6))

#right subplot
sns.countplot(data = data, x = "Music effects", ax = ax1, palette=["blue", "red", "green"], order= data["Music effects"].value_counts().index)
ax1.set_title("Distribution of Music Effects on Mental Health", fontsize=13, fontweight="bold")
ax1.set_xlabel("Music Effect", fontsize=11)
ax1.set_ylabel("Meantal Health", fontsize=11)

#left subplot
mental_health_columns = ["Anxiety", "Depression", "Insomnia", "OCD"]
melted_data = data.melt(id_vars="Music effects", value_vars=mental_health_columns, var_name="Condition", value_name="Score")

sns.barplot(data=melted_data, x="Condition", y="Score", hue="Music effects", ax=ax2, palette=["cyan", "pink", "purple"])
ax2.set_title("Average Mental Health Scores by Music Effect", fontsize=13, fontweight="bold")
ax2.set_xlabel("Mental Health condition", fontsize=11)
ax2.set_ylabel("Average Score (0-10 scale)", fontsize=11)
ax2.legend(title="Music Effect")

plt.show()
#comment explination: The right bar plot represents the count of respondents by music effects whether they improved, had no effect or worsened
#The left bar plot represents the average scores of anxiety, depression, insomnia and OCD grouped by music effects whether they improved, had no effect or worsened
#How this helps is that it shows both the distribution of perceived music effects and how they correlate with mental health scores.

#------------------------------------------------------------------------------------


g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)


g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)

#------------------------------------
#-------------------------------------
#------------------------------------
#2. PRELIMINARY STEPS (DELIVERABLE 3) by Alice

#a) Initial data inspection:
print(data.describe())
# gives out the mean, count (736 participants), std, minimum value for each column, maximum value for each column and the values in between.
print(data.head())
# It is useful to see quickly how the data table is presented for the entire dataset but only displaying the first 5 rows.
print(data.tail())
# Same thing as data.head() but instead of the first 5 rows, the last 5 rows are presented. It is useful to analyse if the dataset shows some variation going through the first rows and the last rows or if the dataset is all randomly dispersed.
print(data.info())
# info() function helps with seeing how many empty values we have in each columns and also the type of data we have: either float or object. 
# We can also see that there is a total of 33 columns with 736 entries, going from 0 to 735. That means there is a total of 736 participants who answered the questionnaire.


#b) Handle duplicate entries: identify duplicate rows + remove them
print(data.duplicated())
# there is no duplicate in sight so no need to use the function drop_duplicates()


#c) Identify and manage missing values:
    
print(data.isnull())
#there is 8 missing values for music effects, 107 missing values for BPM, 4 missing values for foreigh languages, 1 missing value for composer, 4 missing value for instrumentalist, 3 missinng values for listening to music while working, 1 missing value for primary streaming service used and 1 last missing value for age.
#now, we fill in missing values with mean for the columns concerned (only numerical) and fill in missing values with the most common answer with the function mode() for categorical values.
#MEAN = preferred for normally distributed data


#fill categorical value: use MODE, the most common answer used to answer the effects of music (improve, no effect, etc.)
data['Music effects'] = data['Music effects'].fillna(data['Music effects'].mode()[0])
#use fillna() to fill the missing values for foreign language too with its mode(), since its yes / no answers
data['Foreign languages'] = data['Foreign languages'].fillna(data['Foreign languages'].mode()[0])


# same thing for the 1 missing value for composer (categorical value) and 4 missing values for instrumentalists column, 3 missing values for listening to music while working and 1 missing value for primary streaming service used (all categorical = used MODE function)
data['Composer'] = data['Composer'].fillna(data['Composer'].mode()[0])
data['Instrumentalist'] = data['Instrumentalist'].fillna(data['Instrumentalist'].mode()[0])
data['While working'] = data['While working'].fillna(data['While working'].mode()[0])
data['Primary streaming service'] = data['Primary streaming service'].fillna(data['Primary streaming service'].mode()[0])

#to fill NUMERICAL values, now use the mean (like for BPM and age, which are NUMERICAL values)
data['BPM'] = data['BPM'].fillna(data['BPM'].mean())
data['Age'] = data['Age'].fillna(data['Age'].mean())

print(data.isnull().sum())
#now all the missing values were either categorical = used mode, or numerical = used mean to fill them.


#d) Correct data types and formats: convert TIMESTAMP column to the appropriate data type: interger using pd.to_datetime() function.
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
print(data['Timestamp'].dtype)

#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#3) Univariate non-graphical EDA (LIA 3)

#Numerical: mean, median, mode, standard deviation, variance, skewness, kurtosis and quartiles 

numerical = data.select_dtypes(include=['float64'])
print("Mean:")
print(numerical.mean())
print("Median:")
print(numerical.median())
print("Mode:")
print(numerical.mode()) 
print("STD:")
print(numerical.std())
print("Variance:")
print( numerical.var())
print( "Skewness:")
print( numerical.skew())
print("Kurtosis:")
print(numerical.kurt())
print( "Quartiles:")
print( numerical.quantile([0.25,0.5,0.75]))

#Categorical：frequency counts, proportion, mode (most frequent category and the number of unique categories)
categorical = data.select_dtypes(include=['object'])
print("Frequency and Proportions:")
for col in categorical:
   print(categorical[col].value_counts(dropna=False))
   print(categorical[col].value_counts(normalize=True))
print("Mode:")
print(categorical.mode())
print(categorical.nunique())
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#4. Univariate graphical EDA (LIA 3)
#basic theme
sns.set_theme()
#A) Basic histogram with custom bins
#
sns.histplot(data=data, x= "Age", bins=5)
sns.histplot(data=data, x= "Age", bins=15)
sns.histplot(data=data, x= "Age", bins=20)
plt.title("Title", fontsize=12, fontweight='bold')
plt.xlabel("x")
plt.ylabel("y")
#
sns.histplot(data=data, x= "BPM", bins=5)
sns.histplot(data=data, x= "BPM", bins=15)
sns.histplot(data=data, x= "BPM", bins=20)
plt.title("Title2", fontsize=12, fontweight='bold')
plt.xlabel("x")
plt.ylabel("y")
#
sns.histplot(data=data, x= "Hours per day", bins=5)
sns.histplot(data=data, x= "Hours per day", bins=15)
sns.histplot(data=data, x= "Hours per day", bins=20)
#Change the title:
g.fig.suptitle("")
plt.title("Title3", fontsize=12, fontweight='bold')
plt.xlabel("x")
plt.ylabel("y")

#B) using conditioning on other variables (proposition)
#sns.scatterplot(data=data, x="Age", y="Hours per day", hue="Depression")
#plt.title("Scatterplot showing the depression levels in the relationship between the age and the amount of hours listening to music per day")
#plt.show()

#--------------------------------------------------------------
#---------------------------------------------------------------
#-------------------------------------------------------------
#5. Multivariate non-graphical EDA  (LIA 3)

#Relationship between being an instrumentalist and effect of music on mental health (improve or worsen)
print(pd.crosstab(categorical["Instrumentalist"],categorical["Music effects"], normalize=True))





#Relationship between being an instrumentalist and effect of music on mental health (improve or worsen)
print(pd.crosstab(categorical["Instrumentalist"],categorical["Music effects"], normalize=True))


#Relationship between listeners who love to exlore new genres/artists and listeners who regularly listen to music in foreign languages
print(pd.crosstab(categorical["Exploratory"],categorical["Foreign languages"], normalize=True))



#Relationship between being an instrumentalist and effect of music on mental health (improve or worsen)
print(pd.crosstab(categorical["Instrumentalist"],categorical["Music effects"], normalize=True))


#Relationship between listeners who love to exlore new genres/artists and listeners who regularly listen to music in foreign languages
print(pd.crosstab(categorical["Exploratory"],categorical["Foreign languages"], normalize=True))



#Relationship between being a composer and favourite genre of music
pd.set_option('display.max_columns', None)
print(pd.crosstab(categorical["Composer"],categorical["Fav genre"], normalize=True))

#Relationship between music genres and effect on mental health (improve or worsen)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(pd.crosstab([categorical["Frequency [Classical]"], categorical["Frequency [Country]"],categorical["Frequency [EDM]"]],categorical["Music effects"],normalize="index"))

#--------------------------------------------------------------
#---------------------------------------------------------------
#-------------------------------------------------------------
#6. Multivariate graphical EDA

#6.1.Visualizing statistical relationships (5 plots): (using SEABORN)

    
#a) 1 plot using Faceting feature (col parameter in the relplot() function)
h = sns.relplot(data=data, y="Hours per day", x="While working", hue="Age", col="Music effects")
h.fig.suptitle("Title: Hours per day listened to music while working or not: (age group and the benefits from it)", fontsize=12, fontweight='bold')
h.fig.subplots_adjust(top=0.85)

#b) 1 plot representing 5 variables at once (x, y, hue, size, col): 

w = sns.relplot(data=data, y="Music effects", x="Hours per day", hue="Age", size="Instrumentalist", col="While working")
w.fig.suptitle("Title: Music effects based on the amount of hours per day listening to music (instrumentalists + if participants listen or not to music while working)", fontsize=12, fontweight='bold')
w.fig.subplots_adjust(top=0.85)
#c) 1 plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
z = sns.relplot(data=data, y="Depression", x="Insomnia", kind="line", hue="Music effects",col="Music effects")
z.fig.suptitle("Title: The depression level based on insomnia with the effects of music")
z.fig.subplots_adjust(top=0.85)
# We chose the level of insomnia and the level of depression as continuous variables since they both increase and decrease with one another. They vary from 0 to 10, 0 being low insomnia and 10 being high insomnia (same thing for depression). 
#Also, based on the music effects,it is possible to see that there is higher level of insomnia, therefore higher level of depression when participants feel like the effects have worsen after listening to music. 


#d) 1 plot illustrating standard deviation



#e) 1 plot including a linear regression











