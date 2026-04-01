def frequency(text):
    text = text.lower()

    words=text.split()

    freq_dict={}


    for word in words:
        if word in freq_dict:       
             freq_dict[word]+=1
        else:
             freq_dict[word]=1

    sorted_freq=dict(sorted(freq_dict.items()))
     
   

    return sorted_freq

input_string=input("Enter a string:")

result=frequency(input_string)

print("Word frequencies(sorted):")
for word,count in result.items():
           print(word,":",count)
             
        
