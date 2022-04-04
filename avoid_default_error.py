from dataclasses import dataclass,field

@dataclass
class ClubMember:
    name : str
    guest : list=field(default_factory=list) #guest default is list
    # guest: list=[] #wrong way
    # guests : list[str]=field(default_factory=list) #more precise default,but wrong ,py3.9above
    athele: bool = field(default=False,repr=False) #create a field

@dataclass
class HackerClubMember(ClubMember): #extend the class ClubMember
    all_handles = set()
    handle:str = ''
    # all_handles: ClassVar[set[str]] = set() #since py3.9

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)

