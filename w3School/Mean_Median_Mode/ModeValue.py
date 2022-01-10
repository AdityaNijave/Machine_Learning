from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
modeSpeed = stats.mode(speed)
print(modeSpeed)

# output : ModeResult(mode=array([86]), count=array([3]))
# where, mode is : 86
# count : 3rd 86 in speed
