const chatBox = document.getElementById("chat-box")
const userInput = document.getElementById("userInput")
const sendBtn = document.getElementById("sendBtn")
const sugg = document.getElementById("sugg")

let botimg = "data:image/jpeg;base64,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"
let userimg = "data:image/jpeg;base64,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"
var socket = io();
socket.on('connect', function() {
  
chatBox.scroll({
  top:chatBox.scrollHeight,
  behavior:"smooth"
})
});

sendBtn.onclick=()=>{
  socket.emit('message', {data: userInput.value});
  message =createMessage("user",userInput.value,userimg)
chatBox.innerHTML+=message

chatBox.scroll({
  top:chatBox.scrollHeight,
  behavior:"smooth"
})
userInput.value = ""
}

const createMessage=(sender,message,url)=>{
  return `
    <div class="message ${sender}">
      <img src="${url}" class="avatar" />
      <div class="text">${message}</div>
  </div>
`}


socket.on('message', function(reply) {
  message = createMessage("bot",reply.data,botimg)
chatBox.innerHTML+=message

chatBox.scroll({
  top:chatBox.scrollHeight,
  behavior:"smooth"
})
});

userInput.oninput=()=>{
  socket.emit("typing",userInput.value)
}

socket.on("suggestion",(data)=>{
  
sugg.innerText = data
})

socket.on("check",(data)=>{
  let values = []
  for (d in data){
    let p = document.createElement('p')
    p.innerHTML = data[d]
    let inp = document.createElement('input')
    inp.setAttribute("id",d)
    chatBox.appendChild(p)
    chatBox.appendChild(inp)
  }
  const btn = document.createElement("button")
  btn.textContent = "Submit"

  btn.addEventListener('click',()=>{
    for(d in data){
      values[d] = document.getElementById(d).value
    }
    console.log(values)
    socket.emit("sendData",values)
    alert("working")
  })

  chatBox.appendChild(btn)

})

function setData(){
  
}
console.log("hello")

