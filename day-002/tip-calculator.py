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