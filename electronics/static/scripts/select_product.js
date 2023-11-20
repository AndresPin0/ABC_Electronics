$(document).ready(function () {
    $('a.product-link').click(function (event) {
        event.preventDefault();

        var productID = $(this).data('product-id');

        $('#selected-product-id').val(productID);

        $('form#product-form').submit();

        console.log(productID);
    });
});
