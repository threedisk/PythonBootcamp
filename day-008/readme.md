## Day 008

### Yang dipelajari
* Function with Inputs, name disebut __parameter__, Tris disebut __argument__
    ```python
    def greet_with_name(name):
        print(f"Hello {name}")
        print(f"How are you today, {name}?")
    greet_with_name("Tris")
    ```
* Positional and Keyword Argument  
    Positional-argument, ketika argument yang dimasukkan diganti atau dibalik, maka akan muncul output yang terbalik juga
    ```python
    def greet_with(name, location):
        print(f"Hello {name}")
        print(f"You from {location}")
    greet_with("Tris","Ngawi")
    greet_with("Ngawi","Tris")
    ```  
    Output
    ```python
    Hello Tris
    You from Ngawi
    Hello Ngawi
    You from Tris
    ```  
    Berbeda dengan keyword argument, jika posisi dibolak-balik argumentnya, asalkan keywordnya tetap maka akan memunculkan data yang benar seperti yang diminta. Seperti contoh dibawah ini
    ```python
    def greet_with_key(name,location):
        print(f"Hello {name}")
        print(f"You from {location}")
    greet_with_key(name="Tris", location="Ngawi")
    greet_with_key(location="Ngawi", name="Tris")
    ```  
    output
    ```python
    Hello Tris
    You from Ngawi
    Hello Tris
    You from Ngawi
    ```
### Code Exercise / Code Challenge

* [Function with inputs](./day-8-start.py)
* [Paint Area Calculator](./day-8-1-exercise.py)
* [Prime Number Checker](./day-8-2-exercise.py)
* [Self-Exercise Cipher Text Part 1](./self-caesar-cipher-1.py)
* [Cipher Text part 1](./caesar-cipher-1-end.py)
* [Self-Exercise Cipher Text Part 2](./self-caesar-cipher-2.py)
* [Cipher Text part 2](./caesar-cipher-2-end.py)