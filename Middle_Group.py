import sqlite3

# Middleware / Database Manager
class DatabaseManager:
    def __init__(self, db_name="order.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create Customers table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL
            )
        ''')

        # Create Orders table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                food_name TEXT NOT NULL,
                meat_choice TEXT,
                price REAL NOT NULL,
                FOREIGN KEY(customer_id) REFERENCES Customers(id)
            )
        ''')

        self.conn.commit()

    def add_customer(self, person):
        self.cursor.execute('''
            INSERT INTO Customers (name, phone, email, address)
            VALUES (?, ?, ?, ?)
        ''', (person.name, person.phone, person.email, person.address))
        self.conn.commit()
        return self.cursor.lastrowid  # Return the new customer's ID

    def add_order(self, customer_id, food):
        self.cursor.execute('''
            INSERT INTO Orders (customer_id, food_name, meat_choice, price)
            VALUES (?, ?, ?, ?)
        ''', (customer_id, food.name, food.meat, food.price))
        self.conn.commit()

    def close(self):
        self.conn.close()
