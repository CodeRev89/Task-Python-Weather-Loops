# printer(elements)
# - Accepts a list
# - Prints every element of the list


elements = ["string"]
def printer(elements):
    for element in elements:
      print(element)
      
    # Your code here
    ...
printer(elements)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)

temperatures_fahrenheit=[20,30,40,50]
def to_celsius(temperatures):
    # Your code here
    
    celcius=[]
    for temp in temperatures_fahrenheit:
        c= int((temp-32) * (5/9))
        celcius.append(c)
    print(celcius)
    ...
to_celsius(temperatures_fahrenheit)

# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold

highestt=[50,60,40,70,25]
threshhold = 30
def hottest_days(temperatures, threshold):
    highest=[]
    for HT in highestt:
        if HT>threshhold:
            highest.append(HT)
        else: 
            pass
    print (highest)
    return highest    
hottest_days(highestt, threshhold)
    # Your code here
    


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
tempreaturest=[40,50,60,70,80,20,10,25]
thresh=30
def print_hottest_days(temperatures, threshhold):
    alot=[]
    alot=  to_celsius(temperatures)
    thresh=int((threshhold-32)*(5/9))
    threshc=[]
    threshc= hottest_days(alot, thresh)
    # for temp in temperaturest:
    #     c= int((temp-32) * (5/9))
    #     if temp > thresh:
    #          alot.append(c)
    #     else: 
    #         pass
    #     print (c)
    # return (alot)
print_hottest_days(tempreaturest,thresh)
             
    # Your code here