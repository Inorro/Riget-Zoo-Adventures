console.log("JS Connected");

const btns = document.querySelectorAll("[data-target]");
const overlay = document.querySelector("#overlay");
const body = document.querySelector("*");


btns.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelector(btn.dataset.target).classList.add("active");
        overlay.classList.add("active");
    })
})

window.onclick = (e) => {
    if (e.target == overlay) {
        const modals = document.querySelectorAll(".modal");
        modals.forEach((modal) => modal.classList.remove("active"));
        overlay.classList.remove("active");
        body.classList.remove("active");
    }
}

function valthis() {
    var checkBoxes = document.getElementsByName('tickets[]');
    var isChecked = false;
    for (var i = 0; i < checkBoxes.length; i++) {
        if (checkBoxes[i].checked) {
            isChecked = true;
        };
    };
    if (isChecked) {
        return false;
    } else {
        alert('Please, select at least one item');
        event.preventDefault();
    }
}

function openTab(evt, tabname) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcont");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabname).style.display = "block";
    evt.currentTarget.className += " active";
}

elements = document.getElementsByName("tickets[]");
console.log(elements.length)
function checking(){
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].checked){
            select = "num" + String(i+1)
            selectmenu = document.getElementById(select)
            selectmenu.selectedIndex = 1
        }
        if (elements[i].checked === false){
            select = "num" + String(i+1)
            selectmenu = document.getElementById(select)
            selectmenu.selectedIndex = 0
        }
    }
}

var acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      panel.style.padding = "0px";
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
      panel.style.padding = "10px";
    } 
  });
}

if (localStorage.fontSize)
{
    star = document.getElementsByTagName('html')[0];
    star.style.fontSize = localStorage.fontSize;
}

if (localStorage.filter)
{
    star = document.getElementsByTagName('body')[0];
    star.style.filter = localStorage.filter;
    star.style.backdropFilter = localStorage.backdropFilter;
}

function largefont(){
    star = document.getElementsByTagName('html')[0];
    star.style.fontSize = "25px";
    localStorage.fontSize = '25px';
}

function medfont(){
    star = document.getElementsByTagName('html')[0];
    star.style.fontSize = "16px";
    localStorage.fontSize = '16px';
}

function smallfont(){
    star = document.getElementsByTagName('html')[0];
    star.style.fontSize = "12px";
    localStorage.fontSize = '12px';
}

function original(){
    star = document.getElementsByTagName('body')[0];
    bg = document.getElementById("bg");
    star.style.filter = "none";
    bg.style.backdropFilter = "none";
    localStorage.filter = 'none';
    localStorage.backdropFilter = 'none';
}

function greyscale(){
    star = document.getElementsByTagName('body')[0];
    bg = document.getElementById("bg");
    star.style.filter = "grayscale(100%)";
    bg.style.backdropFilter = "grayscale(100%)";
    localStorage.filter = 'grayscale(100%)';
    localStorage.backdropFilter = 'grayscale(100%)';
}

function blue(){
    star = document.getElementsByTagName('body')[0];
    bg = document.getElementById("bg");
    star.style.filter = "hue-rotate(90deg)";
    bg.style.backdropFilter = "hue-rotate(90deg)";
    localStorage.filter = 'hue-rotate(90deg)';
    localStorage.backdropFilter = 'hue-rotate(90deg)';
}
