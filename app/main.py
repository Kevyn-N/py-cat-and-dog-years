def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if (
        not isinstance(cat_age, int)
        or isinstance(cat_age, bool)
        or not isinstance(dog_age, int)
        or isinstance(dog_age, bool)
    ):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    cat_human_years = 0
    dog_human_years = 0

    if cat_age >= 15:
        cat_human_years += 1
    if cat_age >= 24:
        cat_human_years += 1
    if cat_age > 24:
        cat_human_years += (cat_age - 24) // 4

    if dog_age >= 15:
        dog_human_years += 1
    if dog_age >= 24:
        dog_human_years += 1
    if dog_age > 24:
        dog_human_years += (dog_age - 24) // 5

    return [cat_human_years, dog_human_years]
