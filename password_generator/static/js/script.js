var slider = document.getElementById("myRange");
var output = document.getElementById("length_num");
const contentSaved = document.getElementById('copy');
output.innerHTML = slider.value;

slider.oninput = function () {
    output.innerHTML = this.value;
}

$('.js-copy').on('click', function () {
    copyToClipboard( $(this).text());
    ui_copyDone();
})

$('.custom-btn').on('click', function () {
    contentSaved.classList.remove('copied')
    contentSaved.classList.add('visually-hidden')
})

function copyToClipboard(str) {
    let area = document.createElement('textarea');

    document.body.appendChild(area);
    area.value = str;
    area.select();
    document.execCommand('copy');
    document.body.removeChild(area);
}

function ui_copyDone() {
    contentSaved.classList.remove('visually-hidden')
    contentSaved.classList.add('copied')
}