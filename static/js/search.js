$(document).ready(function () {

    let offset = 0;
    let text = "";
    let country = "";
    let didScroll = false;
    let enableScroll = true;

    // toogle description when click on job card
    $('#joblist').on('click', '.jobcard', function () {
        $(this).children(".jobcard_expand").slideToggle('fast');
    });

    // query database with new text/country
    $('#search-button').click(function (event) {
        event.preventDefault();

        offset = 0;
        text = $('#text').val();
        country = $('#country').val();
        enableScroll = true;

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

    // make GET request to receive new job cards as HTML
    const getNewJobs = async () => {
        offset = offset + 20;
        $.ajax({
            url: '/search',
            type: 'GET',
            data: jQuery.param({ text: text, country: country, offset: offset.toString() }),
            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
            dataType: 'text/html',
            statusCode: {
                404: function () {
                    alert("page not found");
                },
                204: function () {
                    // no more job available --> stop request new jobs
                    enableScroll = false;
                },
                200: function (response) {
                    $("#joblist").append(response.responseText);
                }
            }
        });
    }

    // show loading symbol for 0.5 secs and request new job cards
    const loadJobs = async () => {
        $('#loader').show();
        setTimeout(async () => {
            try {
                getNewJobs();
            } catch (error) {
                console.log(error.message);
            }
            finally {
                $('#loader').hide();
            }
        }, 500);
    };

    $(window).scroll(function () {
        didScroll = true;
    });

    // set a timer to check if a "scroll" event happened
    setInterval(function () {
        if (didScroll) {
            didScroll = false;

            // request new job only when special 
            // <div id="noresult"...> is NOT present
            if (!$('#noresult').length) {
                const {
                    scrollHeight,
                    clientHeight
                } = document.documentElement;

                let scrollTop = window.scrollY;

                if (enableScroll == true) {
                    if (scrollTop + clientHeight >= scrollHeight - 10) {
                        loadJobs();
                    }
                }
            }
        }
    }, 250);
});