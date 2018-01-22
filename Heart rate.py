def heartbeat():
    
    print ("Target Heart Rate while exercising")
    Name = str(input("What is your name? "))
    Age = int(input("What is your age? "))
    MaximumHR = 220 - Age
    Resting = int(input("Resting heart rate: "))
    Lower = int((MaximumHR-Resting)*(0.65)+(Resting))
    Upper = int((MaximumHR-Resting)*(0.85)+(Resting))
    print ("\nHEART RATES\n" + str(Name) + ", for your age:\t" + str(Age) + "\nResting heart rate:\t" + str(Resting) + "\nYour target heart rate is  " + str(Upper) + " to " + str(Lower) + " beats per minute.\n")

    text_file = open("HEARTResults.txt", "a")
    text_file.write("\nHEART RATES\n" + str(Name) + ", for your age:\t" + str(Age) + "\nResting heart rate:\t" + str(Resting) +                  "\nYour target heart rate is  " + str(Upper) + " to " + str(Lower) + " beats per minute.\n")
    text_file.close()
    
heartbeat()

