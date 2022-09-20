const host = window.location.host;
const httpProtocol = window.location.protocol;
const rootChatApiBase = "chat-testing/api";

// http://localhost:8000/chat-testing/api/personal/
const allUserRoomEnpoint = `${httpProtocol}//${window.location.host}/${rootChatApiBase}/personal/`;

function getconversationListHtmlText(data) {
    console.log(data);
    const { user, bio, last_message, last_message_time, profile_pic } = data;
    return `<div class="conversation-element">
        <img width="30px" src="${profile_pic}" class="profile-image" />
        <h3 class="room-name">${user}</h3>
        <p class="room-group-info">${bio}</p>
        <p class="room-group-last-message">${last_message}</p>
        <span class="room-last-active">${last_message_time}</span>
    </div>`;
}

async function getPersonalRooms() {
    const response = await fetch(allUserRoomEnpoint);
    if (response.status === 200) {
        const data = await response.json();
        console.log(data);
        return data;
    }
    return [];
}

async function updateContactsList() {
    const parent = document.querySelector(".conversation-elements-container");
    const contacts = await getPersonalRooms();
    const htmlText = contacts
        .map((contact) => {
            return getconversationListHtmlText(contact);
        })
        .join("");
    // console.log(htmlText);
    parent.innerHTML = htmlText;
}

document.addEventListener("DOMContentLoaded", updateContactsList);
