from MultiAgentSim.ingredient import blueberries
from MultiAgentSim.ingredient import chocolate
from MultiAgentSim.ingredient import dough
from MultiAgentSim.ingredient import flour
from MultiAgentSim.ingredient import salt
#, blueberries, chocolate, dough, flour, salt
class ingredients:

    def __init__(self):
        self.incoming_stocks = [blueberries.incoming_stock, chocolate.incoming_stock, dough.incoming_stock, flour.incoming_stock, salt.incoming_stock]
        self.ingredient_availability = [blueberries.availability, chocolate.availability, dough.availability, flour.availability, salt.availability]