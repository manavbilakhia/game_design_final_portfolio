

from steering_character import BeakBall
from fsm import FSM

class FSMBeakBall (BeakBall):

    def __init__ (self, x, y, r, m, color, xv, yv):

        BeakBall.__init__(self, x, y, r, m, color, xv, yv)

        self.fsm = FSM()

        # green - wander; red - run
        #if the agent is in the "green" zone it wanders if the agent is in the "red" zone it loops
        self.fsm.add_states ([('wandering', lambda:self.wander(1.0/30)),
                              ('looping', lambda:self.loop(1.0/30)),
                              ('freezing', lambda: self.freeze()),
                              ('change_color', lambda:self.change_color())
                              ])

        self.fsm.add_transitions('wandering', [(self.test_on_red, 'looping'),])
        self.fsm.add_transitions('looping', [(self.test_on_green, 'wandering')])


    def execute_actions (self):

        self.steering = []

        action = self.fsm.states[self.fsm.current_state]
        action()

        self.apply_steering ()


    def test_on_red (self, world):

        if self.p.x > world.width/2:
            self.transitioned = True
            return True
        else:
            return False

    def test_on_green (self, world):

        if self.p.x <= world.width/2:
            self.transitioned = True
            return True
        else:
            return False

    #test to see if the agent is within 2 body radii of any of the corners of the game world.
    def test_on_corner (self, world):

            if (self.p.x < self.r*5) or (self.p.y < self.r*5) or (self.p.x > world.width - self.r*5) or (self.p.y > world.height - self.r*5):
                return True
            else:
                return False

    def test_on_change_state (self, world):
        if abs(self.p.x - world.width/2) < 4:
            print("in change state")
            return True
        else:
            return False