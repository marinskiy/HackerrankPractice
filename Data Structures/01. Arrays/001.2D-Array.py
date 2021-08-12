#Problem :https://www.hackerrank.com/challenges/2d-array/problem
#Score:15
def hourglassSum(arr):
    # Write your code here
    maxx=-float('inf')
    for i in range(0,4):
        s=0
        for j in range(0,4):
            s=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            maxx=max(maxx,s)
            s=0
    return maxx
