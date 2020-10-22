chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    msg = data.message
    user = data.user
    chat_log = document.querySelector('#chat-log')
//    .value += (user + ': ' + msg + '\n');
    var son = document.createElement("p");
//    son.style.backgroundColor="yellowgreen";
    son.style.padding="3px"
    son.style.borderRadius="3px"
    son.style.clear="both";

    if (user == userName && user != "游客") {
        son.style.float="right";
        son.style.marginRight="5px";
        son.innerHTML= '<span class="msg">' + msg + '</span>' + '<span class="user">' + user + '</span>';
    } else {
        son.style.float="left";
        son.style.marginLeft="5px";
        son.innerHTML='<span class="user">' + user + '</span>' + '<span class="msg">' + msg + '</span>';
    }


    chat_log.appendChild(son);
    son.scrollIntoView();
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    var shiftKey = e.shiftKey || e.metaKey;
    if (shiftKey && e.keyCode === 13) {  // shift+enter, 发送信息
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value.trim();
    if (message != "") {
        chatSocket.send(JSON.stringify({
        'message': message,
        'user': userName
        }));
        messageInputDom.value = '';
    } else {
        alert("不要做无意义的事哦~")
    }

};