function searchJob() {
    jobTitle = document.getElementById("title")
    jobCity = document.getElementById("city")
    jobSeniority = document.getElementById("seniority")
}

// toogle description when click on job card
$('#job-list').on('click', '.jobcard', function () {
    $(this).children(".jobcard_expand").slideToggle('fast');
});

// highlight job card when mouse is over
$('#job-list').on('mouseover', '.jobcard', function () {
    $(this).css('background-color', '#f3f3f3');
});

// restore job card color when mouse is out
$('#job-list').on('mouseout', '.jobcard', function () {
    $(this).css('background-color', 'transparent');
});
