// constructor function
// should start with capital letter
function Person(firstName, lastName, dob){
    this.firstName = firstName
    this.lastName = lastName
    this.dob = new Date(dob)  // mm-dd-yyyy

    this.getBirthDay = () => this.dob.getDay()  // here 'this' has the context of scope
    
    // These functions are registered with the object itself
    // we can declare them separatelty as protoypes
    // this.getFullName = function(){
    //     return `${firstName} ${lastName}`
    // }
}

// Prototyping 
// Prototyping using arrow functon does not work : https://stackoverflow.com/a/31755263
// as arrow function don't have their own 'this', 
// they get the 'this' of the context where they are created in
// In this case outside the scope of the class
Person.prototype.getFullName = () => `${this.firstName} hello  ${this.lastName}`  //will not work this will not have reference to names

Person.prototype.getFullName = function(){
    return `${this.firstName} ${this.lastName}`
}

const person1 = new Person('Aayush', 'Singh', '07-03-1999')
const person2 = new Person('Ash', 'King', '03-27-1999')
console.log(person2.getBirthDay())
console.log(person2.getFullName())
console.log(person2)