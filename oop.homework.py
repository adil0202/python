
#№1
# class Timer:
#     def __init__(self):
#         self.seconds = 0
        
#     def add(self, value):
#         self.seconds += value
        
#     def resert(self):
#         self.seconds = 0
        
#     def get_time(self):
#         minuts = self.seconds // 60
#         seconds = self.seconds % 60
#         return f"{minuts:02d}:{seconds:02d}"
    
# timer = Timer()
# timer.add(65)
# print(timer.get_time())

# №2
# class Playlist:
#     def __init__(self):
#         self.songs = []
        
#     def add_song(self, title):
#         self.songs.append(title)
        
#     def remove_song(self, title):
#         if title in self.songs:
#             self.songs.remove(title)
#         else:
#             print("Такой песни нет в плейлисте")
            
#     def count(self):
#         return len(self.songs)
    
#     def show(self):
#         if not self.songs:
#             print("Плейлист пуст")
#         else:
#             print("Плейлист:")
#             for i, song in enumerate(self.songs, start=1):
#                 print(f"{i}. {song}")
                
# playlist = Playlist()
# playlist.add_song("Snape of You")
# playlist.add_song("RedBull 64 Bars")
# playlist.show()
# print("Количество песен:", playlist.count())

# playlist.remove_song("Snape of You")
# playlist.show()



# №3
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
#     def get_total_price(self):
#         return self.price * self.quantity
    
    
# class ShopCart:
#     def __init__(self):
#         self.items = []
        
#     def add_product(self,product):
#         self.items.append(product)
        
#     def remove_product_by_name(self, name):
#         for product in self.items:
#             if product.name == name:
#                 self.items.remove(product)
#                 return
#             print("Продукт не найден")
            
#     def get_total(self):
#         total = 0
#         for product in self.items:
#             total += product.get_total_price()
#             return total
        
# p1 = Product("Хлеб", 150, 2)
# p2 = Product("Молоко", 400, 1)
# cart = ShopCart()
# cart.add_product(p1)
# cart.add_product(p2)

# print("Сумма", cart.get_total)

# cart.remove_product_by_name("хлеб")
# print("Сумма после удаления:", cart.get_total())




# №4
# class SafeBankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Ошибка")
            
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Ошибка")
            
#     def get_balance(self):
#         return self.balance
    
    
# account = SafeBankAccount("Adil", 1000)

# account.deposit(500)
# print(account.get_balance())

# account.withdraw(300)
# print(account.get_balance())

# account.withdraw(5000) 


