import itertools

class Candidate:
    def __init__(self, name, gender, experience):
        self.name = name
        self.gender = gender
        self.experience = experience

def generate_combinations(candidates, num_positions):
    combinations = []
    female_candidates = [c for c in candidates if c.gender == "женщина" or c.gender == "both"]
    male_candidates = [c for c in candidates if c.gender == "мужчина" or c.gender == "both"]
    for female_combination in itertools.combinations(female_candidates, num_positions["female"]):
        for male_combination in itertools.combinations(male_candidates, num_positions["male"]):
            remaining_positions = num_positions["total"] - num_positions["female"] - num_positions["male"]
            additional_candidates = itertools.combinations(set(candidates) - set(female_combination) - set(male_combination), remaining_positions)
            for additional_combination in additional_candidates:
                combination = list(female_combination) + list(male_combination) + list(additional_combination)
                combinations.append(combination)
    return combinations

def calculate_fitness(combination):
    return sum(candidate.experience for candidate in combination)

def optimize_solution(candidates, num_positions):
    total_positions = num_positions["total"]
    if total_positions > len(candidates) - 1:
        return [], None
    combinations = generate_combinations(candidates, num_positions)
    if combinations:
        best_combination = max(combinations, key=calculate_fitness)
        return combinations, best_combination
    else:
        return [], None

#Список кандидатов
candidates = [
    Candidate("Кандидат 1", "женщина", 5),
    Candidate("Кандидат 2", "женщина", 2),
    Candidate("Кандидат 3", "женщина", 8),
    Candidate("Кандидат 4", "женщина", 4),
    Candidate("Кандидат 5", "женщина", 5),
    Candidate("Кандидат 6", "женщина", 2),
    Candidate("Кандидат 7", "мужчина", 7),
    Candidate("Кандидат 8", "мужчина", 6),
    Candidate("Кандидат 9", "мужчина", 10),
    Candidate("Кандидат 10", "мужчина", 3),
    Candidate("Кандидат 11", "мужчина", 2),
    Candidate("Кандидат 12", "мужчина", 1),
    Candidate("Кандидат 13", "мужчина", 5),
    Candidate("Кандидат 14", "мужчина", 3)
]

num_positions = {
    "female": 6,
    "male": 6,
    "total": 13
}

combinations, best_combination = optimize_solution(candidates, num_positions)

def print_combinations(combinations):
    i = 1
    for combination in combinations:
        print("Комбинация №", i)
        for candidate in combination:
            print(f"Имя: {candidate.name}, Пол: {candidate.gender}, Стаж: {candidate.experience}")
        i += 1

if combinations:
    print("Все комбинации:")
    print_combinations(combinations)

if best_combination:
    print("\nКомбинация, в которой все кандидаты имеют наивысший стаж:")
    print_combinations([best_combination])