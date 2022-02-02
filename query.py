import math

data = [
  {
  "match": {
      "instance_id": "i-0d7110172b986e699"
    }
  },
  {
  "match": {
     "severity": "Criticalvgh"
    }
   }
]
search_dict = dict()
search_param = ['instance_id:i-0d7110172b986e699', 'severity:low','description:Avg']
for exp in search_param:
        column = exp.split(':')[0]
        pattern = exp.split(':')[1]
        search_dict[column] = pattern
sample = []

print(search_dict)
for exp in search_param:

  matchDic = {}
  itemDic = {}

  column = exp.split(':')[0]
  pattern = exp.split(':')[1]
  itemDic[column] =  pattern 
  matchDic["match"] = itemDic
  sample.append(matchDic)
print(sample)

sr = '*\"SearchString\"*'


sr.replace("SearchString", "pattern")

fullString = ''

for exp in search_param:
        column = exp.split(':')[0]
        pattern = exp.split(':')[1]
        if column =='description':
          word = sr.replace("SearchString", pattern)
          print(word)
          if fullString =='':
            fullString =  word
          else:
            temp = ' AND '+ word
            fullString = fullString+ temp
        else:
          temp = ' AND '+pattern
          fullString = fullString + temp
          
searchStr = fullString[4:]
print(fullString[4:])
# '*\"VSmart\"* AND i-055c2327d45d57d84 AND star'

a =[[-1 for i in range(3)] for y in range(3)]
print(a)
count = 0
for i in range(3):
  for j in range(3):
    count+=1
    a[i][j] = math.gcd(i,j)
print(a)
print(count)