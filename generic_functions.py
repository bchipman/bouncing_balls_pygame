from collections import namedtuple
import sys

def mk_namedtuple(name, di):
    return namedtuple(name, di.keys())(**di)

def print_sys_path():
    for p in sys.path:
        print(p)

def change_sys_path():
	del sys.path
	sys.path = [
	'C:\\Dropbox\\sublime_text_saves\\.py\\bouncing_balls_pygame\\',
	'C:\\Program Files (x86)\\Python34\\',
	'C:\\Program Files (x86)\\Python34\\DLLs\\',
	'C:\\Program Files (x86)\\Python34\\Lib\\',
	'C:\\Program Files (x86)\\Python34\\Lib\\site-packages\\',
	'C:\\Program Files (x86)\\Python34\\courselib\\',
	'C:\\Windows\\system32\\python34.zip\\']
        
if __name__ == '__main__':
    print_sys_paths() 
