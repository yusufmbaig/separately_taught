# print("farenheit to celcius calc")
# # 1. prompt user to input farenheit value
# # 2.    if input is string or boolean or blank, display error message and repeat step 1
# # 2. convert farenheit to celcius
# # 3. return celcius to two decimal places
#
#
# fahren = input("Enter a temperature in Fahremheit to be converted to Celsius: ")
# fahren = int(fahren)
# cels = (5/9)*(fahren-32)
# print(cels)





#1. prompt user for their age
#1.5    if blank or string, error
#2. set value as an integer
#3. set folk_age_min to (age/2) +7
#4. set folk_age_min to (age+23)/2
#5. print folk_age_max + age and folk_age_min +age with some string

# import sys
# age = input("Enter age of u ples: ")
# try:
#     age = int(age)
# except:
#     print("YOu didn't enter an interger")
#     sys.exit()
# folk_age_max = ((age / 2) + 7)
# folk_age_min = ((age + 70) / 2)
# print ("Your max get together age is %s and your min (weirdo) is %s" % (folk_age_max, folk_age_min))






#1. prompt for sentence
#2.
#3. if length greater than 0 and less than 5
#4.     print "lol loser"
#5. elif length greater than 5 less thatn 10
#6.     print "now we got a sentence! congrates u r a proficient languager equal to a 4 year old"
#7. else length greater than 10
#8.     print "ya no im not reading that bai"

statement = input("talk to me baby: ")
if (len(statement) >= 0) & (len(statement) < 5):
    print("lol loser")
elif (len(statement) >= 5) & (len(statement) < 10):
    print("now we got a sentence! congrates u r a proficient languager equal to a 4 year old")
else:
    print("ya no im not reading that bai")