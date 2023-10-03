#
##
##from datetime import timedelta 
##delta = timedelta()
##
####from datetime import *
##import re
##
##def lower_after_upper(string):
##    return True if re.search('[А-Я]+[а-я]+$',string) else False
##if __name__ == '__main__':
##    print(lower_after_upper('Ха-Ха-Ха'))  # True
##    print(lower_after_upper('ХОХОХО'))  # False

###написать рекурсивную функцию

##путь до папок
import os

def get_paths(path='.'):
  for name in os.listdir(path):
    abs_path=os.path.abspath(os.path.join(path,name))
    yield abs_path
    
    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths('testfolder'):
    print(i)
    
##путь до файлов
def get_paths(path='.'):
  for name in os.listdir(path):
      abs_path=os.path.abspath(os.path.join(path,name))
      if os.path.isfile(abs_path) is True:
          yield abs_path
      elif os.path.isdir(abs_path) is True:
          yield from get_paths(abs_path)

for i in get_paths('testfolder'):
    print(i)


