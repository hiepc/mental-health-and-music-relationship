#DATASET
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

print(data.describe())

sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")

#>>>>>>> e185ceedd278cb7e5044274aede013cfe2876db2

g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
plt.title("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Hours per day")
g.fig.suptitle("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)
plt.show()
#Comment explination: This plot represents the number of hours listened to daily based off of the age group
#as well as if there are any effects whatsoever on peope if they are improvements, if they worsen or if there is no change.

#------------------------------------------------------------------------------------

##pie plot

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

fig, axs = plt.subplots(1, 2, figsize=(14,6))

#right subplot
axs[0].bar(data["Fav genre"], data["Anxiety"])
axs[0].set_title("Anxiety Levels by Genre", fontsize=13, fontweight="bold")
axs[0].set_xlabel("Genre", fontsize=11)
axs[0].set_ylabel("Anxiety Score", fontsize=11)
axs[0].tick_params(axis="x", rotation=90) #This is used to rotate the x axis labes so that it is clear and not one on top of each other

#left subplot
axs[1].bar(data["Fav genre"], data["Depression"])
axs[1].set_title("Depression Levels by Genre", fontsize=13, fontweight="bold")
axs[1].set_xlabel("Genre", fontsize=11)
axs[1].set_ylabel("Depression score", fontsize=11)
axs[1].tick_params(axis="x", rotation=90) #This is used to rotate the x axis labes so that it is clear and not one on top of each other

plt.show()
#comment explination: This graph is comparing anxiety and depression levels across different music genres.
#It lists the same set of genres for both anxiety and depression with the side by side comparidon of how each
# genre realtes to the two mental health states. It aims to show which genre is associated with high/low levels of mental illnesses.

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
sns.histplot(data=data, x= "Age", multiple="stack", bins=5)
sns.histplot(data=data, x= "Age", multiple="stack", bins=15)
sns.histplot(data=data, x= "Age", multiple="stack", bins=20)
g.fig.suptitle("")
plt.title("Age Demographics of listeners and Music's Impact", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "BPM", bins=5)
sns.histplot(data=data, x= "BPM", bins=15)
sns.histplot(data=data, x= "BPM", bins=20)
#Change the title:
g.fig.suptitle("")
plt.title("Frequency of Beats Per Minute in Music Library", fontsize=12, fontweight='bold')
plt.xlabel("BPM")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Anxiety", bins=5)
sns.histplot(data=data, x= "Anxiety", bins=15)
sns.histplot(data=data, x= "Anxiety", bins=20)
g.fig.suptitle("")
plt.title("Distribution of Self-Reported Anxiety Scores", fontsize=12, fontweight='bold')
plt.xlabel("Anxiety")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Depression", bins=5)
sns.histplot(data=data, x= "Depression", bins=15)
sns.histplot(data=data, x= "Depression", bins=20)
g.fig.suptitle("")
plt.title("Distribution of Self-Reported Depression Scores", fontsize=12, fontweight='bold')
plt.xlabel("Depression")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Insomnia", bins=5)
sns.histplot(data=data, x= "Insomnia", bins=15)
sns.histplot(data=data, x= "Insomnia", bins=20)
g.fig.suptitle("")
plt.title("Distribution of Self-Reported Insomnia Scores", fontsize=12, fontweight='bold')
plt.xlabel("Insomnia")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "OCD", bins=5)
sns.histplot(data=data, x= "OCD", bins=15)
sns.histplot(data=data, x= "OCD", bins=20)
g.fig.suptitle("")
plt.title("Distribution of Self-Reported OCD Scores", fontsize=12, fontweight='bold')
plt.xlabel("OCD")
plt.ylabel("Count")
plt.show()

#B) using conditioning on other variables (proposition)
##Age
#Anxiety
sns.scatterplot(data=data, x="Age", y="Hours per day", hue="Anxiety")
plt.title("Scatterplot showing the anxiety levels in the relationship between the age and the amount of hours listening to music per day")
plt.show()
#Depression
sns.scatterplot(data=data, x="Age", y="Hours per day", hue="Depression")
plt.title("Scatterplot showing the depression levels in the relationship between the age and the amount of hours listening to music per day")
plt.show()
#Insomnia
sns.scatterplot(data=data, x="Age", y="Hours per day", hue="Insomnia")
plt.title("Scatterplot showing the insomnia levels in the relationship between the age and the amount of hours listening to music per day")
plt.show()
#OCD
sns.scatterplot(data=data, x="Age", y="Hours per day", hue="OCD")
plt.title("Scatterplot showing the OCD levels in the relationship between the age and the amount of hours listening to music per day")
plt.show()

