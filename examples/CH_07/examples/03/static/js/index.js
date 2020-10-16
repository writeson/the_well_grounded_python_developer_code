window.addEventListener('load', function (event) {
    let banner = document.querySelector("#header h1");
    window.addEventListener('click', function (event) {
        // is this the click even we're looking for?
        if (event.target.matches('.change-banner-color')) {
            let color = banner_colors[Math.floor(Math.random() * banner_colors.length)];
            banner.style.backgroundColor = color;
        }
    })
});
