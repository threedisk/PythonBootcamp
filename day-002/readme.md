## Day 002

### Yang dipelajari
1. Tipe data : beberapa tipe data seperti string, integer, float dan boolean, dan masih banyak lagi
2. Type error : Error dikarenakan beda type data dalam memasukkan ke fungsi. Contoh fungsi len tidak akan bisa digunakan dalam integer / integer tidak ada fungsi len.
3. Operasi matematika dalam python ( penjumlahan menggunakan + , pengurangan menggunakan - , perkalian menggunakan * , pembagian menggunakan / dan pangkat menggunakan ** ). Jika operasi menggunakan multi operator maka harus menggunakan prinsip PEMDAS : ( Parentheses/tanda kurung , Exponents, Multiplication, Division, Addition, Subtraction)
4. Number manipulation and F Strings in python: Memanipulasi angka dan F String di python
```
result = 4 / 2 # 4 dibagi 2 menjadi 2
result /= 2    # 2 dibagi 2 menjadi 1
print(result)  # disini akan menghasilkan angka 1

CONTOH LAIN 

score = 0       # nilai awal 0
score += 1      # nilai ditambah 1
print (score)   # nilai akan menjadi 1

Digunakan untuk memaipulasi nilai
```
F-String 
Dengan menambahkan f didepan string maka akan menjadi lebih mudah dengan menambahkan tanda kurung kurawal dan variabelnya

```
score = 0
height = 1.8 
isWinning= True

# Perintah dibawah menghasilkan output yang sama tapi berbeda ribet-nya
print("=================")
print ("Your score is "+str(score)+",your height is "+str(height)+",you are winning is "+str(isWinning))
print("=================")
print(f"Your score is {score},your height is {height},you are winning is {isWinning} ")
```
### Split Bill Calculator

### Split Bill Calculator Code
```
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Selamat datang di program kalkulator tip")
tagihan = float(input("Berapa tagihan Anda? Rp. "))
tip = int(input("Berapa tip yang akan diberikan kepada waiter?"))
orang = int(input("Berapa jumlah orang? "))
persen_tip = tip / 100
total_tagihan_perorang = tagihan / orang
tagihan_orang = (total_tagihan_perorang)
total_tagihan_tip = float(total_tagihan_perorang) + (
    total_tagihan_perorang * persen_tip)
tagihan_tip = (format(total_tagihan_tip, '.2f'))

print(
    f"Total tagihan untuk {orang} orang adalah {tagihan}, \ndengan rincian perorang masing-masing {total_tagihan_perorang},\nditambah dengan tip sebesar {tip}%, \nmaka untuk setiap orang harus membayar {tagihan_tip}"
)
```