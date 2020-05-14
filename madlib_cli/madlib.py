def get_file(selected_file):
  file = open(selected_file)
  contents = file.read()
  grab_keys(contents)

def grab_keys(contents):
  word_list = list()
  stop = 0
  for word in range(contents.count('{')):
    start = contents.find('{', stop)
    stop = contents.find('}', start)
    word = contents[start : stop + 1]
    word_list.append(word)
  mad_lib(contents, word_list)

def mad_lib(contents, word_list):
  for x in word_list:
    contents = contents.replace(x, input('Give me a(n) ' + x + ':'), 1)
  print(contents)

def __main__():
  pass

if __name__ == "__main__":
  get_file('assets/spam.txt')