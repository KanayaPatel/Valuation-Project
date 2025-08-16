$(document).ready(function() {

  // Existing click handlers
  $(document).on("click", ".start-button", function() {
    window.location.href = "/getting-started";
  });

  $(document).on("click", ".back", function() {
    window.location.href = "/"
  })

})
