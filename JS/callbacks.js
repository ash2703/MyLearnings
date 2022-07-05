const posts = [
    {title: 'Post one', body: 'this is my hot body'},
    {title: 'Post two', body: 'this is my not so cold body'},
]


// setTimeout(()=>{console.log(444)}, 6000)
// console.log(132)

function getPosts(){
    // waits for 1 second then executes whats inside
    // Non blocking operation
    setTimeout(() => {
        console.log("get post started")
        let output = ''
        posts.forEach((item)=> output+= `<li>${item.title}</li>`)
        document.body.innerHTML = output
    }, 1000);
}

function createPost(post, callback){
    // waits 3 seconds and writes to the array
    setTimeout(()=>{
        console.log("createPost started")
        posts.push(post)
        callback()  // makes sure that DOM is filled after we have written to the array
    }, 3000)
}

createPost({title: 'Post three', body: 'this is my second hot body'}, getPosts)
// getPosts() // Not needed if we are using a callback