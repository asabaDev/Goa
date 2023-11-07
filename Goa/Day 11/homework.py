def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("ასეთი სამკუთხედი იარსებებს")
    else:
        print("ასეთი სამკუთხედი ვერ იარსებებს")

def join_names(name1, name2, name3):
    names_list = [name1, name2, name3]
    print(", ".join(names_list))

# დატესტვა
is_triangle(3, 4, 5)  # სამკუთხედის ფუნქციის ტესტი
join_names("გიორგი", "ნინო", "ლევანი")  # სახელების ფუნქციის ტესტი
