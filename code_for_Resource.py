from dataclasses import dataclass,field
from typing import Optional
from enum import Enum,auto
from datetime import date

class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()

@dataclass
class Resource:
    "Media resource description"
    identifier : str
    title:str = '<untitled>'
    creators:list = field(default_factory=list)
    date : Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description : str =''
    language: str = ''
    subjects : list = field(default_factory=list)

description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9','Refactoring , 2nd Edition',
                ['Martin Fowler','Kent Beck'],date(2018,11,10),
                ResourceType.BOOK,description,'EN',
                ['computer programming','oop'])
print(book) #Resource(identifier='978-0-13-475759-9', title='Refactoring , 2nd Edition', creators=['Martin Fowler', 'Kent Beck'], date=datetime.date(2018, 11, 10), type=<ResourceType.BOOK: 1>, description='Improving the design of existing code', language='EN', subjects=['computer programming', 'oop'])


