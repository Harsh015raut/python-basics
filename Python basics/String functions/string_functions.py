story = '''Year 1943: The first work which is now recognized as AI was done by Warren McCulloch and Walter pits in 1943. They proposed a model of artificial neurons.
Year 1949: Donald Hebb demonstrated an updating rule for modifying the connection strength between neurons. His rule is now called Hebbian learning.
Year 1950: The Alan Turing who was an English mathematician and pioneered Machine learning in 1950. Alan Turing publishes "Computing Machinery and Intelligence" in which he proposed a test. The test can check the machine's ability to exhibit intelligent behavior equivalent to human intelligence, called a Turing test.'''

#String Functions
print(len(story))
print(story.endswith('sfisygishc'))#Will return true or fals based on condition
print(story.endswith('test.'))
print(story.count('Turing'))

#Capitalize-capitalises first letter character of string
print(story[15:20].capitalize())

print(story.find('Turing')) #Gives the index of first letter of the word to be searched
print(story.replace('Turing','AlanTuring'))

# /n->New Line,/t->tab,//-> single /

