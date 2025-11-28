class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # name
        self.name = name

        # validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.pet_type = pet_type

        # validate owner (if provided)
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")

        self._owner = owner

        # store instance
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # return list of pets whose owner is this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # validate pet
        if not isinstance(pet, Pet):
            raise Exception("pet must be a Pet instance")

        # assign owner
        pet.set_owner(self)

    def get_sorted_pets(self):
        # sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)