##BPM
#Anxiety
sns.scatterplot(data=data, x="BPM", y="Hours per day", hue="Anxiety")
plt.title("Scatterplot showing the anxiety levels in the relationship between the BPM and the amount of hours listening to music per day")
plt.show()
#Depression
sns.scatterplot(data=data, x="BPM", y="Hours per day", hue="Depression")
plt.title("Scatterplot showing the depression levels in the relationship between the BPM and the amount of hours listening to music per day")
plt.show()
#Insonmnia
sns.scatterplot(data=data, x="BPM", y="Hours per day", hue="Insomnia")
plt.title("Scatterplot showing the insomnia levels in the relationship between the BPM and the amount of hours listening to music per day")
plt.show()
#OCD
sns.scatterplot(data=data, x="BPM", y="Hours per day", hue="OCD")
plt.title("Scatterplot showing the OCD levels in the relationship between the BPM and the amount of hours listening to music per day")
plt.show()

#C) Stacked histogram
#
sns.histplot(data=data, x= "Age", multiple="stack")
sns.histplot(data=data, x= "Age", multiple="stack")
sns.histplot(data=data, x= "Age", multiple="stack")
g.fig.suptitle("")
plt.title("Age Distribution", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "BPM", multiple="stack")
sns.histplot(data=data, x= "BPM", multiple="stack")
sns.histplot(data=data, x= "BPM", multiple="stack")
#Change the title:
g.fig.suptitle("")
plt.title("BPM Distribution", fontsize=12, fontweight='bold')
plt.xlabel("BPM")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Anxiety", multiple="stack")
sns.histplot(data=data, x= "Anxiety", multiple="stack")
sns.histplot(data=data, x= "Anxiety", multiple="stack")
g.fig.suptitle("")
plt.title("Anxiety Score Distribution", fontsize=12, fontweight='bold')
plt.xlabel("Anxiety")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Depression", multiple="stack")
sns.histplot(data=data, x= "Depression", multiple="stack")
sns.histplot(data=data, x= "Depression", multiple="stack")
g.fig.suptitle("")
plt.title("Depression Score Distribution", fontsize=12, fontweight='bold')
plt.xlabel("Depression")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "Insomnia", multiple="stack")
sns.histplot(data=data, x= "Insomnia", multiple="stack")
sns.histplot(data=data, x= "Insomnia", multiple="stack")
g.fig.suptitle("")
plt.title("Insomnia Score Distribution", fontsize=12, fontweight='bold')
plt.xlabel("Insomnia")
plt.ylabel("Count")
plt.show()
#
sns.histplot(data=data, x= "OCD", multiple="stack")
sns.histplot(data=data, x= "OCD", multiple="stack")
sns.histplot(data=data, x= "OCD", multiple="stack")
g.fig.suptitle("")
plt.title("OCD Score Distribution", fontsize=12, fontweight='bold')
plt.xlabel("OCD")
plt.ylabel("Count")
plt.show()

