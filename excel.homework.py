#  №1
# try:
#     a = float(input("Введите число a: "))
#     b = float(input("Введите число b: "))
    
#     result = a / b
#     print("Результат:", result)
    
# except ValueError:
#     print("Ошибка: введено не число")
    
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль")
    
# finally:
#     print("Завершено")

# №2
# class Product:
#     def __init__(self, title, price, quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity
        
#     def line_total(self):
#         return self.price * self.quantity

# product = []
# total_sum = 0

# df = pd.read_excel("products.xlsx")

# for _, row in df.iterrows():
#     try:
#         title = row["Title"]
#         price = float(row["Price"])
#         quantity = int(row[quantity])
        
#         product = Product(title, price, quantity)
#         line_total = product.line_total()
        
#         product.append({
#             "Title": title,
#             'LineTotal': line_total
#         })
        
#         total_sum += line_total
        
#     except (ValueError, TypeError):
#         continue
    
# product.append({
#     "Title": "TOTAL",
#     "LineTotal": total_sum
# })

# report_df = pd.DataFrame(product)
# report_df.to_excel("products_report.xlsx", index=False)

