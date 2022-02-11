'use strict';

function openLogin() {
    document.getElementById("popupForm").style.display = "block";
}
function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}

window.onclick = function (event) {
    let modal = document.getElementById('loginPopup');
    if (event.target == modal) {
        closeForm();
    }
}