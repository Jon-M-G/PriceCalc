
price = input('Item Price: ')
#price = '.83'
priceF = float(price)

refCount = 0
recCount = 0
scrapCount = 0
wepCount = 0

if priceF>= 1:
    refCount = int(priceF)
else:
    if priceF>=.33:
        recCount = priceF//.33
        priceF= priceF % .33
    if priceF>=.11:
        scrapCount = priceF//.11
        priceF = priceF%.11
    if priceF >= .05:
        wepCount = priceF//.05
        priceF = priceF%.05


print('Ref: '+str(refCount))
print('Rec: '+str(recCount))
print('Scrap '+str(scrapCount))
print('Weps: '+str(wepCount))

countS = input('Item Count: ')
count = int(countS)
refCount *= count
recCount *= count
scrapCount *= count
wepCount *= count

# convert weps to scrap
scrapCount += wepCount//2
wepCount %=2

# convert scraps to reclaimed
recCount += scrapCount//3
scrapCount %= 3

# convert reclaimed to refined
refCount += recCount//3
recCount %= 3

print('UPDATED COUNTS')
print('Ref: '+str(refCount))
print('Rec: '+str(recCount))
print('Scrap '+str(scrapCount))
print('Weps: '+str(wepCount))