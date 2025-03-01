def sum_variants(TimeDiff,nFlights):
    a1=100*sum(1 for t in TimeDiff if t<=5 and t>=-5)/nFlights
    b1=100*sum(1 for t in TimeDiff if t>=0 and t<=5)/nFlights
    a2=100*sum(1 for t in TimeDiff if t<=15 and t>=-15)/nFlights
    b2=100*sum(1 for t in TimeDiff if t>=0 and t<=15)/nFlights

    return [a1,b1,a2,b2]