#D) Dodge bars
sns.displot(data=data, x="Age", hue="Anxiety", multiple="dodge")
g.fig.suptitle("")
plt.title("Axiety Score by Age Group", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="Depression", multiple="dodge")
g.fig.suptitle("")
plt.title("Depression Score by Age Group", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="Insomnia", multiple="dodge")
g.fig.suptitle("")
plt.title("Insomnia Score by Age Group", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="OCD", multiple="dodge")
g.fig.suptitle("")
plt.title("OCD Score by Age Group", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
#E) Normalized histogram statistics
sns.displot(data=data, x="Age", hue="Anxiety", stat= "density", common_norm=False)
g.fig.suptitle("")
plt.title("Axiety Score Destribution by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="Depression", stat= "density", common_norm=False)
g.fig.suptitle("")
plt.title("Depression Score Destribution by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="Insomnia",stat= "density", common_norm=False)
g.fig.suptitle("")
plt.title("Insomnia Score Destribution by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.displot(data=data, x="Age", hue="OCD",stat= "density", common_norm=False)
g.fig.suptitle("")
plt.title("OCD Score Destribution by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
#F) Kernel density estimation (choosing the smooth bandwidth)
##Age
sns.displot(data=data, x="Age", kind="kde", bw_adjust=.5)
g.fig.suptitle("")
plt.title("Age Distribution of Participants", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
##Anxiety
sns.displot(data=data, x="Anxiety", kind="kde", bw_adjust=.5)
g.fig.suptitle("")
plt.title("Density of Anxiety Scores in The Population", fontsize=12, fontweight='bold')
plt.xlabel("Anxiety")
plt.ylabel("Count")
plt.show()
##Depression
sns.displot(data=data, x="Depression", kind="kde", bw_adjust=.5)
g.fig.suptitle("")
plt.title("Density of Depression Scores in The Population", fontsize=12, fontweight='bold')
plt.xlabel("Depression")
plt.ylabel("Count")
plt.show()
##Insomnia
sns.displot(data=data, x="Insomnia", kind="kde", bw_adjust=.5)
g.fig.suptitle("")
plt.title("Density of Insomnia Scores in The Population", fontsize=12, fontweight='bold')
plt.xlabel("Insomnia")
plt.ylabel("Count")
plt.show()
##OCD
sns.displot(data=data, x="OCD", kind="kde", bw_adjust=.5)
g.fig.suptitle("")
plt.title("Density of OCD Scores in The Population", fontsize=12, fontweight='bold')
plt.xlabel("OCD")
plt.ylabel("Count")
plt.show()

#G) Empirical cumulative distributions
##Hours per day
sns.displot(data=data, x="Age", hue= "Hours per day",kind="ecdf")
g.fig.suptitle("")
plt.title("Daily Music Listening Hours by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
##Anxiety
sns.displot(data=data, x="Age", hue= "Anxiety",kind="ecdf")
g.fig.suptitle("")
plt.title("Anxiety Levels by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
##Depression
sns.displot(data=data, x="Age", hue= "Depression",kind="ecdf")
g.fig.suptitle("")
plt.title("Depression Levels by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
##Insomnia
sns.displot(data=data, x="Age", hue= "Insomnia",kind="ecdf")
g.fig.suptitle("")
plt.title("Insomnia Levels by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
##OCD
sns.displot(data=data, x="Age", hue= "OCD",kind="ecdf")
g.fig.suptitle("")
plt.title("OCD Levels by Age", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
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

    
#a) 1 plot using Faceting feature (col parameter in the catplot() function)
h = sns.catplot(data=data, y="Hours per day", x="Music effects", hue="Composer", kind="bar", col="While working")
h.fig.suptitle("Title: Hours per day listened to music while working or not, including the benefits from it", fontsize=12, fontweight='bold')
h.fig.subplots_adjust(top=0.85)

#b) 1 plot representing 5 variables at once (x, y, hue, kind, col): 
w = sns.catplot(data=data, x="Music effects", y="Hours per day", hue="Instrumentalist", kind="bar", col="While working")
w.fig.suptitle("Title: Music effects based on the amount of hours per day listening to music (instrumentalists + if participants listen or not to music while working)", fontsize=12, fontweight='bold')
w.fig.subplots_adjust(top=0.85)

#c) 1 plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
z = sns.relplot(data=data, y="Depression", x="Insomnia", kind="line", hue="Music effects",col="Music effects")
z.fig.suptitle("Title: The depression level based on insomnia with the effects of music")
z.fig.subplots_adjust(top=0.85)
# We chose the level of insomnia and the level of depression as continuous variables since they both increase and decrease with one another. They vary from 0 to 10, 0 being low insomnia and 10 being high insomnia (same thing for depression). 
#Also, based on the music effects,it is possible to see that there is higher level of insomnia, therefore higher level of depression when participants feel like the effects have worsen after listening to music. 


#d)1 plot illustrating standard deviation
#
plt.figure(figsize=(8,5))
sns.lineplot(data=data, x="Age", y="Insomnia", ci="sd")
plt.title("Insomnia by Age with Standard Deviation")

# e) 1 plot including a linear regression
# most peole who say to ahve anxiety are between thee age oge of 10 and 40 and aare not instrumentalsite
e = sns.lmplot(data=data, x="Age", y="Anxiety", hue="Instrumentalist")
e.fig.suptitle("Linear Regression: Anxiety vs Hours Per Day by Instrumentalist Status")
plt.show()

#6.2.Visualizing categorical data (10 plots):
# a) 1 categorical scatter plot with jitter enabled
sns.stripplot(data=data, x="Depression", y="Fav genre", jitter=True, hue='Composer' )
plt.title("Depression Distribution by Genre (Jitter Enabled)")
plt.show()

# b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
sns.stripplot(data=data, x="Music effects", y="OCD", jitter=False, hue='While working')
plt.title("Anxiety Levels by Composer Status (No Jitter)")
plt.show()

# c) 1 “beeswarm” plot representing 3 variables
sns.swarmplot(data=data, x="Depression", y="Fav genre", hue="Foreign languages")
plt.title("Anxiety by Genre and Instrumentalist Status (Beeswarm)")
plt.show()

# d) 1 box plot representing 3 variables
sns.boxplot(data=data, x="Anxiety", y="Hours per day", hue="Exploratory")
plt.title("Depression by Genre and Instrumentalist (Box Plot)")
plt.show()

# e) 1 box plot showing the shape of the distribution (boxenplot())
sns.boxenplot(data=data, x='Music effects', y="Anxiety", hue='Instrumentalist')
plt.title("Distribution Shape of Anxiety Scores Across Genres (Boxenplot)")
plt.xticks(rotation=45)
plt.show()

# f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization
sns.violinplot(data=data, x="Instrumentalist", y="Depression", hue="Composer", split=True, bw=0.3)
plt.title("Depression by Genre Split by Composer Status (Violin Plot)")
plt.show()


# g) 1 violin plot with scatter points inside the violin shapes
sns.violinplot( data=data, x="Composer", y="Anxiety", inner=None)
sns.stripplot(data=data, x="Composer", y="Anxiety", color="pink", size=4, jitter=True, alpha=0.5)
plt.title("Anxiety Distribution for Instrumentalists with Scatter Overlay")
plt.show()


# h) 1 bar plot representing 3 variables showing 97% confidence intervals
sns.barplot(data=data, x="Fav genre", y="Depression",hue="Instrumentalist",ci=97)
plt.title("Depression Across Genres with 97% Confidence Interval")
plt.xticks(rotation=45)
plt.show()

# i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
sns.pointplot( data=data, x="Fav genre", y="Anxiety", hue="Composer", ci=90, linestyles="--")
plt.title("Anxiety Across Genres with 90% CI (Dashed Lines)")
plt.xticks(rotation=45)
plt.show()

# j) 1 bar plot showing the number of observations in each category
sns.countplot( data=data, x="Fav genre", color='#a91616', hue="Composer")
plt.title("Number of Survey Respondents per Genre")
plt.xticks(rotation=45)
plt.show()

#new plot for question 1
palette = {"Improve": "#08A045", "No effect": "#FAD643", "Worsen": "#FF1F1F"}
sns.countplot(data=data, x="Fav genre", hue="Music effects", palette=palette)
plt.xticks(rotation=45)
plt.title("What genre has the best effects on health?")
plt.show()
#plt.pie(data["Frequency"].value_counts(), labels=["Rarely", "Sometimes", "Never", "Very Frequently"] )
#plt.show()

#6.3. Visualizing bivariate distributions (3 plots):
# a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.
sns.displot( data=data, x="Age", y="Depression", kind="hist", binwidth=(2, 1), cbar=True)
plt.title("Heatmap: Age vs Depression")
plt.show()

# b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).
sns.displot(data=data, x="Age", y="Anxiety", kind="kde", levels=12, thresh=0.1)
plt.title("Bivariate KDE: Age vs Anxiety")

# c) 1 “heatmap” plot representing 3 variables, again of kind kde.
sns.displot( data=data, x="Hours per day", y="Depression", hue="Instrumentalist", kind="kde")
plt.title("KDE Heatmap: Hours per Day vs Depression, Colored by Instrumentalist Status")












