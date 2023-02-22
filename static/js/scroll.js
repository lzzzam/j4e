var jobTitle = "";
var jobCity = "";
var jobSeniority = "";

(function () {

    const newjobEl = document.getElementById("newjobs")
    const loaderEl = document.getElementById("loader")

    const hideLoader = () => {
        loaderEl.classList.remove('show');
    };

    const showLoader = () => {
        loaderEl.classList.add('show');
    };

    // get the quotes from API
    const getJobs = async () => {
        const API_URL = `/nextjobs`;
        const response = await fetch(API_URL);
        // handle 404
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status}`);
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

        if (scrollTop + clientHeight >= scrollHeight - 10) {
            loadJobs();
        }
    }, {
        passive: true
    });

})();
