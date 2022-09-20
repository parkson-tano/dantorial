const host = window.location.host;
const httpProtocol = window.location.protocol;
const rootChatApiBase = `${httpProtocol}//${window.location.host}/chat-testing/api`

const roomId = document.querySelector("#chat-id").value
const allUserRoomEnpoint = `${rootChatApiBase}/personal/`;
const contactMessagesEndPoint = `${rootChatApiBase}/messages/${roomId}/`

function getconversationListHtmlText(data) {
    const { user, bio, last_message, last_message_time, profile_pic, chat_url } = data;
    console.log(data)
    return `<div class="conversation-element" role="button" xhref=${chat_url}>
        <img width="30px" src="${profile_pic}" class="profile-image" />
        <h3 class="room-name">${user}</h3>
        <p class="room-group-info">${bio}</p>
        <p class="room-group-last-message">${last_message}</p>
        <span class="room-last-active">${last_message_time}</span>
    </div>`;
}

function getMessageHtmlText(data){
    const {username, content, userprofile, isowner, created} = data;
    return `
        <div class="${isowner ? "owner": ""} message">
            <img src="${userprofile}" alt="" class="profile-image" />
            <div class="message-body">
                <h4>${username}</h4>
                <span>
                ${content}
                </span>
            </div>
            <p class="message-delivery-time">12:30pm</p>
        </div>
    `;
}

async function getData(endpoint) {
    const response = await fetch(endpoint);
    if (response.status === 200) {
        const data = await response.json();
        return data;
    }
    return [];
}

async function updateContactsList() {
    const parent = document.querySelector(".conversation-elements-container");
    const contacts = await getData(allUserRoomEnpoint);
    const htmlText = contacts
        .map((contact) => {
            return getconversationListHtmlText(contact);
        })
        .join("");
    parent.innerHTML = htmlText;
}

async function updateMessagesList(){
    const parent = document.querySelector(".chat-main > div");
    const messages = await getData(contactMessagesEndPoint);
    const htmlText  = messages.messages.map(msg => {
        return getMessageHtmlText(msg)
    }).join("");
    parent.innerHTML = htmlText
}

document.addEventListener("DOMContentLoaded", async () => {
    await updateMessagesList();
    await updateContactsList();
});
