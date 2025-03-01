import matplotlib.pyplot as plt

def plotKPI01_14(KPI_punctuality):

    KPI_punctuality.iloc[0].plot(kind='bar',title="ECAC Area KPI")
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.xlabel('Variants')
    plt.ylabel('Punctuality %')

    plt.figure(1)
    KPI_punctuality.iloc[1:6].plot(kind='bar',title="Countries KPI")
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.xlabel('Countries')
    plt.ylabel('Punctuality %')

    plt.figure(2)
    KPI_punctuality.iloc[6:11].plot(kind='bar',title="Airports KPI")
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.xlabel('Airports')
    plt.ylabel('Punctuality %')

    plt.show()

