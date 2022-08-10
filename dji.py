import sys


def primToMST(adj=None,startPoint= 4):
 v = [startPoint]
 cost = 0
 list = [0,1,2,3,4,5,6]
 ilen = len(list)
 list.remove(startPoint)
 while len(v) < ilen:
  min = 99999999
  edge = [0,0]
  for x in v:
   for y in list:
    if int((adj[x])[y]) < min and int((adj[x])[y]) != 0:
     min = int((adj[x])[y])
     edge = [x,y]

  cost += min
  for x in edge:
   if x in list:
    list.remove(x)
    v.append(x)
    print(cost)
if __name__ == "__main__":
 primToMST([[0,7,0,5,0,0,0],[7,0,8,9,7,0,0],
                           [0,8,0,0,5,0,0],
                           [5,9,0,0,15,6,0],
                           [0,7,5,15,0,8,9],
                           [0,0,0,6,8,0,11],
                           [0,0,0,0,9,11,0]])