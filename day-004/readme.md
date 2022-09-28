## Day 004

### Yang dipelajari
* Random Module menggunakan 
```python
import random
```
* List , index dimulai dari 0, untuk mengambil data terakhir dari list menggunakan -1.
```python
fruits = [item1,item2]
```
* Menambahkan item menggunakan append `list.append()`
* Memotong string menggunakan split
```python
names = ("My Name", "is", "Khan")
splitted_name = names.split(",")
print(splitted_name)
```
* Nested List
```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    
dirty_dozen = [fruits, vegetables]    
print(dirty_dozen[0])
print(dirty_dozen[1])
print("=======")
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
```
Hasil
```
['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
=======
Tomatoes
Celery
```
### Code Exercise and Challenge
* [Heads or Tails Randomizer](./day-4-1-exercise.py)
* [Siapa yang traktir makan Randomizer](./day-4-2-exercise.py)
* [Hide your treasure](./day-4-3-exercise.py)
* [Jan-ken-pon / Rock Paper Scissors](./day-4-rock-paper-scissors-start.py)