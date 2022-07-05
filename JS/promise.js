const posts = [
    {title: 'Post one', body: 'this is my hot body'},
    {title: 'Post two', body: 'this is my not so cold body'},
]

function getPosts(){
    setTimeout(() => {
        console.log("get post started")
        let output = ''
        posts.forEach((item)=> output+= `<li>${item.title}</li>`)
        document.body.innerHTML = output
    }, 1000);
}


function createPost(post, callback){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log("createPost started")
            posts.push(post)

            error = false // dummy error check
            if(!error){
                // go ahead and resolve the promise if no error
                resolve('hale looya')
            } else{
                // else throw error
                reject("ERROR: Some unwanted error occured")
            }
            // callback()  // No need of a callback when using promise
        }, 5000)
    })
    
}

/* Comment this to run aync await

const promise4 = createPost(
    {title: 'Post three', body: 'this is my second hot body'}
    ).then(getPosts) // then is used to attach a callback if promise is resolved
    .catch(err => console.log(err))  // catch the error if promise is rejected and handle it via another callback

console.log(promise4)  // state will be pending
setTimeout(()=> console.log(promise4), 7000)  // state will be fulfilled 

// Handling multiple promises

const promise1 = Promise.resolve('works like a charm')  // change to reject for understanding .all behaviour
const promise2 = 'hello world'
const promise3 = new Promise((resolve, reject)=>{
    setTimeout(resolve, 4000, 'i also can work')
})

// promise.all returns a single promise which resolves only if all promises resolve
// it has a fail-fast mechanism, if even 1 promise rejects all will return reject immediately
Promise.all([promise1, promise2, promise3])
.then(values => console.log(values))
.catch(err => console.log("haha", err))

*/

// Comment this to run above code

// Async / Await
// basically an elegant way to deal with .then
let step = 0

async function init(){
    console.log("within init start executed at step: ", step)
    step++

    // await is blocking only within the async function
    // calls outside the function will not be blocked

    await createPost({title: 'Post three', body: 'this is my second hot body'})
    console.log("within init end executed at step: ", step) // blocked until above function returns
    step++
    getPosts()
}

console.log("before init executed at step: ", step)  // will run first
step++
init()
console.log("after init executed at step: ", step) // will run without waiting for init to finish
step++
