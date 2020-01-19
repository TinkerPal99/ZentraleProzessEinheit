class job:
    def __init__(self):
        self.jobdescription = {"Destination": None,
                               "Prio": None,
                               "Job": None}

    def sync(self, input):
        self.jobdescription.update(input)
