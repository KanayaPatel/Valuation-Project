$(document).ready(function() {

    $(document).on("click", ".back", function() {
        window.location.href = "/info";
    })

    $(document).on("click", ".go-next", function() {
        window.location.href = "/valuation";
    })
})