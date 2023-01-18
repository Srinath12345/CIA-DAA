def prim(n,g):
    p=[]
    v=[]
    weight=[]
    for i in range(n):
        weight.append(9999999)
        v.append(0)
        p.append(-1)
    weight[0]=0
    for i in range (n):
        m = 9999999
        for j in range (n):
            if (v[j] == 0 and weight[j] < m):
                m = weight[j]
                ver = j
        v[ver] = 1
        for j in range (n):
            if (g[ver][j]!=0 and g[ver][j] < weight[j]):
                p[j] = ver
                weight[j] = g[ver][j]
        
    for i in range (1,n):
        print(i," ",p[i],"   ",weight[i])
        
def parent(x,pa):
    while(pa[x]):
        x = pa[x]
    return x ;

   
def kruskals(n,g):  
    p = [None for i in range (n)]
    i = 1
    while(i<n):
        m = 9999999
        for j in range (n):
            p[j]=0
            for k in range (n):
                if(g[j][k]!=0 and g[j][k] < m):
                    m = g[j][k]
                    a=c=j
                    b=d=k
        c = parent(c,p)
        d = parent(d,p)
        if (c != d):
            p[c] = d
            print(b," ",a," ",m)
            i+=1
        g[a][b] = 0
        
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

'prim(n,g)'
print()
'kruskals(n,g)'
print()
dikstra(n,g)