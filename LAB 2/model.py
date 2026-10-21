class ClassroomAgent:
    def __init__(self):
     
        self.previous_mode = None

    def act(self, temp, occupied):

        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"


        if target_mode == self.previous_mode:
            send_command = False
        else:
            send_command = True
            self.previous_mode = target_mode  # Update state only when command changes

        return target_mode, send_command



if __name__ == "__main__":
    agent = ClassroomAgent()
    
   
    percepts = [
        (29, True),   
        (29, True),   
        (20, True),   
        (26, True),   
        (19, True), 
        (29, False) 
    ]

    print(f"{'Step':>4} | {'Percept (Temp, Occupied)':<25} | {'Target Mode':^11} | {'Send Command?':^13}")
    print("-" * 62)
    for step, percept in enumerate(percepts, 1):
        target, command = agent.act(*percept)
        print(f"{step:>4} | {str(percept):<25} | {target:^11} | {str(command):^13}")
    