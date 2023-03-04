import pandas as pd

fh = pd.read_csv('WAdriving.csv')
#https://remoteapps.wsdot.wa.gov/highwaysafety/collision/data/portal/public/
outside = pd.read_csv('outside.csv')
zipcode = fh['zip'].tolist()
#find count of zipcode
zip_dict = {}
for num in zipcode: 
    if num in zip_dict:
        zip_dict[num] += 1
    else:
        zip_dict[num] = 1

#print(zip_dict)
#Make a csav with 'good' zipcodes
counts = pd.value_counts(fh['zip'])
red = counts.index[counts >= 10]

goodzips = fh[fh['zip'].isin(red)]
goodzips.to_csv('goodzips.csv')
good = pd.read_csv('goodzips.csv')

#Finding age groups 
first = good[good['Age'] >= 18]
young = first[good['Age'] <= 30]

young.to_csv('young.csv')

second = good[good['Age'] > 30]
middle = second[good['Age'] <= 55]
middle.to_csv('middle.csv')

old = good[good["Age"] > 55]
old.to_csv('old.csv')

print(outside)


#zipcode and score, zipcode and race, age and likelyhood,  