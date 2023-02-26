var jobTitle = "";
var jobCity = "";
var jobSeniority = "";

(function () {

    const newjobEl = document.getElementById("newjobs")
    const loaderEl = document.getElementById("loader")
    let stopScrolling = 0

    const hideLoader = () => {
        loaderEl.style.display = "none";
    };

    const showLoader = () => {
        loaderEl.style.display = "block";
    };

    // get the quotes from API
    const getJobs = async () => {
        const API_URL = `/nextjobs`;
        const response = await fetch(API_URL);
        // handle 404
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status}`);
        }
        else if (response.status == 204) {
            stopScrolling = 1;
        }
        return await response.text();
    }

    const showJobs = (jobs) => {
        const newEl = document.createElement('div');
        newEl.innerHTML = jobs
        newjobEl.appendChild(newEl);
    };

    // load new jobs
    const loadJobs = async () => {

        showLoader();

        // 0.1 second later
        setTimeout(async () => {
            try {
                // call the API to get new jobs
                const response = await getJobs();
                showJobs(response);
            } catch (error) {
                console.log(error.message);
            }
            finally {
                hideLoader();
            }

        }, 300);
    };

    window.addEventListener('scroll', () => {
        const {
            scrollTop,
            scrollHeight,
            clientHeight
        } = document.documentElement;

        if (stopScrolling == 0) {
            if (scrollTop + clientHeight >= scrollHeight - 10) {
                loadJobs();
            }
        }
    }, {
        passive: true
    });

})();
