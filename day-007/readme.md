## Day 007

### Yang dipelajari
* Hangman Project
* Import module 
    Python import statement from [AskPython](https://www.askpython.com/python/python-import-statement)
    1. Import class/function from a module
        ```python
        from collections import OrderedDict
        from os import path
        from math import pi
        print(pi)
        ```
    2. The import * statement
        ```python
        from math import *
        print(pi)
        print(floor(3.15))
        ```
    3. Python's import as Statement
        ```python
        # python import as
        import math as M
        
        print(M.pi)
        print(M.floor(3.18))
        ```
    4. Importing user-defined modules  
        test.py
        ```python
        def sub(a, b):
        return int(a) - int(b)
    
        def lower_case(str1):
        return str(str1).lower()
        ```  
        test2.py
        ```python
        import test
        
        print(test.sub(5,4))
        print(test.lower_case('SafA'))
        ```
    5. Importing from another directory  
        test1.py
        ```python
        def sub(a, b):
        return int(a) - int(b)

        def lower_case(str1):
        return str(str1).lower()
        ```  
        design.py
        ```python
        import importlib, importlib.util
 
        def module_directory(name_module, path):
        P = importlib.util.spec_from_file_location(name_module, path)
        import_module = importlib.util.module_from_spec(P)
        P.loader.exec_module(import_module)
        return import_module
 
        result = module_directory("result", "../inspect_module/test1.py")
 
        print(result.sub(3,2))
        print(result.lower_case('SaFa'))
        ```
    6. Importing class from another file  
        test.py
        ```python
        class Employee:
            designation = ""
    
            def __init__(self, result):
            self.designation = result
    
            def show_designation(self):
            print(self.designation)
 
 
        class Details(Employee):
            id = 0
    
            def __init__(self, ID, name):
            Employee.__init__(self, name)
            self.id = name
    
            def get_Id(self):
            return self.id
        ```  
        design.py
        ```python
        import importlib, importlib.util
 
        def module_directory(name_module, path):
            P = importlib.util.spec_from_file_location(name_module, path)
            import_module = importlib.util.module_from_spec(P)
            P.loader.exec_module(import_module)
            return import_module
        
        result = module_directory("result", "../Hello/tests.py")
        
        a = result.Employee('Project Manager')
        a.show_designation()
        
        x = result.Details(4001,'Safa')
        x.show_designation()
        print(x.get_Id())
        ```

### Code Exercise / Code Challenge
* [Hangman 1](./hangman1.py)
* [Hangman 2](./hangman2.py)
* [Hangman 3](./hangman3.py)
* [Hangman 4](./hangman4.py)
* [Hangman 5](./hangman5.py)
* [Hangman Arts as a module ](./hangman_art.py)
* [Hangman Words as a module](./hangman_words.py)
* [Hangman Final](./hangman_final.py)
