

$(".page_item").click(function() {
  $(".page_item").removeClass("page_active");
  $(this).addClass("page_active");
})

let num=1;
  function new_deals(){
  $('<div class="deal"> Сделка '+num+'</div>').appendTo("#new_deals_column");
  num++;
  console.log(num)
}
