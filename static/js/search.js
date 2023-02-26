import Typed from './typed.js';

// auto type city in the header
const newCity = new Typed('#header-city', {
    strings: [
        'Munich', 'Vienna', 'Paris',
        'Warsaw', 'Berlin', 'Rome',
        'Madrid', 'Zagreb', 'Athens',
        'Lisbon', 'Milan'
    ],
    // typing-in speed. default value is one
    typeSpeed: 1,
    // typing-out speed. default value is one
    backSpeed: 1,
    // occur once or forever. default value is false
    loop: true,
    // color of insertion point. default value is black
    IPColor: "white",
});
// Initialize Typing Effect
newCity.start();

function searchJob() {
    jobTitle = document.getElementById("title")
    jobCity = document.getElementById("city")
    jobSeniority = document.getElementById("seniority")
}
$("#search-text").click(function () {
    $(this).css('border-width', '3px');
});

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

// highlight job board logo when mouse is over
$('.clickable').mouseover(function () {
    $(this).css('opacity', '0.6');
});

// restore job board logo when mouse is out
$('.clickable').mouseout(function () {
    $(this).css('opacity', '1.0');
});