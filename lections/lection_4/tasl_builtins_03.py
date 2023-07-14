"""zip(*iterables, strict=False)"""
names = ["Иван", "Николай", "Петр"]
salaries = [125_00, 96_000, 103_000]
awards = [0.1, 0.22, 0.21, 0.12]
for name, salary, award, in zip(names, salaries, awards): 
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')     