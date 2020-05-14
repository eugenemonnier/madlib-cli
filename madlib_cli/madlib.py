file = open('assets/spam.txt')
global contents
contents = file.read()

word_list = list()
stop = 0

for x in range(contents.count('{')):
  start = contents.find('{', stop)
  stop = contents.find('}', start)
  word = contents[start : stop + 1]
  word_list.append(word)

# print(word_list)

mad_lib = str()

for x in word_list:
  mad_lib = contents.replace(x, input('Give me a(n) ' + x + ':'), 1)
# contents.format(**mad_lib_dict)
print(mad_lib)