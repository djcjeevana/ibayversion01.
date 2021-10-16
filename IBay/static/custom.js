$(document).ready(function(){
	

	$("#addToCartBtn").on('click', function(){
		var _vm=$(this);
		
		var _productid=$(".product-id").val();
		var _productim=$(".product-image").val();
		var _productitle=$(".product-title").val();
		var _productqty=$("#productQty").val();
		var _producpric=$(".product-price").text();
		
		$.ajax({
			url:'/add-to-cart',
			data:{
				'id':_productid,
				'qty':_productqty,
				'title':_productitle,
				'price':_producpric,
				'image':_productim
				
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		});

	});


	


});
// End Document.Ready

