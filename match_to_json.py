import simplejson
result = [] 
with open('match.txt') as f:
    for row in f:
        result.append([e.strip() for e in row.split()])

print simplejson.dumps(result)
