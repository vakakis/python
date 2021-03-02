#ergasia3
import urllib.request

date = "2021-03-01"

#kino is 1100
gameId = "1100"


req = urllib.request.Request('https://api.opap.gr/draws/v3.0/' + gameId + '/draw-date/' + date + '/' + date + '/draw-id')
with urllib.request.urlopen(req) as response:
   drawIdresults = response.read()
   drawIdresults = drawIdresults.decode("utf-8")
   drawIdresults = drawIdresults.replace("[","")
   drawIdresults = drawIdresults.replace("]","")

myList = drawIdresults.split(",")

req = urllib.request.Request('https://api.opap.gr/draws/v3.0/' + gameId + '/' + myList[0] )
with urllib.request.urlopen(req) as response:
   kinoResults = response.read()
   kinoResults = kinoResults.decode("utf-8")

print (kinoResults)
