$(document).ready(function() {
    let banner = $("div.jumbotron");

    // create handler for button click event
    $("#change-banner-color").click(function(event) {
        let color = banner_colors[Math.floor(Math.random() * banner_colors.length)];
        banner.css("background-color", color);
    })
});
