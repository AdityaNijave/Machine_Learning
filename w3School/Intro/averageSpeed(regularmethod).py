
def average(speed):
    averageSpeed = sum(speed) / len(speed)
    return averageSpeed


speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# average(speed)
print(f"average speed is {average(speed)}")

# output : average speed is 89.76923076923077                            (this is mean value)
