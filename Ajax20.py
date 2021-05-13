import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

ajax1 = pd.read_csv(r'C:\Users\Pavel\Desktop\Python1\Ajax 20-21 Eredvisie\AjaxEredivisie2021.csv')

#lets create some new columns

ajax1['goalpmin'] = ajax1['goal'] / ajax1['minsPlayed']
ajax1['goalpmatch'] = ajax1['goalpmin'] * 90
ajax1['newfullname']  = ajax1[['firstName', 'lastName']].agg('-'.join, axis=1)

#lets see some of the results of the table: filter the first 5 by 'ranking'
print(ajax1[(ajax1['ranking']<6)])


#GOALS ANALYSIS
#now lets show the ranking of players with more goals
ajax2=ajax1[(ajax1['goal']>0)]
print(ajax2.sort_values(by=['goal'], ascending=False).plot.bar(x='newfullname', y='goal'))
#but lets compare it with the ranking of players with more goals PER MINUTE
print(ajax2.sort_values(by=['goalpmatch'], ascending=False).plot.bar(x='newfullname', y='goalpmatch'))


#ASISTS ANALYSIS
ajax1['asistpermatch'] = ajax1['assistTotal'] / (ajax1['minsPlayed']/90)
#lets show the ranking of players with more assistans
ajax3=ajax1[(ajax1['assistTotal']>0)]
ajax3.sort_values(by=['assistTotal'], ascending=False).plot.bar(x='newfullname', y='assistTotal')
#but lets compare it with the ranking of players with more goals PER MINUTE
ajax3.sort_values(by=['asistpermatch'], ascending=False).plot.bar(x='newfullname', y='asistpermatch')


#GOALS PER POSITION ANALYSIS

#first I need to group the positions by goal
ajax4 =pd.pivot_table(ajax1, index=["positionText"], values=["goal"], aggfunc=py.sum)
print(ajax4)
# now I need to transform this pivot in a dataframe
ajax5 = ajax4.reset_index()
print(ajax5)
# finally with this new df I will plot the graphic in a pie
plt.pie(ajax5['goal'], labels = ajax5['positionText'], startangle = 90)
plt.show()
