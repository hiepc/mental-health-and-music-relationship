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

##array using different colors and line styles
import pandas as pd
import matplotlib.pyplot as plt

x = Hours_Per_Day
y1 = anxiety
y2 = depression
width = 0.16

plt.bar(x - width, y1, width, color='skyblue', label='anxiety', hatch='dotted')
plt.bar(x + width , y2, width, color='salmon', label='depression', hatch='\\')

# Add labels
plt.xlabel('Hours of Music Listened per Day')
plt.ylabel('Mental Health Conditions Rated from 1-10')
plt.title('Self-Reporded Mental Health Conditions Based on Hours of Music Listened per Day')
plt.legend()
plt.show()
#Comment explination: This is a bar plot containing data from anxiety and depression. 
#It shows how anxiety and depression are affected depending on the hours of music.
#Anxiety and depression are differentiated by colors and design.

##histogram
import pandas as pd
import matplotlib.pyplot as plt

x = insomnia
plt.title("Self-Reported Insomnia")
plt.xlabel("Insomnia on a scale from 1-10")
plt.ylabel("Number of reported cases")
plt.hist(x)
plt.show()
#Comment explination: This plot represents the number of responses to having insomnia and putting it on a 
#scale from 1-10 to see how many reported cases are high and low in insomnia cases.

##scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('mxmh_survey_results.csv')


print(data.describe())

#sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")

g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
plt.title("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Hours per day")
g.fig.suptitle("Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)
#Comment explination: This plot represents the number of hours listened to daily based off of the age group
#as well as if there are any effects whatsoever on peope if they are improvements, if they worsen or if there is no change.

##pie plot
import matplotlib.pyplot as plt
import numpy as np

#w = my_string.count("Very frequently")


#y = np.array([Frequency_Classical, Frequency_Country, Frequency_EDM, Frequency_Folk, Frequency_Gospel, Frequency_Hip_hop, Frequency_Jazz, Frequency_K_pop, Frequency_Latin, Frequency_Lofi, Frequency_Metal, Frequency_Pop, Frequency_RNB, Frequency_Rap, Frequency_Rock, Frequency_VGM])
#mylabels = ["classical", "country", "EDN", "Folk", "Gospel", "Hip_hop", "Jazz", "k_pop", "Latin", "Lofi", "Metal", "Pop", "R&B", "Rap", "Rock", "video_game_music"]

#plt.pie(y, labels = mylabels)
#plt.show() 


print(data["Frequency [Classical]"].value_counts())

g.fig.suptitle("")
g = sns.relplot()

plt.title("The frequency listened to Classical music")

plt.pie(data["Frequency [Classical]"].value_counts(), labels=["Rarely", "Sometimes", "Never", "Very Frequently"] )
plt.show()
#Comment explination: This plot represents the amout of times(frequency) someone listens to a specific genre (classical)
# it is split into four categories rarely (the biggest area), sometimes (the second biggest), never (second smallest) and very frequently (the smallest).

##bar plot
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


import matplotlib.pyplot as plt

Streaming_service = ['Spotify', 'Pandora', 'YouTube Music', 'Apple Music', 'None']
Means_of_hours_per_day = [3.8373, 2.1364, 3.2207, 3.5588, 2.9542]

plt.bar(Streaming_service, Means_of_hours_per_day, color = 'hotpink')
plt.title('Streaming service by Hours per day')
plt.xlabel('Streaming service')
plt.ylabel('Hours per day')
plt.show()

##grid plot
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
plt.ylabel('Metal health')
plt.xlabel('Age')

plt.plot(data_sample['Age'] ,data_sample['Anxiety'], linestyle = '')
plt.grid()
plt.show()

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
