function checkInput() {
    let elements = document.getElementsByClassName("input_cred");
    let button = document.getElementById("submit");
    if (elements[0].value.length > 0 && elements[1].value.length > 0) {
        button.removeAttribute('disabled');
    }
    else {
        button.setAttribute('disabled', '');
    };
};

function displayError(error, className) {
    let divChild = document.createElement("div");
    let target = document.getElementById("main");
    divChild.innerHTML = error;
    divChild.className = className;
    divChild.style.width = parseInt(getComputedStyle(target).width) - 25 + "px";
    target.appendChild(divChild);
}
if (error !== 'None') {
    displayError(error, 'error');
};
if (success !== 'None') {
    displayError(success, 'success');
};

let form = document.getElementById("form");
form.addEventListener('submit', function(event) {
    let targetStyle = getComputedStyle(form);
    let loading = document.getElementById("loading");
    let loading_outer = document.getElementById("loading_outer");
    loading_outer.style.width = parseInt(targetStyle.width) + "px";
    loading_outer.style.height = parseInt(targetStyle.height) + "px";
    if (parseInt(targetStyle.width) < parseInt(targetStyle.height)) {
        loading.style.width = parseInt(targetStyle.width) / 3 + "px";
        loading.style.height = parseInt(targetStyle.width) / 3 + "px";
    }
    else {
        loading.style.width = parseInt(targetStyle.height) / 3 + "px";
        loading.style.height = parseInt(targetStyle.height) / 3 + "px";
    };
    loading.style.display = 'block';
    if (success !== 'None') {
        document.getElementsByClassName('success')[0].style.display = 'none';
    };
    if (error !== 'None') {
        document.getElementsByClassName('error')[0].style.display = 'none';
    };
    form.style.display = 'none';
});

function reveal_pswd() {
    let target = document.getElementById('pswd_input')
    let img = document.getElementById('pswd_reveal_img')
    let img_crossed = document.getElementById('pswd_reveal_img_crossed')
    if (target.type == 'password') {
        target.type = 'text';
        img.setAttribute('style', 'display: none;')
        img_crossed.setAttribute('style', '')
    } else {
        target.type = 'password';
        img.setAttribute('style', '')
        img_crossed.setAttribute('style', 'display: none;')
    }
}
document.getElementById('reveal_pswd').addEventListener('click', reveal_pswd);