def clockangle(time): #time = 730, 1545 
    angle = 0
    #1200 - 0
    #0300 - 90
    #0900 - 90
    #0730 - 45
    #1545 - 157.5
    #2350
    mins = time%100 #mins = 30, 45, 50
    hr = time//100 #hr = 7, 15, 23
    min_loc = mins/5 #min_loc = 6, 9, 10
    if hr > 12:
        hr_loc = (hr-12)+mins/60 #hr_loc = 3+0.75=3.75, 11+0.83 = 11.83
    else:
        hr_loc = hr+mins/60 # hr_loc = 7+0.5 = 7.5
    diff = abs(hr_loc-min_loc) #diff = 1.5, 5.25, 1.83
    angle = diff * 30 #angle = 45, 157.5, 50
    if angle > 180:
        angle = 360 - angle
    return round(angle,2)

#print(clockangle(900))


#Take a year as an argument (-2000 to 4000), print whether it is a leap year or not
#1900 is not a leap year
#1920 is a leap year
#2000 is a leap year
#2023 is not a leap year
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

#print(isLeapYear(2704))

#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

#Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
#Output: 3
#Explanation:
#Start at station 3 (index 3) and fill up with 4 units of gas. Your tank = 0 + 4 = 4
#Travel to station 4. Your tank = 4 - 1 + 5 = 8
#Travel to station 0. Your tank = 8 - 2 + 1 = 7
#Travel to station 1. Your tank = 7 - 3 + 2 = 6
#Travel to station 2. Your tank = 6 - 4 + 3 = 5
#Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
#Therefore, return 3 as the starting index.

def startPoint(gas, cost):
    startPoint = -1
    for start in range(len(gas)): #start=3
        currentTank = gas[start]-cost[start] #currentTank = 3
        if currentTank < 0:
            continue
        for position in range(1,len(gas)+1): #position = 1,2,3,4,5
            if start+position >= len(gas):
                position = position-len(gas) #position = -3, -2, -1
            if start+position == start:
                return start
            currentTank = currentTank+gas[start+position]-cost[start+position] #currentTank = 6, 4, 2, 0
            if currentTank < 0:
                break
    return startPoint


#Three Sum Closest list with numbers find three integers that are as close to a given target as possible


#Given an integer list nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

#Input: nums = [1,2,3,4,5] len(nums) = 5
#Output: true

#Input: nums = [5,4,3,2,1]
#Output: false

#Input: nums = [2,1,5,0,4,6]
#Output: true

def orderTriple(nums):
    triplePresent = False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] < nums[j] and nums[j] < nums[k]:
                    return True
    return triplePresent

print(orderTriple([2,1,5,0,4,6]))