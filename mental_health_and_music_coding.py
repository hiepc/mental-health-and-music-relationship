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

#1 plot of any type containing data from more than 1 array using different 
#colors and line styles
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
#Comment: This is a bar plot containing data from anxiety and depression. 
#It shows how anxiety and depression are affected depending on the hours of music.
#Anxiety and depression are differentiated by colors and design.

#histogram
import pandas as pd
import matplotlib.pyplot as plt

x = insomnia
plt.title("Self-Reported Insomnia")
plt.xlabel("Insomnia on a Scale from 1-10")
plt.ylabel("Number of Participants")
plt.hist(x)
plt.show()
#Comment: Each participant have to rate their insomnia on a scale from 1-10. 
#This plot (historgram) displays the frequency of each rating. 


#scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('mxmh_survey_results.csv')


print(data.describe())

<<<<<<< Updated upstream


sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")


g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)


#pie plot
import matplotlib.pyplot as plt
import numpy as np

#w = my_string.count("Very frequently")


#y = np.array([Frequency_Classical, Frequency_Country, Frequency_EDM, Frequency_Folk, Frequency_Gospel, Frequency_Hip_hop, Frequency_Jazz, Frequency_K_pop, Frequency_Latin, Frequency_Lofi, Frequency_Metal, Frequency_Pop, Frequency_RNB, Frequency_Rap, Frequency_Rock, Frequency_VGM])
#mylabels = ["classical", "country", "EDN", "Folk", "Gospel", "Hip_hop", "Jazz", "k_pop", "Latin", "Lofi", "Metal", "Pop", "R&B", "Rap", "Rock", "video_game_music"]

#plt.pie(y, labels = mylabels)
#plt.show() 

#>>>>>>> Stashed changes
g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)
#=======

print(data["Frequency [Classical]"].value_counts())
plt.xlabel("")
plt.ylabel("")

g.fig.suptitle("")
g = sns.relplot()

plt.title("The frequency listened to Classical music")

plt.pie(data["Frequency [Classical]"].value_counts(), labels=["Rarely", "Sometimes", "Never", "Very Frequently"] )

#Comment: In this scatter plot, each dot represents a single observation. 
#This plot allows us to determine if there's a relationship between the age of a person and the number of hours of music listened in a day.





g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)

=======
g = sns.relplot(data=data, y="Hours per day", x="Age", hue="Music effects")
g.fig.suptitle("Title: Hours per day listened to music based on the age group and the benefits from it", fontsize=12, fontweight='bold')
g.fig.subplots_adjust(top=0.85)
>>>>>>> Stashed changes
