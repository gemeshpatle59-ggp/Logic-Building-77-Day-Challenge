#  Given temperatures, find the next greater temperature for each day.


def greater_temperature(temperatures):

    temperature = [0]*len(temperatures)    

    for i in range(len(temperatures)):

        for j in range(i+1 , len(temperatures)):
            if temperatures[j] > temperatures[i]:
                temperature[i] = j - i
                break

    

    return temperature

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(greater_temperature(temperatures))
        


