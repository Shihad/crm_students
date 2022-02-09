

$(".page_item").click(function() {
  $(".page_item").removeClass("page_active");
  $(this).addClass("page_active");
})

let num=1;
  function new_deals(){
  $('<div class="deal"> Сделка '+num+'</div>').appendTo("#new_deals_column");
  num++;

  $(function() {

  	$('.deal').draggable(
    {
        containment: "#deals_container",
        snap: ".deals_column",
        snapMode: "top",
        snapTolerance: 50
      }
    );

  });
}

$('.deals_column').droppable({
      drop: function(event, ui) {
           ui.draggable.text("Оставлено")
      }
  });
/*
function prepare_deals() {
  $('<div class="deal"> Документ '+num+'</div>').appendTo("#prepare_deals_column");
  num++;
}

function working_deals() {
  $('<div class="deal"> Сделка '+num+'</div>').appendTo("#working_deals_column");
  num++;
}

function closed_deals() {
  $('<div class="deal"> Сделка '+num+'</div>').appendTo("#closed_deals_column");
  num++;
}*/
