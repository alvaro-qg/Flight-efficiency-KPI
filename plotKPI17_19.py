import matplotlib.pyplot as plt

def plotKPI17_19(KPI):

    KPI.iloc[1:6]['Average distance'].plot(kind='bar',title="Countries")
    plt.axhline(y=KPI.iloc[0]['Average distance'],linewidth=1, color='g',linestyle='--')  
    plt.xticks(rotation=0)
    plt.xlabel('Countries')
    plt.ylabel('Average distance[NM]')

    plt.figure(2)
    KPI.iloc[6:11]['Average distance'].plot(kind='bar',title="Airports")
    plt.axhline(y=KPI.iloc[0]['Average distance'],linewidth=1, color='g',linestyle='--')  
    plt.xticks(rotation=0)
    plt.xlabel('Airports')
    plt.ylabel('Average distance[NM]')

    plt.figure(3)
    KPI.iloc[1:6]['Average time'].plot(kind='bar',title="Countries")
    plt.axhline(y=KPI.iloc[0]['Average time'],linewidth=1, color='g',linestyle='--')  
    plt.xticks(rotation=0)
    plt.xlabel('Countries')
    plt.ylabel('Average time[min]')

    plt.figure(4)
    KPI.iloc[6:11]['Average time'].plot(kind='bar',title="Airports")
    plt.axhline(y=KPI.iloc[0]['Average time'],linewidth=1, color='g',linestyle='--')  
    plt.xticks(rotation=0)
    plt.xlabel('Airports')
    plt.ylabel('Average time[min]')


    plt.show()

