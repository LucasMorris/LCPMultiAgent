from MultiAgentSim.ingredient import blueberries
from MultiAgentSim import timer

class incoming_storage:
    def __init__(self):
        self.initial_stock = 0
        self.stock_blueberries = (self.initial_stock + (blueberries.availibility * timer.clock_t))


