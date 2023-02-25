def main():
    qty = None
    cost = None

    def fetch_quantity():
        """
        Returns a number, any number
        """
        # ...

        return ...

    def fetch_cost():
        """
        Returns a number, any number
        """
        # ...

        return ...

    def compute_cost_per_quantity():
        try:
            qty = fetch_quantity()
        except Exception as exp:
          #Printing type of exception
            print(f"Exception: {exp}")
            #Quit the program after Exception
            exit()

        try:
            cost = fetch_cost()
        except Exception as exp:
            print(f"Exception: {exp}")

        try:
            cost_per_quantity = cost / qty
        except Exception as exp:
          #Printing type of exception
            print(f"Exception: {exp}")
            
            #Quit the program after Exception
            exit()

        return cost_per_quantity

    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a + b)
