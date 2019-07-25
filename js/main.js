


let adding = document.querySelectorAll(".add");
let subtracting = document.querySelectorAll(".subtract");
let countdown = document.querySelectorAll(".giveMeOne");

adding.forEach(function(elm, i){
  elm.addEventListener("click", function(){
    countdown[i].innerHTML ++
  });
});


subtracting.forEach(function(elm, i){
  elm.addEventListener("click", function(){
    countdown[i].innerHTML --
  });
});

// let hoverDivs = document.querySelectorAll(".column");
// let colincol = document.querySelectorAll(".columnInCol");
//
// hoverDivs.forEach(function(elm, i){
//   elm.addEventListener("mouseover", function(){
//     colincol[i].classList.remove("makeMeVisible")
//   });
//   elm.addEventListener("mouseout", function(){
//     colincol[i].classList.add("makeMeVisible")
//   });
// });
