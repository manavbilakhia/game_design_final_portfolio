

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
                              ('change_color', lambda:self.change_color())])

        self.fsm.add_transitions('looping', [(self.test_on_green, 'wandering'),(self.test_on_change_state,'change_color'),(self.test_on_corner, 'freezing') ])
        self.fsm.add_transitions('wandering', [(self.test_on_red, 'looping'),(self.test_on_change_state,'change_color'),(self.test_on_corner, 'freezing')])
        self.fsm.add_transitions('change_color',[(self.test_on_red, 'looping'), (self.test_on_green, 'wandering')])





    def test_on_green (self, world):
        print(id(self), self.p.x, "test on green")
        if self.p.x <= world.width/2:
            return True
        else:
            return False


    def execute_actions (self):

        self.steering = []
        print("current state: ", self.fsm.current_state)

        action = self.fsm.states[self.fsm.current_state]
        action()

        self.apply_steering ()


    def test_on_red (self, world):
        print(id(self), self.p.x, "test on red")
        if self.p.x > world.width/2:
            return True
        else:
            return False



    #test to see if the agent is within 2 body radii of any of the corners of the game world.
    def test_on_corner (self, world):

            if (self.p.x < self.r*5) or (self.p.y < self.r*5) or (self.p.x > world.width - self.r*5) or (self.p.y > world.height - self.r*5):
                print(id(self), self.p.x, "test on corner")
                return True
            else:
                return False

    def test_on_change_state (self, world):
        if abs(self.p.x - world.width/2) < 2:
            print("in change state color")
            return True
        else:
            return False