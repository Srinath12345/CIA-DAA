def dikstra(n,g):
    ver=[]
    cost=[999999 for i in range(n)]
    cost[0]=0
    mincost = min(cost)
    mc = cost.index(min(cost))
    for i in range (n-1):
        if mc not in ver:
            ver.append(mc)
            print(mc)
            for j in range (n):
                if (g[mc][j] != 0 and mincost+g[mc][j]<cost[j]):
                    cost[j] = mincost+g[mc][j]
        mincost = 999999
        for i in range (n):
            if i not in ver:
                if cost[i] < mincost:
                    mincost = cost[i]
        mc = cost.index(mincost)
        print(cost)

n = 6
g = [[0,10,0,0,0,8],
     [0,0,1,2,0,0],
     [0,0,0,0,0,0],
     [0,0,-2,0,0,0],
     [0,-4,0,-1,0,0],
     [0,0,0,0,1,0]]

dikstra(n,g)