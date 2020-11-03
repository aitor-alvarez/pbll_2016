// discussions.js
jQuery(function($) {

	var $container = $('#thread_display');

	$container.isotope({
		itemSelector: '.thread_content',
		layoutMode: 'vertical',
		filter: $('#thread_display').attr('data-selected'),
	});

	$('#thread_filters').on( 'click', '.button', function() {
		var filterValue = $(this).attr('data-filter');
		$container.isotope({ filter: filterValue });
	});

	
    $(".post_delete").submit(function( event ) {
        event.preventDefault();
        var container = $("#" + $(this).attr('data-reply-target'));
        $.ajax({
            url : $(this).attr('action'),
            type : "POST",
            data : $(this).serializeArray(),
            dataType : "json",
            // handle a successful response
            success : function(json) {
                container.remove();
            },

            // handle a non-successful response
            error : function(xhr, errmsg, err) {
                // console.log(xhr.status + ": " + errmsg ); // provide a bit more info about the error to the console
            }
        });
    });

    $( ".postform" ).submit(function( event ) {
        event.preventDefault();
        
        /* **** Must call this to populate the form's textarea element */
        tinymce.triggerSave();
        /* **** */

        if ($(this).find("#id_text").val() === "") {
            return;
        }

        var reply_thread = $(this).attr('data-reply_target');
        d = $("#"+event.target.id).serializeArray();
        $.ajax({
            url : $(this).attr('action'),
            type : "POST",
            data : d,
            dataType : "json",

            // handle a successful response


            success : function(json) {
            	var hdr = '<div class="well" style="margin-left: 30px"><dt>' + json.subject + ' <small> ' + json.creator + '</small><small style="float: right"> ' + json.modified + '</small><small style="float: right">&nbsp;<a href="/discussions/post/' + json.id + '/edit/">edit</a>&nbsp;</small></dt>';
				var body = '<dd>' + json.text + '</dd></div>';
				var msg = hdr + ' ' + body;

                // $('#posts').append(msg);
                $("#"+reply_thread).prepend(msg);
                $("#"+event.target.id).trigger("reset");
            },

            // handle a non-successful response
            error : function(xhr, errmsg, err) {
                // console.log(xhr.status + ": " + errmsg ); // provide a bit more info about the error to the console
            }
        });
    });


	$(document).ready(function() {

	});

});