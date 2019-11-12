# Affordance Handler
# Reads affordances from the environment, 
# modifying belief memory according to each entity properties.
class AffordanceHandler:

    def __init__(self, affordances):
        self.afford = affordances

    def check_affordances(self, belief):
        # For now check object affordances.
        # Beliefs are of the form:
        # AGT BELIEVES OBJ
        obj = belief[2]
        for sublist in self.afford:
            if sublist[0] == obj:
                # Object has an affordance.
                belief.append(sublist[1])
                break
        return belief
