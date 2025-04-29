import tkinter as tk
from tkinter import messagebox

# Menu items
menu = {
    "Taco": 4,
    "Supreme Taco": 5,
    "Quesadilla": 8,
    "Burrito": 12,
    "Nachos": 12,
    "Arroz con Pollo": 12
}

meats = ["Steak", "Chicken", "Pastor", "Chorizo", "Ground Beef"]
TAX_RATE = 0.07  # 7% sales tax

# Food Class
class Food:
    def __init__(self, name, price, meat=""):
        self.name = name
        self.price = price
        self.meat = meat

# Customer Class
class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# GUI Class
class FoodTruckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mil Amores Food Truck Ordering System")

        self.cart = []

        # Customer Information Section
        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Label(root, text="Phone:").grid(row=1, column=0)
        tk.Label(root, text="Email:").grid(row=2, column=0)
        tk.Label(root, text="Address:").grid(row=3, column=0)

        self.name_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)
        self.email_entry = tk.Entry(root)
        self.address_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.address_entry.grid(row=3, column=1)

        # Food Menu Section
        tk.Label(root, text="Select Food:").grid(row=5, column=0)
        self.food_var = tk.StringVar(root)
        self.food_var.set("Taco")  # Default value

        self.food_menu = tk.OptionMenu(root, self.food_var, *menu.keys())
        self.food_menu.grid(row=5, column=1)

        # Meat Options
        tk.Label(root, text="Select Meat:").grid(row=6, column=0)
        self.meat_var = tk.StringVar(root)
        self.meat_var.set(meats[0])

        self.meat_menu = tk.OptionMenu(root, self.meat_var, *meats)
        self.meat_menu.grid(row=6, column=1)

        # Add to Cart Button
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).grid(row=7, column=0, pady=5)

        # Remove Last Item Button
        tk.Button(root, text="Remove Last Item", command=self.remove_last_item).grid(row=7, column=1, pady=5)

        # Cart Display
        self.cart_display = tk.Text(root, width=40, height=10)
        self.cart_display.grid(row=8, column=0, columnspan=2)

        # Checkout Button
        tk.Button(root, text="Checkout", command=self.checkout).grid(row=9, column=0, columnspan=2, pady=10)

    def add_to_cart(self):
        food_name = self.food_var.get()
        meat_choice = self.meat_var.get()
        price = menu[food_name]
        food_item = Food(food_name, price, meat_choice)
        self.cart.append(food_item)
        self.update_cart_display()

    def remove_last_item(self):
        if self.cart:
            self.cart.pop()
            self.update_cart_display()
        else:
            messagebox.showwarning("Warning", "Cart is already empty!")

    def update_cart_display(self):
        self.cart_display.delete(1.0, tk.END)
        total = 0
        for item in self.cart:
            self.cart_display.insert(tk.END, f"{item.name} ({item.meat}) - ${item.price}\n")
            total += item.price
        tax = total * TAX_RATE
        grand_total = total + tax
        self.cart_display.insert(tk.END, f"\nSubtotal: ${total:.2f}\nTax: ${tax:.2f}\nTotal: ${grand_total:.2f}")

    def checkout(self):
        if not self.cart:
            messagebox.showerror("Error", "Your cart is empty!")
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not (name and phone and email and address):
            messagebox.showerror("Error", "Please complete all customer information fields.")
            return

        customer = Person(name, phone, email, address)
        messagebox.showinfo("Order Placed", f"Thank you {customer.name}! Your order has been placed.")

        # Reset
        self.cart.clear()
        self.update_cart_display()
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodTruckApp(root)
    root.mainloop()