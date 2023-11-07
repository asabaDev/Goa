family = ["tamuna", "saba", "mate"]
ages = [45, 18, 20]  # მაგალითად, აქ მითითებულია თითოეულის ასაკი

# პირველი წინადადება: ამჟამინდელი ასაკები
current_age_sentence = "My mom's name is {}, she is {} years old. My brother's name is {}, he is {} years old. My name is {}, I am {} years old.".format(family[0], ages[0], family[1], ages[1], family[2], ages[2])
print(current_age_sentence)

# მეორე წინადადება: 10 წლის შემდეგ
future_ages = [age + 10 for age in ages]  # ყველას ასაკი ვზრდი 10-ით
future_age_sentence = "In 10 years, my mom {} will be {} years old, my brother {} will be {} years old, and I {} will be {} years old.".format(family[0], future_ages[0], family[1], future_ages[1], family[2], future_ages[2])
print(future_age_sentence)
