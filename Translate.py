
import csv
import re
import time
import psutil
#psutil package is used mainly for system monitoring, profiling and limiting process resources and management of running processes.

# start time of the performance file creation.
start_time = time.time()

# read the file find_words.txt
words_text = open("find_words.txt", "r")
find_words = words_text.read()
words_text.close()
find_words_inlist = find_words.split()

# creating a frequency dictionary and matches any character from a-z or 0-9 but the length range must between 3 to 15 using regular expression.
frequency = {}
shakespeare_text = open("t8.shakespeare.txt", 'r')
text_string = shakespeare_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

#read the french_dictionary.csv file in its csv mode
with open('french_dictionary.csv', mode='r') as data:
    reader = csv.reader(data)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}

#create an english list for all english words in find_words file
total_english = []
for word in match_pattern:
    if word in find_words_inlist:
        total_english.append(word)

#reduce the duplicate entries from the list
english = set(total_english)

#again convert it in to a list
english = list(english)

# creating an french list for all french words in find_words file
french = []
for x in english:
    for key, value in dict_from_csv.items():
        if x in key:
            french.append(value)


#frequency = {}
for y in total_english:
     count = frequency.get(y, 0)
     frequency[y] = count + 1

#create an frequency list , number of times the word was replaced
frequency_list = frequency.keys()
freq = []
for z in frequency_list:
     freq.append(frequency[z])

#zip the list of english,french words and its corresponding frequency
final = list(zip(english, french, freq))

#create frequency.csv having 3 columns, English Word, French Word and third “Frequency” and its the first line of the file
headerFile = ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as file:
     writer = csv.writer(file)
     writer.writerow(headerFile)

     for row in final:
         for r in row:
             file.write(str(r) + ',')
         file.write('\n')

#create t8.shakespeare.translated.txt is the output file (translated from English to French)
test_string = text_string
print("The original string is : " + str(test_string))

#copy
new_dict = dict_from_csv

#create result list and adding dictionary information
result = []
for word in test_string.split():
    result.append(new_dict.get(word, word))

#result contains all the entire paragraph
result = ' '.join(result)

#write the paragraph in a translated text file 
f = open("t8.shakespeare.translated.txt", "w")
f.write(str(result))
f.close()

#total time taken 
time_taken = time.time() - start_time
#memory taken for this process
memory_taken = psutil.cpu_percent(time_taken)

#write the time taken for translation in performance text file
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()