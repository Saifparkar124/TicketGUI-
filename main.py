import tkinter as tk
from datetime import datetime, timedelta
from io import BytesIO
from tkinter import ttk
import razorpay
import requests
from PIL import Image, ImageTk

razorpay_api_key = "rzp_test_x9yYe7svYVyyaf"
razorpay_api_secret = "6ezRz0C51xRKaRAjVvTL2H5w"
client = razorpay.Client(auth=(razorpay_api_key, razorpay_api_secret))


def get_accessible_routes(source):
    routes = {
        "Pune": {"Mumbai": 50, "Nashik": 30, "Kolhapur": 80},
        "City B": {"Destination 1": 60, "Destination 2": 40, "Destination 3": 70},
        "City C": {"Destination X": 55, "Destination Y": 45, "Destination Z": 65}
    }
    return list(routes.get(source, {}).keys())


def get_ticket_price(source, destination):
    ticket_prices = {
        "Pune": {"Mumbai": 50, "Nashik": 30, "Kolhapur": 80},
        "City B": {"Destination 1": 60, "Destination 2": 40, "Destination 3": 70},
        "City C": {"Destination X": 55, "Destination Y": 45, "Destination Z": 65}
    }
    return ticket_prices.get(source, {}).get(destination, 0)


class TicketingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Ticketing System")
        self.source_combobox = ttk.Combobox(self.root, values=["Pune", "City B", "City C"], state="readonly",
                                            font=("Arial", 8))
        self.destination_combobox = None
        self.qr_code_image_label = None
        self.photo_image = None
        self.passenger_quantity = tk.IntVar()
        self.passenger_quantity.set(1)

        self.show_buy_ticket_page()

    def show_buy_ticket_page(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to Smart Ticketing System!\nClick below to buy a ticket:",
                 font=("Arial", 10)).pack(pady=10)
        tk.Button(self.root, text="Buy Ticket", command=self.show_source_page, font=("Arial", 8)).pack()

    def show_source_page(self):
        self.clear_window()
        tk.Label(self.root, text="Select your source:", font=("Arial", 8)).pack(pady=5)
        self.source_combobox.set("Pune")
        self.source_combobox.pack(pady=5)
        tk.Button(self.root, text="Next", command=self.show_destination_page, font=("Arial", 8)).pack()

    def show_destination_page(self):
        self.clear_window()
        selected_source = self.source_combobox.get()
        tk.Label(self.root, text=f"Selected Source: {selected_source}", font=("Arial", 8)).pack(pady=5)
        accessible_routes = get_accessible_routes(selected_source)
        tk.Label(self.root, text="Select your destination:", font=("Arial", 8)).pack(pady=5)
        self.destination_combobox = ttk.Combobox(self.root, values=accessible_routes, state="readonly",
                                                 font=("Arial", 8))
        self.destination_combobox.set(accessible_routes[0])
        self.destination_combobox.pack(pady=5)
        tk.Button(self.root, text="Next", command=self.show_passenger_page, font=("Arial", 8)).pack()

    def show_passenger_page(self):
        self.clear_window()
        selected_destination = self.destination_combobox.get()
        ticket_price = get_ticket_price(self.source_combobox.get(), selected_destination)

        tk.Label(self.root, text=f"Selected Destination: {selected_destination}", font=("Arial", 8)).pack(pady=5)
        tk.Label(self.root, text=f"Ticket Price: ${ticket_price}", font=("Arial", 8)).pack(pady=5)
        tk.Label(self.root, text="Select the quantity of passengers:", font=("Arial", 8)).pack(pady=5)

        tk.Spinbox(self.root, from_=1, to=10, textvariable=self.passenger_quantity, font=("Arial", 8)).pack(pady=5)
        tk.Button(self.root, text="Calculate Amount", command=self.calculate_amount, font=("Arial", 8)).pack()

    def calculate_amount(self):
        total_amount = get_ticket_price(self.source_combobox.get(),
                                        self.destination_combobox.get()) * self.passenger_quantity.get()
        self.clear_window()
        tk.Label(self.root, text=f"Total Amount: ${total_amount}", font=("Arial", 8)).pack(pady=10)
        self.generate_qr_code(total_amount)

    def generate_qr_code(self, total_amount):
        try:
            close_by_timestamp = int((datetime.now() + timedelta(minutes=15)).timestamp())
            qr_code_data = dict(type="upi_qr", name="Store Front Display", usage="single_use", fixed_amount=True,
                                payment_amount=total_amount * 100, description="For Store 1",
                                close_by=close_by_timestamp, notes=dict(purpose="Test UPI QR Code notes"))
            qr_code = client.qrcode.create(data=qr_code_data)
            image_url = qr_code.get("image_url", "")
            response = requests.get(image_url)
            image_data = Image.open(BytesIO(response.content))
            self.photo_image = ImageTk.PhotoImage(image_data)
            tk.Label(self.root, image=self.photo_image, font=("Arial", 8)).pack()
            print("QR code image displayed successfully.")

        except razorpay.errors.BadRequestError as e:
            print(f"Error creating QR code: {e}")
            print(f"Details: {e.__dict__}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketingApp(root)
    root.mainloop()
