// Fix menu bug
function openResponsiveMenu() {
  var x = document.getElementById("navBar");
  if (x.className === "navBar") {
    x.className += " responsive";
  } else {
    x.className = "navBar";
  }
};

// Set home menu active link
function setActive(linkId) {
  // Set interval
  var activeInterval = setInterval(() => {
    // Check if element exists
    if (document.getElementById(linkId)) {
      // Add "active" class
      document.getElementById(linkId).classList.add("active");
      // Stop from running
      clearInterval(activeInterval);
    }
  }, 100);
}

function setFooter() {
  // Set interval
  var footerInterval = setInterval(() => {
    // Check if element exists
    if (document.getElementById("footerText")) {
      // Get current year
      var year = new Date().getFullYear();
      // Set footer text
      document.getElementById("footerText").innerHTML = "&copy; Copyright  | Bluebotlaboratories | 2016 - " + year;
      // Stop from running
      clearInterval(footerInterval);
    }
  }, 100);
}