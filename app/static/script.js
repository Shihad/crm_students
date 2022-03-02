
$(".page_item").click(function() {
  $(".page_item").removeClass("page_active");
  $(this).addClass("page_active");
})

  let num=1;


  function new_deals(){
    $( "#dialog_add_deal" ).dialog( "open" );
    console.log(343)
}

$( function () {
  $("#dialog_add_deal").dialog({
    autoOpen: false,
    show: {
      effect: "blind",
      duration: 100
    },
    hide: {
      effect: "blind",
      duration: 100
    },
    resizable:false,
    height:"auto",
    width:400
  /*  modal:true,
    buttons: {
      "Создать сделку": function() {
                create_deals()
        $(this).dialog("close");
      },
      "Отмена": function () {
          $(this).dialog("close");
      }

    }*/
  });
});

$( function() {
  $( "#datepicker_start" ).datepicker();
    $( "#datepicker_end" ).datepicker();
} );

$('.deals_column').droppable({
      drop: function(event, ui) {

           ui.draggable.appendTo(event.target);
           ui.draggable.removeClass("*");
           ui.draggable.addClass("deal")
           if (event.target.id=="new_deals_column") {
             ui.draggable.addClass("deal_new");
             ui.draggable.text("Новая");
           }
           if (event.target.id=="prepare_deals_column") {
             ui.draggable.addClass("deal_prepare");
             ui.draggable.text("Подготовка");
             $.post( "/index", { desk: desk, firstDate: "2pm",lastDate:"2pm" } );
           }
           if (event.target.id=="working_deals_column") {
             ui.draggable.addClass("deal_work");
             ui.draggable.text("В работе");
           }
           if (event.target.id=="closed_deals_column") {
             ui.draggable.addClass("deal_close");
             ui.draggable.text("Закрыта");
           }
           console.log(event.target);
      }
  });

function create_deals (){
    console.log ('3')

    let desk=$( "input[name=description]" ).val();
    var firstDate = $( "#datepicker_start" ).datepicker( "getDate" );
    var lastDate = $( "#datepicker_end" ).datepicker( "getDate" );
    $.post( "deals", { desk: desk, firstDate: "2pm",lastDate:"2pm" } );
  $('<div class="deal">' +desk +'<br>' +firstDate+'<br>' +lastDate+'</div>' ).appendTo("#new_deals_column");
  num++;

  $(function() {

      $('.deal').draggable(
    {
        containment: "#deals_container",
        revert:"invalid"
      }
    );

  })
}

$(function() {

    $('.deal').draggable(
  {
      containment: "#deals_container",
      revert:"invalid"
    }
  );

});


/*
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
        revert:"invalid"
      }
    );

  });
}

$('.deals_column').droppable({
      drop: function(event, ui) {

           ui.draggable.appendTo(event.target);
           ui.draggable.removeClass("*");
           ui.draggable.addClass("deal")
           if (event.target.id=="new_deals_column") {
             ui.draggable.addClass("deal_new");
             ui.draggable.text("Новая");
           }
           if (event.target.id=="prepare_deals_column") {
             ui.draggable.addClass("deal_prepare");
             ui.draggable.text("Подготовка");
           }
           if (event.target.id=="working_deals_column") {
             ui.draggable.addClass("deal_work");
             ui.draggable.text("В работе");
           }
           if (event.target.id=="closed_deals_column") {
             ui.draggable.addClass("deal_close");
             ui.draggable.text("Закрыта");
           }
           console.log(event.target);
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
