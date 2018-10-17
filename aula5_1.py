#função local
import time as tm
lt=tm.localtime()
day=lt.tm_mday
mon=lt.tm_mon
year=lt.tm_year
hour=lt.tm_hour
minu=lt.tm_min
if mon==10:
    mon='outubro'
print('A data de hoje é',day,'/',mon,'/',year)
print('A hora de hoje é',hour,':',minu)


