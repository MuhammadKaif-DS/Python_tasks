import csv
from datetime import datetime

# Logging helper
def write_log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp} {message}\n")

class Order:
    products_file = "product.csv"
    discount_rate = 0  

    def __init__(self):
        self.items = []

    # Decorator for logging method execution
    @staticmethod
    def log_action(func):
        def wrapper(self, *args, **kwargs):
            write_log(f"Executed {func.__name__}")
            return func(self, *args, **kwargs)
        return wrapper

    @log_action
    def add_item_by_id(self, product_id, quantity):
        if not Order.is_valid_product_id(product_id):
            write_log(f"Invalid product ID attempt: {product_id}")
            return

        with open(Order.products_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['id']) == product_id:
                    name = row['name']
                    price = float(row['price'])
                    total = price * quantity
                    self.items.append({'name': name, 'quantity': quantity, 'total': total})
                    write_log(5*'*'*5)
                    write_log(f"Added item: {name} (x{quantity}) - Total: {total}")
                    write_log(5*'*'*5)
                    break

    @log_action
    def calculate_total(self):
        subtotal = sum(item['total'] for item in self.items)
        discount = Order.discount_rate / 100
        total = subtotal * (1 - discount)
        write_log(5*'*'*5)
        write_log(f"Calculated total with discount: {total}")
        return total

    @classmethod
    def set_discount(cls, discount_rate):
        cls.discount_rate = discount_rate
        write_log(f"Discount set to {discount_rate}%")

    @staticmethod
    def is_valid_product_id(product_id):
        with open(Order.products_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['id']) == product_id:
                    return True
        return False         
    
# Create an order
order = Order()

# Add valid items
order.add_item_by_id(3, 2)  # hedphone × 2
order.add_item_by_id(4, 3)  # Mouse × 3

# Add invalid item
order.add_item_by_id(99, 1)  # Invalid ID

# Apply discount
Order.set_discount(10)

# Calculate total
total = order.calculate_total()
print(f"Final total after discount: ${total}")