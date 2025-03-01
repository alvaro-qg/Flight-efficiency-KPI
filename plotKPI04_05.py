import matplotlib.pyplot as plt

def plotKPI04_05(KPI):

    KPI.iloc[1:6].plot(kind='bar',title="Countries")
    plt.axhline(y=KPI.iloc[0]['En-route extension'],linewidth=1, color='g',linestyle='--')
    plt.xticks(rotation=0)
    plt.xlabel('Countries')
    plt.ylabel('Execess distance %')

    plt.figure(1)
    KPI.iloc[6:11].plot(kind='bar',title="Airports")
    plt.axhline(y=KPI.iloc[0]['En-route extension'],linewidth=1, color='g',linestyle='--')
    plt.xticks(rotation=0)
    plt.xlabel('Airports')
    plt.ylabel('Excess distance %')

    plt.show()

