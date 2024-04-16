// ობიექტის მაგალითი: ავტომობილი
const car = {
    make: 'Toyota',
    model: 'Corolla',
    year: 2021,
    color: 'red',
    // ფუნქცია, რომელიც აბრუნებს მანქანის სრულ აღწერას
    displayInfo: function() {
        return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}, Color: ${this.color}`;
    }
};

document.getElementById('showCarInfo').addEventListener('click', function() {
    document.getElementById('output').textContent = car.displayInfo();
});

// ობიექტის მაგალითი: წიგნი
const book = {
    title: 'The Catcher in the Rye',
    author: 'J.D. Salinger',
    yearPublished: 1951,
    pages: 214,
    // ფუნქცია წიგნის დეტალების აღწერისთვის
    getDetails: function() {
        return `Title: ${this.title}, Author: ${this.author}, Year Published: ${this.yearPublished}, Pages: ${this.pages}`;
    }
};

document.getElementById('showBookDetails').addEventListener('click', function() {
    document.getElementById('output').textContent = book.getDetails();
});
