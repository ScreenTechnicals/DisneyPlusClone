// toggle button
const toggler = document.querySelector(".toggle-box");
const circle = document.querySelector(".circle");
toggler.addEventListener("click", function () {
  if (circle.style.left == "50%") {
    circle.style.left = "0";
    circle.style.background = "#f1f1f1";
  } else {
    circle.style.left = "50%";
    circle.style.background = "orange";
  }
});
// Mobile Nav
const mobileNavbar = document.querySelector("#mobile-navbar");
const navRight = document.querySelector(".nav-right");
const bars = document.querySelector(".bars");
bars.addEventListener("click", function () {
  mobileNavbar.style.width = "100%";
});
navRight.addEventListener("click", function () {
  mobileNavbar.style.width = "0";
});

// Mobile Search Box
const mobileSearchBox = document.querySelector(".mobile-search-box");
const mobileSearchIcon = document.querySelector(".mobile-search-icon");
const arrowLeft = document.querySelector(".fa-arrow-left");
mobileSearchIcon.addEventListener("click", function () {
  mobileSearchBox.style.display = "block";
});
arrowLeft.addEventListener("click", function () {
  mobileSearchBox.style.display = "none";
});
