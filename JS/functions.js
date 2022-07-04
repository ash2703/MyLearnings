function addNums(first = 5, second = 4){
    return first + second
}

console.log(addNums(3, 5))
console.log(addNums(3)) // default values

// arrow function
// sort of like lambda functions

const addNumsArrow = (first, second = 4) => first + second  // no need to return explicitly
// => called fat arrow

console.log(addNumsArrow(4,99))

const addFive = num => num + 5  // damn, much more slim with single parameter

console.log(addFive(10))

// arrow funcs are great to use with maps, filters or any place where inline funcion needs to be created
const lotOfNumbers = new Array(1,2,3,4,5)
lotOfNumbers.forEach((item) => console.log(item))
