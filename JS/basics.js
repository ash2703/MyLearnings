// alert('fk world ');

// vaiables: var, let, const
// var is global scope avoid using it
// let can reassign values
// const needs to be reassigned with a value

let age = 30 
console.log(age)

age = 40   // TypeError: Assignment to constant variable is this was intiialized with const

console.log(age)

// data types
// String, Numbers, Booleans, null, undefined

const name = 'John Doe'
const newAge = 10
const isBool = true
const x = null  // type will return object but it's a bpgus return
const y = undefined
let z // also undefined
 
console.log(typeof isBool)


// Strings

// string cocnat is same as python using +

console.log(name + newAge)  // can add other dataype too lol

// Template string. NOTE: `` not '' we use backicks here
console.log(`My name is ${name} and my age is ${newAge}`)

console.log(name.length)  //property
console.log(name.split(" "))  //method

// Arrays
const lotOfNumbers = new Array(1,2,3,4,5)
const lotOfNumbersNew = [1,2,3,4,5]
const lotOfNumbersNew2 = [1,2,"3,4,5"]  //any dtype
console.log(lotOfNumbers, lotOfNumbersNew, lotOfNumbersNew2)
// indexing is same as python

console.log(lotOfNumbers[1])

// const arrays can be maniplated as long as new array is not created

lotOfNumbers[1] = "i am a string"
console.log(lotOfNumbers)

lotOfNumbers.push("i'll go at the end")
lotOfNumbers.unshift("i'll go at the start")
console.log(lotOfNumbers)
lotOfNumbers.pop()
console.log(lotOfNumbers)
const doIExist = Array.isArray(lotOfNumbers)
console.log(lotOfNumbers.indexOf("3"))

// Objects

const dict = {
    'firstName': 'Aayush',
    lastName: 'Singh',
    address: {
        city: 'Mumbai',
        pin: '738',
        state: 'los angeles'
    },
    likes: ['icecream', 'fruits', 'momos'],
    isAlive: true
}

// accessing is normal so skipping that but below metod is new
const {firstName, lastName} = dict
console.log(firstName, lastName)
console.log(typeof firstName, typeof lastName) //with or without '' will be string only
// to access object in object
const {address: {city}} = dict  // no idea how this works, it's called destructuring
console.log(city)  

// javascript by default does shallow copy of objects
// structuredClone is a very new method hence may not be supported in all browsers
// json stringify then parse back to create deep copy which is generic
// https://stackoverflow.com/a/23481096
let diffDict = structuredClone(dict)
diffDict.isAlive = false

let diffDictGeneral =  JSON.parse(JSON.stringify(dict))
diffDictGeneral.isAlive = false
// you can create array of objects [{}, {}, {}...]
// Array of objects is similar to JSOn only difference being JSON requires key and value to be in ""double quotes
const notJson = [dict, dict, diffDict, diffDictGeneral] // list of dict objects
// above dict are references, hence changing them later will modify the list dict as well
// dict.isAlive = false
const toJson = JSON.stringify(notJson)

console.log(toJson, typeof toJson)  //Json is basically a string now

//loops
for(var i = 0; i < 10; i++){
    console.log(i)
} 
console.log(i+ 1)
// while(i < 10){
//     console.log(i)
// }

// loop over lists
for(let items of notJson){
    console.log('is alive', items.isAlive)
}

//foreach, map, filter exactly same as python/c++
notJson.forEach(function(item){
    console.log(item.firstName)
})

const notJsonNames = notJson.map(function(item){
    return item.firstName
})

console.log(notJsonNames)

const notJsonAlive = notJson.filter(function(item){
    return item.isAlive === false
})
// === strict equality : data type and value both must match
// == comparison: value must match, data types are changed to match before comparing
console.log(1 == "1") //true
console.log(1 === "1") //false

console.log(notJsonAlive)

//chaining
const aliveNames = notJson.filter(function(item){
    return item.isAlive == true
}).map(function(item){
    return item.firstName
})

console.log(aliveNames)

// || or, && and operator
const check = 10
const value = check > 10 ? '20': '10'  // ternary operator
console.log(value)