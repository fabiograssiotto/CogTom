# Intention Handler
# Handles intentions from the environment, 
# modifying belief memory according to the interpretation 
# of the agent intention.
class IntentionHandler:

    def __init__(self, intentions):
        self.intentions = intentions

    def getintentions(self):
        return self.intentions

    def check_intentions(self, belief):
        # Next step is to analyse INTENTIONS and verify Beliefs that could be 
        # modified based on intentions detected in the environment.

        blf_agt = belief[0]
        blf_obj = belief[2]
        blf_afd = belief[3]

        for intention in self.intentions:
            agt = intention[0]
            intent = intention[1]
            obj = intention[2]

            # Some intentions affect directly the agent, such as movement.
            # ie Mary Moves Self to bathroom.
            if (obj == 'Self'):
                # Set the object as the same as the agent.
                obj = agt
            
            tgt = intention[3]

            if (blf_obj == obj):
                # ie we only need to analyse an intention 
                # if the object is the same as the object in the current belief.
                belief = self.map_intention(intent, agt, obj, tgt, belief)

        if (len(belief) == 4):
            # Belief does not have a target object, set as None.
            belief.append('None')

        return belief

    def map_intention(self, intent, agt, obj, tgt, belief):
        mapper = {
            'None': self.skip,
            'ReachFor': self.reachFor,
            'Puts': self.put,
            'Gets': self.get,
            'Go': self.go,
            'Give': self.give,
            'Exits': self.skip,
            'Enters': self.skip,
            'Search': self.skip
        }
        # Get the function from mapper dictionary
        func = mapper.get(intent)
        # Execute the function
        return func(agt, obj, tgt, belief)

    def skip(self, agt, obj, tgt, belief):
        # Nothing to do
        return belief

    def reachFor(self, agt,obj, tgt, belief):
        # Reaching for an object results
        # on the object ending up on the agent hand.
        belief[3] = 'OnHand'
        belief.append('Of ' + agt)
        return belief
    
    def put(self, agt, obj, tgt, belief):
        belief[3] = 'HiddenIn'
        belief.append(tgt)
        return belief

    def get(self, agt, obj, tgt, belief):
        belief[3] = 'OnHand'
        belief.append('Of ' + agt)
        return belief

    def go(self, agt, obj, tgt, belief):
        belief[3] = 'Went to'
        belief.append(tgt)
        return belief

    def give(self, agt, obj, tgt, belief):
        belief[3] = 'Was Given to'
        belief.append(tgt)
        return belief
