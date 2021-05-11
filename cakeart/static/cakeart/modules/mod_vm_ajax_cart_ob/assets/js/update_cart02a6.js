;
(function (jQuery) {

    jQuery.fn.updateVirtueMartCartModule = function (arg) {

        var options = jQuery.extend({}, jQuery.fn.updateVirtueMartCartModule.defaults, arg);

        return this.each(function () {

            // Local Variables
            var $this = jQuery(this);

            jQuery.ajaxSetup({ cache: false })
            jQuery.getJSON(window.vmSiteurl + "index.php?option=com_ajax&module=vm_ajax_cart_ob&method=viewJS&format=json" + window.vmLang,
                function (datas, textStatus) {
                    if (datas.totalProduct > 0) {
                        $this.find(".vm_cart_products").html('<ul class="cart_list"></ul>');
                        jQuery.each(datas.products, function (key, val) {
                            //jQuery("#hiddencontainer .vmcontainer").clone().appendTo(".vmcontainer .vm_cart_products");
                            jQuery("#hiddencontainer .vmcontainer").clone().appendTo(".vmCartModule .vm_cart_products ul.cart_list");
                            jQuery.each(val, function (key, val) {
                                if (jQuery("#hiddencontainer .vmcontainer ." + key)) $this.find(".vm_cart_products ." + key + ":last").html(val);
                            });
                        });
                    }
                    $this.find(".total_products").html(datas.totalProduct);

                        jQuery(".vm_cart_products").append('<p class="total">'+datas.billTotal+'</p>');

                        jQuery(".vm_cart_products").append('<p class="buttons show_cart">'+datas.cart_show+'</p>');
                }
            );
        });
    };

    // Definition Of Defaults
    jQuery.fn.updateVirtueMartCartModule.defaults = {
        name1: 'value1'
    };

})(jQuery);