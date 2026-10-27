def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_human_years = 0
    dog_human_years = 0

    # Conversão para o Gato
    if cat_age >= 15:
        cat_human_years += 1
    if cat_age >= 24:
        cat_human_years += 1
    if cat_age > 24:
        cat_human_years += (cat_age - 24) // 4

    # Conversão para o Cão
    if dog_age >= 15:
        dog_human_years += 1
    if dog_age >= 24:
        dog_human_years += 1
    if dog_age > 24:
        dog_human_years += (dog_age - 24) // 5

    return [cat_human_years, dog_human_years]
