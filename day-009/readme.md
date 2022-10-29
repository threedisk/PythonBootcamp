## Day 009

### Yang dipelajari
* <details><summary>Dictionary. Ada key, ada value `{key:value}`</summary>

    ```python
    programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
    ```
    Mengambil data dari dictionary, dengan memanggil key
    ```python
    print(programming_dictionary["Function"])
    ```
    Menambahkan item baru ke dictionary
    ```python
    programming_dictionary["Loop"] = "The action of doing something over and over again."

    print(programming_dictionary)
    ```

    Membuat dictionary kosong, bisa juga digunakan untuk menghapus dictionary yang sudah berisi menjadi kosong
    ```python
    empty_dictionary = {}

    programming_dictionary = {}
    ```

    Mengubah sebuah item di dictionary, perintahnya sama dengan menambahkan item baru di dictionary
    ```python
    programming_dictionary["Bug"] = "a moth in your computer"
    ```

    Looping dalam dictionary
    ```python
    for key in programming_dictionary:
        #Print key dari dictionary saja
        print(key)
        #Akan melakukan printing value dari key
        print(programming_dictionary[key])
    ```
    Output:
    ```python
    Bug
    An error in a program that prevents the program from running as expected.
    Function
    A piece of code that you can easily call over and over again.
    Loop
    The action of doing something over and over again.
    ```
    </details>
### Code Exercise / Code Challenge
* [Dictionary](./dictionary-file.py)
* [Grading Program](./day-9-1-exercise.py)
