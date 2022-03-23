CityArea = {
     'Rabat to Sueca' : 1065,
     'Sueca to Rudow' : 2656,
     'Rudow to Mosu' : 1352,
     'Mosu to Le Plessis Trevise' : 1841,
     'Le Plessis Trevise to Kang Dong' : 61,
     'Kang Dong to Nezahualcoyotl' : 1634,
     'Nezahualcoyotl to Lindenwold' : 1051,
     'Lindenwold to Queanbeyan' : 285,
     'Queanbeyan to Saint Chamond' : 146,
     'Saint Chamond to Cheektowaga' : 11,
     'Cheektowaga to Tirupati' : 380,
     'Tirupati to Snezhinsk' : 2547
 }
getCity = min(CityArea,key=CityArea.get)
minDistance = min(CityArea.values())
print("Short path city is : " ,getCity," and Distance is : ", minDistance,"Km")