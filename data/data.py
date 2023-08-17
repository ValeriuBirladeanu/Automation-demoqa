from dataclasses import dataclass


@dataclass
class Person:
    full_name:str = None
    email:str = None
    currents_address:str = None
    permanent_address:str = None