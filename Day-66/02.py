#  Given heights, find how much water can be trapped between bars; first derive a brute-force solution.


def trapping_rain_water(heights):
    n = len(heights)
    total_water = 0

    for i in range(n):

        left_max = heights[i]
        right_max = heights[i]

        for j in range(i + 1):
            if heights[j] > left_max:
                left_max = heights[j]

        for j in range(i, n):
            if heights[j] > right_max:
                right_max = heights[j]

        water = min(left_max, right_max) - heights[i]

        if water > 0:
            total_water += water

    return total_water


heights = [3, 0, 2, 0, 4]

print(trapping_rain_water(heights))
