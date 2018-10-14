class Shop:
    def __init__(self):
        self.ary_products = {
            "apple" : 2.1,
            "banana" : 1.09,
            "beef" : 4.3,
            "pork" : 4.4,
            "milk" : 1.2,
            "belt fish" : 3.2,
            "yellow fish" : 5.6,
            "eggs" : 4.3,
            "cabbiage" : 1.1,
            "seaweed" : 1.2,
            "mantou" : 2.1,
            "baozi" : 2.2,
            "toufu" : 3.2
        }

    def print_recepit(self, shop_items):
        print("in print_recepit\n")
        print(self.ary_products)


        print("---warmart shopping recepit---")
        print("10/13/2018 7:49pm\n")
        sum = 0

        for i in shop_items:
            if i in self.ary_products:
                sum += self.ary_products[i]
                print(str(i) + " : " + "$" + str(self.ary_products[i]))
        print("sum={}".format(sum))
        print("\nthank you!")
                

def start_test():
    shopWalmart = Shop()

    shop_items = []
    shop_items.append("eggs")
    shop_items.append("apple")
    shop_items.append("milk")

    shopWalmart.print_recepit(shop_items)

start_test()
