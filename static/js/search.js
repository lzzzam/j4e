$(document).ready(function () {

    let offset = 0;
    let text = "";
    let country = "";

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

    $('#search-button').click(function (event) {
        event.preventDefault();

        offset = 0;
        text = $('#text').val();
        country = $('#country').val();

        $.ajax({
            url: '/search',
            type: 'GET',
            data: jQuery.param({ text: text, country: country, offset: offset.toString() }),
            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
            success: function (response) {
                $("#joblist").empty().append(response)
            }
        });
    });


    const joblist = document.getElementById("joblist")
    const loader = document.getElementById("loader")
    const noresult = document.getElementById("noresult")

    let stopScrolling = 0

    const hideLoader = () => {
        loader.style.display = "none";
    };

    const showLoader = () => {
        loader.style.display = "block";
    };

    const getJobs = async () => {
        offset = offset + 10;
        $.ajax({
            url: '/search',
            type: 'GET',
            data: jQuery.param({ text: text, country: country, offset: offset.toString() }),
            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
            dataType: 'text/html',
            success: function (response) {
                $("#joblist").append(response.responseText);
            },
            statusCode: {
                404: function () {
                    alert("page not found");
                },
                204: function () {
                    stopScrolling = 1;
                },
                200: function (response) {
                    $("#joblist").append(response.responseText);
                }
            }
        });
    }

    // load new jobs
    const loadJobs = async () => {

        showLoader();

        // 0.5 second later
        setTimeout(async () => {
            try {
                getJobs();
            } catch (error) {
                console.log(error.message);
            }
            finally {
                hideLoader();
            }

        }, 500);
    };

    window.addEventListener('scroll', () => {
        if (noresult == null) {
            const {
                scrollHeight,
                clientHeight
            } = document.documentElement;

            let scrollTop = window.scrollY;

            if (stopScrolling == 0) {
                if (scrollTop + clientHeight >= scrollHeight - 5) {
                    loadJobs();
                }
            }
        }
    }, {
        passive: true
    });
});