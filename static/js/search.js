function searchJob() {
    jobTitle = document.getElementById("title")
    jobCity = document.getElementById("city")
    jobSeniority = document.getElementById("seniority")
}

$(document).ready(function () {
    // toogle description when click on job card
    $('#joblist').on('click', '.jobcard', function () {
        $(this).children(".jobcard_expand").slideToggle('fast');
    });

    // highlight job card when mouse is over
    $('#joblist').on('mouseover', '.jobcard', function () {
        $(this).css('background-color', '#f3f3f3');
    });

    // restore job card color when mouse is out
    $('#joblist').on('mouseout', '.jobcard', function () {
        $(this).css('background-color', 'transparent');
    });

    // highlight job board logo when mouse is over
    $('.clickable').mouseover(function () {
        $(this).css('opacity', '0.6');
    });

    // restore job board logo when mouse is out
    $('.clickable').mouseout(function () {
        $(this).css('opacity', '1.0');
    });

    $('#search-button').click(function(event) {
        event.preventDefault();
        $.ajax({
            url: '/',
            type: 'GET',
            data: jQuery.param({ field1: "hello", field2 : "hello2"}) ,
            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
            success: function (response) {
                alert(response.status);
            },
            error: function () {
                alert("error");
            }
        }); 
      });
});