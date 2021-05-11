/**
* @package Helix3 Framework
* @author JoomShaper http://www.joomshaper.com
* @copyright Copyright (c) 2010 - 2015 JoomShaper
* @license http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 or later
*/
jQuery(function($) {

    var $body = $('body'),
    $wrapper = $('.body-innerwrapper'),
    $toggler = $('#offcanvas-toggler'),
    $close = $('.close-offcanvas'),
    $offCanvas = $('.offcanvas-menu');

    $toggler.on('click', function(event){
        event.preventDefault();
        stopBubble (event);
        setTimeout(offCanvasShow, 50);
    });

    $close.on('click', function(event){
        event.preventDefault();
        offCanvasClose();
    });

    var offCanvasShow = function(){
        $body.addClass('offcanvas');
        $wrapper.on('click',offCanvasClose);
        $close.on('click',offCanvasClose);
        $offCanvas.on('click',stopBubble);

    };

    var offCanvasClose = function(){
        $body.removeClass('offcanvas');
        $wrapper.off('click',offCanvasClose);
        $close.off('click',offCanvasClose);
        $offCanvas.off('click',stopBubble);
    };

    var stopBubble = function (e) {
        e.stopPropagation();
        return true;
    };

    //Mega Menu
    $('.sp-megamenu-wrapper').parent().parent().css('position','static').parent().css('position', 'relative');
    $('.sp-menu-full').each(function(){
        $(this).parent().addClass('menu-justify');
    });

    //Sticky Menu
    $(document).ready(function(){
        $("body.sticky-header").find('#sp-header').sticky({topSpacing:0})
    });

    //tab_product detail
    $('.virtuemart-tabs .tabs li a').click(function(){
        $('.virtuemart-tabs .panel.active').removeClass('active');
        $('.virtuemart-tabs .tabs li.active').removeClass('active');
        $(this).parent().addClass('active');
        $($(this).attr('href')).addClass('active');
        return false;
    });

    //Tooltip
    $('[data-toggle="tooltip"]').tooltip();
    
    $(document).on('click', '.sp-rating .star', function(event) {
        event.preventDefault();

        var data = {
            'action':'voting',
            'user_rating' : $(this).data('number'),
            'id' : $(this).closest('.post_rating').attr('id')
        };

        var request = {
                'option' : 'com_ajax',
                'plugin' : 'helix3',
                'data'   : data,
                'format' : 'json'
            };

        $.ajax({
            type   : 'POST',
            data   : request,
            beforeSend: function(){
                $('.post_rating .ajax-loader').show();
            },
            success: function (response) {
                var data = $.parseJSON(response.data);

                $('.post_rating .ajax-loader').hide();

                if (data.status == 'invalid') {
                    $('.post_rating .voting-result').text('You have already rated this entry!').fadeIn('fast');
                }else if(data.status == 'false'){
                    $('.post_rating .voting-result').text('Somethings wrong here, try again!').fadeIn('fast');
                }else if(data.status == 'true'){
                    var rate = data.action;
                    $('.voting-symbol').find('.star').each(function(i) {
                        if (i < rate) {
                           $( ".star" ).eq( -(i+1) ).addClass('active');
                        }
                    });

                    $('.post_rating .voting-result').text('Thank You!').fadeIn('fast');
                }

            },
            error: function(){
                $('.post_rating .ajax-loader').hide();
                $('.post_rating .voting-result').text('Failed to rate, try again!').fadeIn('fast');
            }
        });
    });

    //counter
    $('.counters-box .counter-up').counterUp({
        delay: 100,
        time: 1000
    });

    $(".various1").fancybox({
        'titlePosition'		: 'inside',
        'transitionIn'		: 'none',
        'transitionOut'		: 'none'
    });

    $('.owl-carousel').owlCarousel({

        margin:10,
        nav:true,

        responsive:{
            0:{
                items:2
            },
            767:{
                items:3
            },
            1000:{
                items:4
            }
        },
        navContainer: '.controls_navi',
        navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],

    });

    // Parallax for box banner title
    if($(window).width()<767) {
        $('.sp_ob_opening_slider').css('background-image', 'url(' + $('.sp_ob_opening_slider .bg_img').find('img').css('opacity','0').attr('src') + ')');
    }

    //view shop
    $('.browse-view .display_view a.grid').click(function(){
        if(!$(this).hasClass('active')) {
            $('.browse-view').removeClass('list_products').addClass('grid_products');
            $('.browse-view .display_view a').removeClass('active');
            $(this).addClass('active');
        }
        return false;
    });
    $('.browse-view .display_view a.list').click(function(){
        if(!$(this).hasClass('active')) {
            $('.browse-view').removeClass('grid_products').addClass('list_products');
            $('.browse-view .display_view a').removeClass('active');
            $(this).addClass('active');
        }
        return false;
    });

    //Back To top
    var back_to_top = function () {
        jQuery(window).scroll(function () {
            if (jQuery(this).scrollTop() > 100) {
                jQuery('#back-to-top').css({bottom: "15px"});
            } else {
                jQuery('#back-to-top').css({bottom: "-50px"});
            }
        });
        jQuery('#back-to-top').click(function () {
            jQuery('html, body').animate({scrollTop: '0px'}, 800);
            return false;
        });
    }
    back_to_top();

    var sticky_sidebar = function() {
        $( '#sp-right .sp-column' ).wrap( '<div class="wrap_sidebar"></div>' ); // wrap it up
        $( '<div class="sticky-stop"></div>' ).insertAfter( '#sp-main-body' );// stop it!
        var sidebarheight, mainheight;
        var sidebarWidth = $( '#sp-right').width();
        $( '#sp-right .wrap_sidebar').width(sidebarWidth);
        var cushion = 100; // cushion for spapping to the bottom
        function measureheight() {
            sidebarheight = $('#sp-right').outerHeight() + cushion;
            mainheight = $('#sp-component').outerHeight();
            if (mainheight - sidebarheight > 0) {
                $('#sp-main-body').waypoint(function(direction) {
                    $(this).toggleClass('sticky', direction === 'down');
                }, {
                    offset: 120
                });
                $('.sticky-stop').waypoint(function(direction) {
                    $('#sp-main-body').toggleClass('at-bottom', direction === 'down');
                }, {
                    offset: function() {
                        return sidebarheight;
                    }
                })
            } else {
                //$().waypoints('destroy');
            }
        };
        measureheight();
        $(window).resize(measureheight);
    }
    $(document).ready(function() {
        if($(window).width()>=768)
            sticky_sidebar();
    });


    $('#searchModal').on('shown.bs.modal', function () {
        $('#searchModal input[name="keyword"]').focus();
    });

    $('.ob_lightbox_shop .addtocart-area .addtocart-button').click(function(){
        $.fancybox.close();
    });

});