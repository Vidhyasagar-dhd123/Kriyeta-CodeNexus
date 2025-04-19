function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (message === "") return;
  
    appendMessage("user", message);
    input.value = "";
  
    let response = "I'm here to help!";
    const lower = message.toLowerCase();
  
    if (lower.includes("hello")) {
      response = "Hello! How can I help you today?";
    } else if (lower.includes("thank")) {
      response = "You're welcome! Is there anything else I can help you with?";
    } else if (lower.includes("bye")) {
      response = "Goodbye! Have a great day!";
    }
  
    setTimeout(() => {
      appendMessage("bot", response);
    }, 500);
  }
  
  function appendMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}`;
  
    const avatar = document.createElement("img");
    avatar.className = "avatar";
    avatar.src =
      sender === "bot"
        ? "https://cdn-icons-png.flaticon.com/512/4712/4712107.png"
        : "https://cdn-icons-png.flaticon.com/512/219/219969.png";
  
    const msgText = document.createElement("div");
    msgText.className = "text";
    msgText.innerText = text;
  
    msgDiv.appendChild(avatar);
    msgDiv.appendChild(msgText);
  
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  
  document.getElementById("sendBtn").addEventListener("click", sendMessage);
  document.getElementById("userInput").addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
  });
  
  