/*const selectElement= (s) => document.querySelector(s);

selectElement('.open').addEventListener('click', () => {
    selectElement('.nav-list').classList.add('active');
});


selectElement('.close ').addEventListener('click', () => {
    selectElement('.nav-list').classList.remove('active');
});
*/

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }