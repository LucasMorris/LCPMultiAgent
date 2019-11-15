from MultiAgentSim.ingredient import blueberries
from MultiAgentSim.ingredient import chocolate
from MultiAgentSim.ingredient import dough
from MultiAgentSim.ingredient import flour
from MultiAgentSim.ingredient import salt
from MultiAgentSim import timer

class incoming_storage:
    def __init__(self):
        self.initial_stock = [8,7,6,5,4]
        self.stock_blueberries_new = (self.initial_stock[1] + self.stock_blueberries + (blueberries.availibility * timer.clock_t))
        self.stock_chocolate_new = (self.initial_stock[2] + self.stock_chocolate + (chocolate.availibility * timer.clock_t))
        self.stock_dough_new = (self.initial_stock[3] + self.stock_doug + (dough.availibility * timer.clock_t))
        self.stock_flour_new = (self.initial_stock[4] + self.stock_flour + (flour.availibility * timer.clock_t))
        self.stock_salt_new = (self.initial_stock[5] + self.stock_salt (salt.availibility * timer.clock_t))

