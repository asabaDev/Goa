// 1. ორი int ტიპის ცვლადი და მათი მათემატიკური ოპერაციები
let num1 = 15;
let num2 = 3;
console.log("Multiplication: " + (num1 * num2));
console.log("Division: " + (num1 / num2));
console.log("Addition: " + (num1 + num2));
console.log("Subtraction: " + (num1 - num2));

// 2. წიგნების ცვლადები და ფასდაკლებები
let books = [
    { name: "Book1", price: 20 },
    { name: "Book2", price: 30 },
    { name: "Book3", price: 40 },
    { name: "Book4", price: 50 },
    { name: "Book5", price: 60 },
    { name: "Book6", price: 70 },
    { name: "Book7", price: 80 },
    { name: "Book8", price: 90 },
    { name: "Book9", price: 100 },
    { name: "Book10", price: 110 }
];

books.forEach((book, index) => {
    if (index < 5) {
        book.price *= 0.9; // 10% discount
    } else {
        book.price *= 0.8; // 20% discount
    }
    console.log(book.name + " new price: " + book.price);
});

// 3. ოჯახის წევრების ასაკი და დათვლა 25 წელიწადში
let familyAges = { mother: 45, father: 50, child: 20 };
Object.keys(familyAges).forEach(key => {
    let ageIn25Years = familyAges[key] + 25;
    console.log(key + " will be " + ageIn25Years + " years old in 25 years.");
});

// 4. მომხმარებელის ინფორმაცია
let user = {
    firstName: "Giorgi",
    lastName: "Smith",
    age: 28,
    residence: "Tbilisi",
    profession: "Developer",
    hobby: "Reading",
    additionalInfo: "Likes to travel"
};

let userInfo = `User ${user.firstName} ${user.lastName} is ${user.age} years old, lives in ${user.residence}, works as a ${user.profession}, enjoys ${user.hobby}, and ${user.additionalInfo}.`;
console.log(userInfo);

// 5. შემოსული რიცხვის ლუწობა თუ კენტობა
let inputNumber = 17; // გამოცვალეთ რიცხვით რაც მომხმარებლისაგა
