

$(document).ready(function() {

    // Get the modal
    var $popup = $('#popup');

    // Open the modal
    var button = $('#button-open-modal');
    button.on('click', function(event) {
        modal.css('display', 'block');
    })

    // Close the modal
    var close_button = $('.close');
    close_button.on('click', function(event) {
        modal.css('display', 'none');
    })

    // when the user clicks anywhere in modal , close it
    $(window).on('click', function(event) {
        if (event.target.id == modal.attr('id')) {
            modal.css('display', 'none');
        }
    })
    //$('body').on('click', '.item a', function(e) {
        //e.preventDefault();
        //var $link = $(this);
        //var popup_url = $link.data('popup-url');
        //var popup_title = $link.data('popup-title');

        //if (!popup_url) {
            //return true;
        //}
        //$('.modal-title', $popup).html(popup_title);
        //$('.modal-body', $popup).load(popup_url, function() {
            //$popup.on('shown.bs.modal', function () {
                //// do somethings when dialog is shown
                ////
            //}).modal("show");
        //});

        //$('.close', $popup).click(function() {
            //// do something when dialog is closing
        //});
    //});
});
