// OOP IN JAVASCRIPT
// Object-Oriented Programming (OOP) is a programming paradigm that uses objects to design software.
const person = {
  name: "John",
  age: 30,
  greet: function() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
};