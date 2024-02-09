from PyQt5 import QtWidgets, QtCore


class Ui_TicketingApp(object):
    def setupUi(self, TicketingApp):
        TicketingApp.setObjectName("TicketingApp")
        TicketingApp.resize(240, 320)

        self.centralwidget = QtWidgets.QWidget(TicketingApp)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(10, 10, 220, 300)
        self.stackedWidget.setObjectName("stackedWidget")

        # Page 0 - Buy Ticket
        self.page_buy_ticket = QtWidgets.QWidget()
        self.page_buy_ticket.setObjectName("page_buy_ticket")

        self.buy_ticket_label = QtWidgets.QLabel(self.page_buy_ticket)
        self.buy_ticket_label.setGeometry(30, 30, 160, 60)
        self.buy_ticket_label.setAlignment(QtCore.Qt.AlignCenter)
        self.buy_ticket_label.setObjectName("buy_ticket_label")

        self.buy_ticket_button = QtWidgets.QPushButton(self.page_buy_ticket)
        self.buy_ticket_button.setGeometry(60, 120, 120, 40)
        self.buy_ticket_button.setObjectName("buy_ticket_button")

        self.stackedWidget.addWidget(self.page_buy_ticket)

        # Page 1 - Source
        self.page_source = QtWidgets.QWidget()
        self.page_source.setObjectName("page_source")

        self.source_label = QtWidgets.QLabel(self.page_source)
        self.source_label.setGeometry(30, 30, 160, 20)
        self.source_label.setAlignment(QtCore.Qt.AlignCenter)
        self.source_label.setObjectName("source_label")

        self.source_combobox = QtWidgets.QComboBox(self.page_source)
        self.source_combobox.setGeometry(30, 60, 160, 30)
        self.source_combobox.setObjectName("source_combobox")

        self.next_button_source = QtWidgets.QPushButton(self.page_source)
        self.next_button_source.setGeometry(60, 120, 120, 40)
        self.next_button_source.setObjectName("next_button_source")

        self.stackedWidget.addWidget(self.page_source)

        # Page 2 - Destination
        self.page_destination = QtWidgets.QWidget()
        self.page_destination.setObjectName("page_destination")

        self.selected_source_label = QtWidgets.QLabel(self.page_destination)
        self.selected_source_label.setGeometry(30, 30, 160, 20)
        self.selected_source_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_source_label.setObjectName("selected_source_label")

        self.destination_label = QtWidgets.QLabel(self.page_destination)
        self.destination_label.setGeometry(30, 60, 160, 20)
        self.destination_label.setAlignment(QtCore.Qt.AlignCenter)
        self.destination_label.setObjectName("destination_label")

        self.destination_combobox = QtWidgets.QComboBox(self.page_destination)
        self.destination_combobox.setGeometry(30, 90, 160, 30)
        self.destination_combobox.setObjectName("destination_combobox")

        self.next_button_destination = QtWidgets.QPushButton(self.page_destination)
        self.next_button_destination.setGeometry(60, 150, 120, 40)
        self.next_button_destination.setObjectName("next_button_destination")

        self.stackedWidget.addWidget(self.page_destination)

        # Page 3 - Passenger
        self.page_passenger = QtWidgets.QWidget()
        self.page_passenger.setObjectName("page_passenger")

        self.selected_destination_label = QtWidgets.QLabel(self.page_passenger)
        self.selected_destination_label.setGeometry(30, 30, 160, 20)
        self.selected_destination_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_destination_label.setObjectName("selected_destination_label")

        self.ticket_price_label = QtWidgets.QLabel(self.page_passenger)
        self.ticket_price_label.setGeometry(30, 60, 160, 20)
        self.ticket_price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ticket_price_label.setObjectName("ticket_price_label")

        self.passenger_label = QtWidgets.QLabel(self.page_passenger)
        self.passenger_label.setGeometry(30, 90, 160, 20)
        self.passenger_label.setAlignment(QtCore.Qt.AlignCenter)
        self.passenger_label.setObjectName("passenger_label")

        self.passenger_spinbox = QtWidgets.QSpinBox(self.page_passenger)
        self.passenger_spinbox.setGeometry(30, 120, 160, 30)
        self.passenger_spinbox.setObjectName("passenger_spinbox")

        self.calculate_button = QtWidgets.QPushButton(self.page_passenger)
        self.calculate_button.setGeometry(60, 180, 120, 40)
        self.calculate_button.setObjectName("calculate_button")

        self.stackedWidget.addWidget(self.page_passenger)

        # Initialize QR Code Page
        self.qr_code_page = QtWidgets.QWidget()
        self.qr_code_page.setObjectName("qr_code_page")

        self.total_amount_label = QtWidgets.QLabel(self.qr_code_page)
        self.total_amount_label.setGeometry(30, 30, 160, 20)
        self.total_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_amount_label.setObjectName("total_amount_label")

        self.qr_code_label = QtWidgets.QLabel(self.qr_code_page)
        self.qr_code_label.setGeometry(30, 60, 160, 160)
        self.qr_code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qr_code_label.setObjectName("qr_code_label")

        self.stackedWidget.addWidget(self.qr_code_page)

        self.retranslateUi(TicketingApp)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TicketingApp)

    def retranslateUi(self, TicketingApp):
        _translate = QtCore.QCoreApplication.translate
        TicketingApp.setWindowTitle(_translate("TicketingApp", "TicketingApp"))

        # Page 0 - Buy Ticket
        self.buy_ticket_label.setText(_translate("TicketingApp", "Welcome to Smart Ticketing System!\nClick below to buy a ticket:"))
        self.buy_ticket_button.setText(_translate("TicketingApp", "Buy Ticket"))

        # Page 1 - Source
        self.source_label.setText(_translate("TicketingApp", "Select your source:"))
        self.next_button_source.setText(_translate("TicketingApp", "Next"))

        # Page 2 - Destination
        self.selected_source_label.setText(_translate("TicketingApp", "Selected Source:"))
        self.destination_label.setText(_translate("TicketingApp", "Select your destination:"))
        self.next_button_destination.setText(_translate("TicketingApp", "Next"))

        # Page 3 - Passenger
        self.selected_destination_label.setText(_translate("TicketingApp", "Selected Destination:"))
        self.ticket_price_label.setText(_translate("TicketingApp", "Ticket Price: $0"))
        self.passenger_label.setText(_translate("TicketingApp", "Select the quantity of passengers:"))
        self.calculate_button.setText(_translate("TicketingApp", "Calculate Amount"))

        # Initialize QR Code Page
        self.total_amount_label.setText(_translate("TicketingApp", "Total Amount: $0"))
