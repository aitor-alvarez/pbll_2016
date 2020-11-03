// filtering.js
jQuery(function($) {

    var $participant_container = $('#participant_container');

    $participant_container.isotope({
        itemSelector: '.participant',
        layoutMode: 'fitRows',
        // filter: $('#content_filters').attr('data-default'),
    });

    $('#type_filters').on( 'click', '.btn', function() {
        var filterValue = $(this).attr('data-filter');
        $participant_container.isotope({ filter: filterValue });
    });
    $('#alpha_filters').on( 'click', '.btn', function() {
        var floor = $(this).attr('data-floor');
        var ceiling = $(this).attr('data-ceiling');
        
        $participant_container.isotope({ filter: function() {
            var q = $(this).find('.email_addr').text().toLowerCase();
            q = q.charAt(0);
            return q >= floor && q <= ceiling;
        }});
    });


    $(document).ready(function() {

    });

});