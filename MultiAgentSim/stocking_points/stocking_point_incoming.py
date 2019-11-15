from MultiAgentSim.ingredient import blueberries
from MultiAgentSim.ingredient import chocolate
from MultiAgentSim.ingredient import dough
from MultiAgentSim.ingredient import flour
from MultiAgentSim.ingredient import salt
from MultiAgentSim import timer

class incoming_storage:
    def __init__(self):
        self.initial_stock = [8,7,6,5,4]
        self.stock_blueberries_accumulated = (self.initial_stock[0] + (blueberries.availibility * timer.clock_t))
        self.stock_chocolate_accumulated = (self.initial_stock[1] + (chocolate.availibility * timer.clock_t))
        self.stock_dough_accumulated = (self.initial_stock[2] + (dough.availibility * timer.clock_t))
        self.stock_flour_accumulated = (self.initial_stock[3] + (flour.availibility * timer.clock_t))
        self.stock_salt_accumulated = (self.initial_stock[4] + (salt.availibility * timer.clock_t))



stock_bb = [] #There is a way in python to create a function via def, that substitute words based on inputs. So we could write stock_ingredientname and substitute "ingredient name" based on a list.
if timer.clock_t < 0:
    stock_bb[timer.clock_t] = stock_bb[timer.clock_t - 1] + outgoing_bb[timer.clock_t] - incoming_bb[timer.clock_t]
    #The list incoming has to be defined here with help of the availability variable. The list outgoing has to be defined in oven.
else stock_bb[timer.clock_t] = outgoing_bb[timer.clock_t] - incoming_bb[timer.clock_t]

incoming_bb = blueberries.availability #At the moment this value is independent from clock_t. We could change that by making it random.