n=int(input())
sum=0
t=n
while n>0:
  digit=t%10
  sum+=digit**3
  t/=10

if sum==n:
  print("Armstrong")
else:
  print("Not Armstrong)
