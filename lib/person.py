#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    def __init__(self, job, name = "Guido",):
        self.name = name.title()
        self.job = job.title()

    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name.title()
        elif not name:
            print("Name must be string between 1 and 25 characters.")
        else:
            print('Name must be string between 1 and 25 characters.')

    def set_job(self, job):
        if job.title() in Person.APPROVED_JOBS:
            self._job = job.title
        else:
            print("Job must be in list of approved jobs.")