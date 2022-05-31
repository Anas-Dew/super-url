window.onload = function () {
    history.replaceState("", "", "/");
};

function click_redirect_to() {
    link = document.getElementById('linkhere').textContent;

    if (link == 'Generate a link !' || link == 'Put a link !!') {

    }
    else {
        alert("Copied the text: " + link);
        window.open(link, "_blank");
    }
};

function click_redirect_to_anas() {
    window.open('https://github.com/Anas-Dew', "_blank");
};