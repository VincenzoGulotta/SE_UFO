from dataclasses import dataclass

@dataclass
class Stato:
    id: str
    lat: float
    lng: float

    def __str__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)
