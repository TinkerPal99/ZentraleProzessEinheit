import queue

from Dispatcher.library import job


class Priorisator:
    # Priorisator (Jobprocessor) empfängt das jobpaket des Kontrolltools und verarbeitet diese nach der priorisierung
    def __init__(self):

        self.adress = ""
        self.jobdescription = dict
        self.job_q = queue.Queue()
        self.job_l = None
        self.client = None

    def put(self, newjob=job.job):
        self.job_q.put(newjob)

    def organize(self):
        # nimmt job aus der queue, organisiert diesen dann, je nach Prio, in die outputlist
        job_item = self.job_q.get()
        if job_item["Prio"] == 1:
            self.job_l.insert(2, job_item)
            # TODO Idee: je prio eine Liste, if list1 isempty -> look at next list
        else:
            self.job_l.insert(-1, job_item)

    def get(self):
        return self.job_l.pop()

