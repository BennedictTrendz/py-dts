# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='ardhianto.hari@pajak.go.id'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  pass
     hasil = []
    for item in items:
        if item[0]==letter:
            hasil.append(item)
    return hasil

#Graded

def counter_item(items):
  pass
   itung ={}
    for item in items:
        if item in itung:
            itung[item] += 1
        else:
            itung[item] = 1
    return(itung)

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {}
for i in range(len(fruits)):
    fruit_price[fruits[i]] = prices[i]

def total_price(dcounter,fprice):
    pass
    prizeSum = 0
    for key, value in dcounter.items():
        prizeSum += fprice[key]*value
    return prizeSum

#Graded

def discounted_price(total,discount,minprice=100):
  pass
      if total < minprice:
        bayar = total
    else:
        disc = 100 - discount
        bayar = (total*disc/100)
    return bayar


#Graded

def print_summary(items,fprice):
  pass
  countItem = counter_item(items)
    total = total_price(countItem,fruit_price)
    for key,value in sorted(countItem.items()):
        print(value,key,":",fprice[key]*value)
    print("total :",total)
    print("discount price :",discounted_price(total,10,minprice=100))
