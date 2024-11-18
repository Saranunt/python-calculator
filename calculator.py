class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # return b - a
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            a = -a
            b = -b
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            return "ZeroDivisionError"
            #raise ZeroDivisionError("Division by zero is not allowed.")
        
        sign = 1
        if (a < 0) != (b < 0):
            sign = -1
            if b<0: 
                b = -b
            if a<0: 
                a = -a

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = result + 1
        return result * sign
    
    def modulo(self, a, b):
        if b == 0:
            return "ZeroDivisionError"
            #raise ZeroDivisionError("Modulo by zero is not allowed.")
        
        sign = 0
        if (a < 0) != (b < 0):
            if a < 0: 
                a = -a
                sign = -1
            if b < 0: 
                b = -b
                sign = 1

        while a >= b:
            a = a - b
        return (a-b)*sign if (sign != 0) else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, -2))
    print("Example: modulo: ", calc.modulo(-10, 3))