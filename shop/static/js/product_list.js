

jQuery(function($) {
    var $list = $(".container");
    var $popup = $("#popup");

    $popup.on("click", ".close", function(event) {
        $popup.modal("hide");
        // do something when dialog is closed
    });

    $list.on("click", ".card a", function(event) {
        var link = this;
        var url = link.getAttribute("data-popup-url");
        console.log("open modal");

        if (url) {
            event.preventDefault();

            $(".modal-title", $popup).text(link.textContent);
            $(".modal-body", $popup).load(url, function() {
                $popup.on("shown.bs.modal", function () {
                    // do something when dialog is shown
                }).modal("show");
            });
        }
    });
});

