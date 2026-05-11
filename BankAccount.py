class BankAccount:
    def __init__(self, balance, owner, pin):
        self.__balance = balance
        self.__owner = owner  
        self.__pin = pin
        
    def deposit(self, amount, pin):
        if self.__validate_pin(pin) and self.__is_positive(amount):
            self.__balance += amount
        
    def withdraw(self, amount, pin):
        if self.__validate_pin(pin) and self.__is_positive(amount) and self.__balance>=amount:
            self.__balance -= amount
        
    def get_balance(self, pin):
        if self.__validate_pin(pin):
            return self.__balance
        
    def __validate_pin(self, pin):
        if pin == self.__pin:
            return True
        else:
            raise ValueError("Неправильный пароль")
        
    def __is_positive(self, amount):
        if amount > 0:
            return True
        else:
            raise ValueError("Нужно больше нуля")
            
emp = BankAccount(40, "John", "1234")   
emp.withdraw(2000, "1234")     

