


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
