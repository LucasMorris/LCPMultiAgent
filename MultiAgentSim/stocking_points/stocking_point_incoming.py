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



stock_bb = []
if timer.clock_t < 0:
    stock_bb[timer.clock_t] = stock_bb[timer.clock_t - 1] + push[timer.clock_t] - pull[timer.clock_t]
else stock_bb[timer.clock_t] = push[timer.clock_t] - pull[timer.clock_t]