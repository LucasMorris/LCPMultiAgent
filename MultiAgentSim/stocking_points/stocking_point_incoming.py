from MultiAgentSim.ingredient import ingredients
from MultiAgentSim import timer
#This importing gives me error messages.

class incoming_storage:
    def __init__(self):
        self.incoming_stocks_list = []

    def incoming_stock_change():
        number_ingredients = len(ingredients.incoming_stocks)
        for i in range(0, number_ingredients):
            if timer.clock_t < 0:
                ingredients.incoming_stocks(i)[timer.clock_t] = ingredients.incoming_stocks(i)[timer.clock_t - 1] + ingredients.ingredient_availability(i)[timer.clock_t]  # -outgoing_bb[timer.clock_t]
            else:
                ingredients.incoming_stocks(i)[timer.clock_t] = ingredients.incoming_stocks(i)[timer.clock_t] + ingredients.ingredient_availability(i)[timer.clock_t]   # -outgoing_bb[timer.clock_t]
            print(ingredients.incoming_stocks)


#Below this there are just old notes that we can delete if my idea was good

        #self.initial_stock = [8,7,6,5,4]
        #self.stock_blueberries_accumulated = (self.initial_stock[0] + (blueberries.availibility * timer.clock_t))
        #self.stock_chocolate_accumulated = (self.initial_stock[1] + (chocolate.availibility * timer.clock_t))
        #self.stock_dough_accumulated = (self.initial_stock[2] + (dough.availibility * timer.clock_t))
        #self.stock_flour_accumulated = (self.initial_stock[3] + (flour.availibility * timer.clock_t))
        #self.stock_salt_accumulated = (self.initial_stock[4] + (salt.availibility * timer.clock_t))


#stock_chocolate = []
#stock_dough = []
#stock_flour = []
#stock_salt = [] #We should put these into the ingredient classes to be able to call upon them easier.
#ingredient_stocks =[stock_blueberries, stock_chocolate, stock_dough, stock_flour, stock_salt]

#Now in ingredients
#ingredient_incoming_stocks = [blueberries.incoming_stock, chocolate.incoming_stock, dough.incoming_stock, flour.incoming_stock, salt.incoming_stock]
#ingredient_availability = [blueberries.availability, chocolate.availability, dough.availability, flour.availability, salt.availability]