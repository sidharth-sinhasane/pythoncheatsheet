# cook your dish here
# Amphibian Escape

t=int(input())


for i in range(t):
    n,sec,h=map(int,input().split())
    ans=0
    start=n-1
# if n>=h:
#     ans+=n*(n-h+1)
#     start=h-1
# print(start,ans)
    
    for gain in range(start,0,-1):
        print("gains:",gain)

        if gain*sec  >= h:
            ans+=n-gain
            print(ans)
        else:
            break

    if n>=h:
        rem_row=gain-1
        row=n-h+1 + rem_row
        x=rem_row*(rem_row+1)//2
        extra=(row*(row+1)//2)-x
        ans+=extra
    print(ans)
    
    
