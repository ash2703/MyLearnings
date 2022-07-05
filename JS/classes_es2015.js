// constructor function
// should start with capital letter
class Person {
    constructor(firstName, lastName, dob) {
        this.firstName = firstName
        this.lastName = lastName
        this.dob = new Date(dob) // mm-dd-yyyy
    }

    // this will not be a prototype since 'this' needs to be retrived from current scope
    // Does not exist outside for arrrow functions
    // TODO: have more clarity on this
    getBirthDay = () => this.dob.getDay() // here 'this' has the context of scope
    // this will be added to prototype
    getFullName() {
        return `${this.firstName} ${this.lastName}`    
    }
}

const person1 = new Person('Aayush', 'Singh', '07-03-1999')
const person2 = new Person('Ash', 'King', '03-27-1999')
console.log(person2.getBirthDay())
console.log(person2.getFullName())
console.log(person2)