#continue 

#Loop Control: Continue
#While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely. 
#What if we only want to skip the current iteration of the loop?

#continue allows you to skip certain parts of a loop's code for a specific iteration,

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)