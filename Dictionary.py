from statistics import mean
StudentGrades = {
    'Ivan': [4.32, 3, 2],
    'Martin': [3.45, 5, 6],
    'Stoyan': [2, 5.67, 4],
    'Vladimir': [5.63, 4.67, 6]
}
avgDict = {}
for k,v in StudentGrades.items():
    avgDict[k] = mean(v)
print(avgDict)
print(max(avgDict.values()))
print(min(avgDict.values()))
print(mean(avgDict.values()))
#avgDict[k] = sum(v)/ float(len(v))