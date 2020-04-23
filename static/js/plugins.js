/*========== NAVBAR TRANSPARENT TO SOLID ==========*/
$(document).ready(function () { //when document(DOM) loads completely
    checkScroll(); //check if page is scrolled
    $(window).scroll(checkScroll); //get scroll position of window
});

function checkScroll() { //check if page is scrolled
if ($(window).scrollTop() >= 300) { //if window is scrolled 300px or more
    $('.navbar').addClass('solid'); //add class 'solid' to element with class 'navbar'
} else { //if page is not scrolled 300px from top
    $('.navbar').removeClass('solid'); //remove class 'solid' from navbar element
}
}


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

$(document).ready(function () {
    $(document).click(function (event) {
        var clickover = $(event.target);
        var _opened = $("#navbarResponsive").hasClass("show");
        if (_opened === true && !clickover.hasClass("navbar-toggler")) {
            $(".navbar-toggler").click();
        }
    });
});


/*========== MAKE ALL ANIMATION "FADEINUP" ON MOBILE ==========*/
$(document).ready(function () { //when document(DOM) loads completely
    if ($(window).width() < 768) { //if the window is less than 768px
        $("div").attr('data-animation', 'fadeInUp'); //any div with the "data-animation" attribute should have it's value (animation style) changed to "fadeInUp"
        $("div").attr('data-delay', '0s'); //remove data delay
    }
});


/*========== WAYPOINTS ANIMATION DELAY ==========*/
$(function () { // a self calling function
    function onScrollInit(items, trigger) { // a custom made function
       items.each(function () { //for every element in items run function
          var osElement = $(this), //set osElement to the current
             osAnimationClass = osElement.attr('data-animation'), //get value of attribute data-animation type
             osAnimationDelay = osElement.attr('data-delay'); //get value of attribute data-delay time
 
          osElement.css({ //change css of element
             '-webkit-animation-delay': osAnimationDelay, //for safari browsers
             '-moz-animation-delay': osAnimationDelay, //for mozilla browsers
             'animation-delay': osAnimationDelay //normal
          });
 
          var osTrigger = (trigger) ? trigger : osElement; //if trigger is present, set it to osTrigger. Else set osElement to osTrigger
 
          osTrigger.waypoint(function () { //scroll upwards and downwards
             osElement.addClass('animated').addClass(osAnimationClass); //add animated and the data-animation class to the element.
          }, {
                triggerOnce: true, //only once this animation should happen
                offset: '70%' // animation should happen when the element is 70% below from the top of the browser window
             });
       });
    }
 
    // onScrollInitCounterUp();
    onScrollInit($('.os-animation')); //function call with only items
    onScrollInit($('.staggered-animation'), $('.staggered-animation-container')); //function call with items and trigger
});


/*========== PORTFOLIO GALLERY NAVBAR COLLAPSE
(so main nav and portfolio nav don't ipen and close at the same time.) ==========*/
$(document).ready(function () {
    $('#navbarProjects .nav-link').on('click', function () {
        $('.navbar-collapse.collapse').removeClass('show');
    });
});


/*========== PORTFOLIO FILTER (ISOTOPE) INITIALIZATION ==========*/
var $grid = $('.grid').isotope({
    filter: '.nature',
    itemSelector: '.element-item',
    layoutMode: 'fitRows'
});


/*========== ISOTOPE FILTER PROJECT GALLERY ==========*/
// filter functions
var filterFns = {
    // show if number is greater than 50
    numberGreaterThan50: function () {
       var number = $(this).find('.number').text();
       return parseInt(number, 10) > 50;
    },
    // show if name ends with -ium
    ium: function () {
       var name = $(this).find('.name').text();
       return name.match(/ium$/);
    }
 };
 // bind filter button click
 $('.filters-button-group').on('click', 'a.filter', function () {
    var filterValue = $(this).attr('data-filter');
    // use filterFn if matches value
    filterValue = filterFns[filterValue] || filterValue;
    $grid.isotope({ filter: filterValue });
 });
 // change is-checked class on menu
 $('.button-group').each(function (i, buttonGroup) {
    var $buttonGroup = $(buttonGroup);
    $buttonGroup.on('click', 'a.filter', function () {
       $buttonGroup.find('.is-checked').removeClass('is-checked');
       $(this).addClass('is-checked');
    });
 });


/*========== ISOTOPE GALLERY SPACING FIX ==========*/
$(document).ready(function () {
    $container.imagesLoaded(function () {
    $container.isotope({
        itemSelector: ".item",
        isOriginLeft: false,
    });
    $container.isotope();
    });
});


/*========== MAGNIFIC POPUP LIGHTBOX IMAGE GALLERY ==========*/
$(document).ready(function () {
    $('.img-popup').magnificPopup({
       type: 'image',
       gallery: { enabled: true },
       removalDelay: 100, // Delay in milliseconds before popup is removed
       image: {
          titleSrc: 'title'
          // this tells the script which attribute has your image caption
       }
    });
});
 

/*========== MAGNIFIC POPUP LIGHTBOX IMAGE GALLERY ==========*/
 $(document).ready(function () {
    $('.img-popup2').magnificPopup({
       type: 'image',
       gallery: { enabled: true },
       removalDelay: 100, // Delay in milliseconds before popup is removed
       image: {
          titleSrc: 'title'
          // this tells the script which attribute has your image caption
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

$(function () {

  // init the validator
  // validator files are included in the download package
  // otherwise download from http://1000hz.github.io/bootstrap-validator

  $('#contact-form').validator();


  // when the form is submitted
  $('#contact-form').on('submit', function (e) {

      // if the validator does not prevent form submit
      if (!e.isDefaultPrevented()) {
          var url = "contact/contact.php"; //Location of form (apply change if moved).

          // POST values in the background the the script URL
          $.ajax({
              type: "POST",
              url: url,
              data: $(this).serialize(),
              success: function (data)
              {
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