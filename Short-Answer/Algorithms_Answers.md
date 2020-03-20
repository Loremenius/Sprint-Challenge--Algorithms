#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) The while loop stops after a is greater than n^3 but only add n^2 everytime. In my mind it will run n^3 - n^2 times which is just n^3 times


b) O(n*log(n)) The for loop is equivalent to n run time. The while loop has a runtime of log(n) because it decreases by a multiple of 2 everytime. since the while is in the for loop, it will run log(n) for n amount of times. 


c) O(n) because run time is linear and dependent on amount given. The function has a complexity of 1 and runs n amount of times which leaves us with O(n)

## Exercise II

start at the base floor and drop an egg. if the egg doesnt break, go up a floor and drop another egg. continue until an egg breaks. 

This would have a runtime of O(n) because the action is constant for each floor and will continue until nth floor. This is 1*n and has a runtime of O(n)


