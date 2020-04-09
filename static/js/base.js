

/*========== ADD SOLID CLASS TO NAVBAR WHEN TOGGLED ==========*/
$('.navbar-toggler').click(function () { //when navbar-toggler is clicked
    if ($(window).scrollTop() <= 300) { //if window scrolled 300px or less from top
        $("nav.navbar").toggleClass("solid-toggle"); //add the solid class to navbar
    }
});


/*========== CLOSE MOBILE MENU ON CLICK & SMOOTH SCROLL TO LINK a[href^="#"] ==========*/
$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
    $('.navbar-toggler').addClass('collapsed');
    $('#navbarResponsive').removeClass('show');

    setTimeout(function () {
        $('nav.navbar').removeClass('solid-toggle');
    }, 300);

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 1000);
}); 


/*========== MULTI-LEVEL / DOUBLE CLICK DROP DOWN MENU ==========*/
// $(document).ready(function () {
//     var DELAY = 700, clicks = 0, timer = null;

//     // On click or double click
//     $("nav ul li.dropdown a.dropdown-toggle")
//         .on("click", function (e) {
//             clicks++;
//             if (clicks === 1) {
//                 timer = setTimeout(function () {
//                     clicks = 0;
//                 }, DELAY);
//             } else {
//                 clearTimeout(timer);
//                 window.location.href = $(this).attr('href');
//                 clicks = 0;
//             }
//         })
//         .on("dblclick", function (e) {
//             e.preventDefault();
//         });

/*========== BOUNCING DOWN ARROW ==========*/
$(document).ready(function () {
    $(window).scroll(function () {
        $('.arrow').css('opacity', 1 - $(window).scrollTop() / 250);
    });
});


/*========== LIGHTBOX IMAGE GALLERY ==========*/
$(document).ready(function () {
    lightbox.option({
        'resizeDuration': 600,
        'wrapAround': true,
        'imageFadeDuration': 500
    });
});


/*========== TEAM CAROUSEL ==========*/
$(document).ready(function () { //when document(DOM) loads completely
    $('#team-carousel').owlCarousel({ //owlCarousel settings
        autoplay: true, //set to false to turn off autoplay and only use nav
        autoplayHoverPause: true, //set to false to prevent pausing on hover
        loop: true, //set to false to stop carousel after all slides shown
        autoplayTimeout: 8000, //time between transitions
        smartSpeed: 1600, //transition speed
        dotsSpeed: 1000, //transition speed when using dots/buttons
        responsive: { //set number of items shown per screen width
            0: {
                items: 1 //0px width and up display 1 item
            },
            768: {
                items: 2 //768px width and up display 2 items
            }
        }
    });
});

/*========== TOP SCROLL BUTTON ==========*/
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 500) {
            $('.top-scroll').fadeIn();
        } else {
            $('.top-scroll').fadeOut();
        }
    });
});


/*========== CONTACT FORM INPUT VALIDATION ==========*/
//Original Resource: https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form
$(function () {

    // init the validator
    // validator files are included in the download package
    // otherwise download from http://1000hz.github.io/bootstrap-validator

    $('#contact-form').validator();


    // when the form is submitted
    $('#contact-form').on('submit', function (e) {

        // if the validator does not prevent form submit
        if (!e.isDefaultPrevented()) {
            var url = "contact/contact.php";

            // POST values in the background the the script URL
            $.ajax({
                type: "POST",
                url: url,
                data: $(this).serialize(),
                success: function (data) {
                    // data = JSON object that contact.php returns

                    // we recieve the type of the message: success x danger and apply it to the
                    var messageAlert = 'alert-' + data.type;
                    var messageText = data.message;

                    // let's compose Bootstrap alert box HTML
                    var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + messageText + '</div>';

                    // If we have messageAlert and messageText
                    if (messageAlert && messageText) {
                        // inject the alert to .messages div in our form
                        $('#contact-form').find('.messages').html(alertBox);
                        // empty the form
                        $('#contact-form')[0].reset();
                    }
                }
            });
            return false;
        }
    })
});

/*========== Profile ==========*/
$(document).ready(function () {


    var readURL = function (input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('.avatar').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }


    $(".file-upload").on('change', function () {
        readURL(this);
    });
});

/*========== Data Table ==========*/
$(document).ready(function () {
    $("#table").DataTable({
        scrollY: "50vh",
        scrollCollapse: true,
        paging: false
    });
});
