sentence = str(raw_input("Enter any sentence: "))

letterCount = 0
vowelCount = 0
wordCount = 0
if(len(sentence)) != 0:
    for char in sentence:
        letterCount += 1
        
        if(char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u'):
            vowelCount += 1
        if(char == ' '):
            wordCount += 1
            
    wordCount +=1
    
    print("\n\n")
    print("Letter Count: " + str(letterCount))
    print("Vowel Count: " + str(vowelCount)) 
    print("Word Count: " + str(wordCount))
    
           
            
else:
    print("\n\nError, you did not input anything!")

        
raw_input("\n\nPress <Enter> to exit...")