x,y,s,t=map(int,input().split())
a=["WE"[x>s]]*abs(x-s)+[""]*90+["NS"[y>t]]*abs(y-t)
while 1:print(a.pop()+a.pop(0))
