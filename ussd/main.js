const title = document.getElementById("title");
const list1 = document.getElementById("list1");
const list2 = document.getElementById("list2");
const list3 = document.getElementById("list3");
const list4 = document.getElementById("list4");
const list5 = document.getElementById("list5");
const list6 = document.getElementById("list6");
const list7 = document.getElementById("list7");
const list9 = document.getElementById("list9");
const codeinput = document.getElementById("codeinput");
const Submitbtn = document.getElementById("Submitbtn");
const listbox = document.getElementById("listbox");
const divtext = document.getElementById("divtext");

function Submitcode() {
  if (codeinput.value === "") {
    alert("Invalid Code. Try again");
    // title.textContent='Invalid Code. try again';
    // listbox.style.display="none";
  }
  console.log(codeinput.value);
  if (codeinput.value === "1") {
    title.textContent = "Select Option";
    list1.textContent = "1. Send To Own Number";
    list2.textContent = "2. Send to Another Number";
    list3.style.display = "none";
    list4.style.display = "none";
    list5.style.display = "none";
      list6.style.display = "none";
      list7.style.display = "none";
      list9.style.display = "none";
      codeinput.value = "";
    }
    if(title.value==='Select Option'){
      if (codeinput.value === 1) {
        title.textContent = "Select Account";
        list1.textContent = "1. 233557968414";
        list2.textContent = "2. 233656595956";
        list3.style.display = "block";
        list4.style.display = "block";
        list4.textContent = "4. 233541235478";
        list3.textContent = "3. 233656595956";
        list5.style.display = "none";
        list6.style.display = "none";
        list7.style.display = "none";
        list9.style.display = "none";
      }
    }
  }

