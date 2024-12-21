import random

# Grid boyutu tanımlanması ve simülasyon için sabitlerin tanımlanması
GRID_SIZE = 500

# Hayvanlar için hareket aralıklarının tanımlanması
MOVEMENT_RANGES = {
    'Sheep': 2,
    'Cow': 2,
    'Rooster': 1,
    'Chicken': 1,
    'Wolf': 3,
    'Lion': 4,
    'Hunter': 1
}

# Tüm varlıklar için temel class
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, range_limit):
        self.x = max(0, min(GRID_SIZE, self.x + random.randint(-range_limit, range_limit)))
        self.y = max(0, min(GRID_SIZE, self.y + random.randint(-range_limit, range_limit)))

    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

# Hayvan class
class Animal(Entity):
    def __init__(self, x, y, gender):
        super().__init__(x, y)
        self.gender = gender

class Hunter(Entity):
    pass

# Varlıkların başlatılması
def initialize_entities():
    animals = []

    # Koyunların eklenmesi
    for _ in range(15):
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'M'))
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'F'))

    # İneklerin eklenmesi
    for _ in range(5):
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'M'))
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'F'))

    # Tavuk ve horozların eklenmesi
    for _ in range(10):
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), None))  # Chicken
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), None))  # Rooster

    # Kurtların eklenmesi
    for _ in range(5):
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'M'))
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'F'))

    # Aslanların eklenmesi
    for _ in range(4):
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'M'))
        animals.append(Animal(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), 'F'))

    # Avcının eklenmesi
    hunter = Hunter(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE))

    return animals, hunter

# Simülasyon mantığı
def simulate():
    animals, hunter = initialize_entities()

    for turn in range(1000):
        # Hayvanların hareket ettirilmesi
        for animal in animals:
            species = type(animal).__name__
            range_limit = MOVEMENT_RANGES.get(species, 1)
            animal.move(range_limit)

        # Avcının hareket ettirilmesi
        hunter.move(MOVEMENT_RANGES['Hunter'])

        # Etkileşimlerin yönetimi (avlanma ve üreme)
        handle_interactions(animals, hunter)

    # Sonuçların çıktısının alınması
    print(f"Simulation complete after 1000 turns.")
    count_species(animals)

# Hayvanlar ile avcı arasındaki etkileşimlerin yönetimi
def handle_interactions(animals, hunter):
    hunted = []

    for predator in animals:
        if isinstance(predator, Animal):
            for prey in animals:
                if predator != prey and predator.distance_to(prey) <= 4:  # Gerçek mantıkla değiştirin
                    hunted.append(prey)

    for prey in hunted:
        animals.remove(prey)

# Her bir türün sayısını sayma ve yazdırma
def count_species(animals):
    species_count = {}

    for animal in animals:
        species = type(animal).__name__
        species_count[species] = species_count.get(species, 0) + 1

    for species, count in species_count.items():
        print(f"{species}: {count}")

if __name__ == "__main__":
    simulate()
