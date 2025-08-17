var PROCESS_URL = "/process"; 
var steps = 1; 
let low_est = []; 
let high_est = [];

function calc_valuation(control) {
    var ticker = control.find("input[name='ticker']").val();
    var time_period = control.find("select[name='time_period']").val();
    var amount = control.find("input[name='amount']").val();
    var data_type = control.find("select[name='data_type']").val();

    var minest = control.find("input[name='minest']");
    var maxest = control.find("input[name='maxest']");

    var data = {
        ticker_sym: ticker,
        period: time_period,
        time_amount: amount,
        d_type: data_type,
        step: steps
    };

    $.ajax({
        url: PROCESS_URL,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(result) {
            $(".est").removeClass("est").addClass("next");
            minest.val(result.result.min);
            maxest.val(result.result.max);

            low_est.push(result.result.min);
            high_est.push(result.result.max);
            $(".next").text("Next Step");

            console.log("Low Est: ", low_est);
            console.log("High Est: ", high_est);

            const minlist = $("#minlist");
            const maxlist = $("#maxlist");

            $.each(low_est, function(index, item) {
                minlist.append("<li>" + item + "</li>");
                low_est.pop();
            }); 

            $.each(high_est, function(index, item) {
                maxlist.append("<li>" + item + "</li>");
                high_est.pop();
            });
        },

        error: function(xhr, status, error) {
            console.error("AJAX error:", error);
        }
    });
}

$(document).ready(function() {

    $(document).on("click", ".est", function() {
        var control = $(this).closest(".control");
        $(".tp").attr("disabled", true);
        $(".ta").attr("disabled", true);
        $(".dt").attr("disabled", true);
        $(".tk").attr("disabled", true);
        $(this).text("Processing...");
        calc_valuation(control);
    });

    $(document).on("click", ".next", function() {
        steps = steps + 1;
        console.log("Next Clicked. Steps = ", steps);
        var control = $(this).closest(".control"); 
        $(this).text("Processing...");
        calc_valuation(control);
    });

    $(document).on("click", ".back", function() {
        window.location.href = "/info";
    });

    $(document).on("change", "select[name='time_period']", function() {
        var period = $(this).val();
        var amountInput = $(this).closest(".control").find("input[name='amount']");

        if (period === "ytd") {
            amountInput.val("Year To Date Selected").prop("disabled", true);
        } else if (period === "max") {
            amountInput.val("Max Selected").prop("disabled", true);
        } else {
            amountInput.val("").prop("disabled", false);
        }
    });

    $(document).on("input", "input[name='amount']", function() {
        this.value = this.value.replace(/[^0-9.]/g, '');
    });

});
