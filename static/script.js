const currentYear = document.getElementById("current-year");

// update copyright date to current year
const year = new Date().getFullYear();
currentYear.innerHTML = year.toString();