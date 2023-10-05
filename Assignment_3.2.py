#import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the test and training data
test1 = pd.read_csv('test.csv')
train = pd.read_csv("train.csv")
test2 = pd.read_csv("gender_submission.csv")

#concatenate the two test data sets together along the columns
test = pd.concat([test1, test2], axis=1)
#remove the duplicate column
test = test.T.drop_duplicates().T

#combine the test and train data. Use axis 0 to combine along rows adn ignore index to reset the indexing since the important index is passenger ID.
tit_data = pd.concat([train, test], axis=0, ignore_index=True)

#Create a variable summarydata to contain the summary of the titanic dataset
summarydata = tit_data.describe()

#create a separate dataset with just the variables we are going to plot
vis_data = tit_data[['PassengerId', 'Pclass', 'Age', 'Sex', 'Survived']]
#drop all rows that have na
vis_data = vis_data.dropna(axis = 0)
#create a died column that is compliment of survived
vis_data['Died'] = ~vis_data['Survived'].astype(bool)


#Create a histogram showing the distribution of age of people on the Titanic. 
hist1 = sns.histplot(x = 'Age', data = vis_data)

#create the x and y label and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Frequency of Titanic Passengers')
# Set the style with grid
sns.set_style("darkgrid")
# Add a description to the figure
hist1.text(-13, -55, """Figure 1. Age Frequency of Titanic Passengers shows the majority of 
Titanic passengers were in their 20s with the frequency steadily 
decreasing after this age range.""")

#show the histogram
plt.show()

#plt.show(hist1)


#Make another histogram showing the distribution of age of people on the Titanic segregated by survivalship.
#use survived as the hue but dont include null values
hist2 = sns.histplot(x = 'Age', hue = 'Survived', data = vis_data, multiple='stack')
#create legend labels and assign them to the legend
legend_labels = ['Survived', 'Died']
hist2.legend(labels=legend_labels)
#create the x and y label and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Frequency of Titanic Passengers by Survivorship')
# Set the style with grid
sns.set_style("darkgrid")
# Add a description to the figure
hist2.text(-13, -70, """Figure 2. Age Frequency of Titanic Passengers by Survivorship shows 
the majority of Titanic passengers were in their 20s with the frequency 
steadily decreasing after this age range. The additional survivorship 
histogram shows that survivorship distribution was similar to the age
histogram. Young children had higher counts of surviving.""")

#show the histogram

plt.show()


#Create a bar chart showing the percentages of who survived on the Titanic. 
lived = len(tit_data.loc[tit_data['Survived'] == 1])*100/len(tit_data)
died = len(tit_data.loc[tit_data['Survived'] == 0])*100/len(tit_data)
liv_die_x = ['Lived','Died']
liv_die_y = [lived, died]

plt.bar(liv_die_x, liv_die_y)
plt.xlabel('Survivorship')
plt.ylabel('Percentage of Titanic Passengers')
plt.title('Survivorship of Titanic Passengers')
plt.text(-0.7, -13, """Figure 3. Survivorship of Titanic Passengers shows that overall, around 40% of 
passengers survived.""",
       va = "center")

plt.show()


#Make another bar chart showing the percentages of who survived on the Titanic segregated by sex.
#create the bar chart with x being percentage of passengers that survived seperated by sex.
bar = sns.barplot(x= 'Survived', y= 'Sex', data = vis_data)
#create the x label and title
bar.set(title = 'Survivorship by Sex',
        xlabel = 'Percentage of Passengers that Survived')
# Set the style with grid
sns.set_style("darkgrid")
# Add a description to the figure
bar.text(-.14, 2, """Figure 4. Survivorship of Titanic Passengers by Sex shows that of males 
on the Titanic, only around 15% survived whereas around 80% of females 
survived.""",
       va = "center")

#show the bar chart
#plt.show(bar)

plt.show()


#Create a boxplot showing the distribution of who survived on the Titanic vs their passenger class. 
box = sns.boxplot(x = 'Pclass', y= 'Survived',  data = vis_data)
# Set the style with grid
sns.set_style("darkgrid")
#create the x and y label and title
plt.xlabel('Passenger Class')
plt.ylabel('Percentage of Passengers Survived')
plt.title('Survivorship on the Titanic Based on Passenger Class')
# Add a description to the figure
box.text(-.8, -.35, """Figure 5. Survivorship of Titanic Passengers by Class shows that there 
is not one class on the Titanic that results almost exclusively in survival 
or death. Becuase this uses binary data with a box plot, if there are 
approximately equal data points, a box will be drawn.""",
       va = "center")

#plt.show(box)

plt.show()


#Make another boxplot showing the distribution of who survived on the Titanic vs their passenger class segregated by sex.
box2 = sns.boxplot(x= 'Pclass', y = 'Survived', hue = 'Sex', data = vis_data)
# Set the style with grid
sns.set_style("darkgrid")
#create the x and y label and title
plt.xlabel('Passenger Class')
plt.ylabel('Percentage of Passengers Survived')
plt.title('Survivorship on the Titanic Based on Passenger Class and Sex')
# Add a description to the figure
box2.text(-.8, -.5, """Figure 6. Survivorship of Titanic Passengers by Class and Sex shows 
that almost all Class 1 Females survived, approximately equal amounts
of class 1 males survived and died, almost all class 2 males died, 
almost all class 2 females survived, almost all class 3 males died,
and approximately equal amount of class 3 females died or survived.
A box is only drawn if there are approximately equal amounts of death
and survival. A line is shown if there are almost exclusively values
at that location (either death or survival).""",
       va = "center")

#plt.show(box2)

plt.show()


#Write a few sentence explaining the findings of your analysis. Feel free to reference any of visualizations.

print("""Based on the Figure 4, males were much less likely to survive when compared to females. Additionally, looking at Figure at 2, people of younger and older ages were more likely to survive when compared to the more middle ages. Lastly, there are a few main takeaways from Figure 6. One is that 1st class and 2nd females were very likely to survive while 2nd and 3rd class males were very likely to die. The two groups that were more split evenly were 1st class males and 3rd class females. Overall takeaway: if you were a male you were likely to die and if you were a female, more likely to survive and higher the class the better. """)
