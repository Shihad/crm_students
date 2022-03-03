

function active_list(header_id) {
  $(".nonactive").removeClass("active");
  $(header_id).addClass("active");
  if (header_id =='#chats'){
    $(".nonactive2").removeClass("active2");
    $("#main_chats").addClass("active2");
    $('#plus').css("display", 'block');
    $('#search').css("display", 'block');
    $('#menu').css("display", 'block');
  }
  else if (header_id =='#notice') {
    $(".nonactive2").removeClass("active2");
    $("#main_notice").addClass("active2");
    $('#plus').css("display", 'none');
    $('#search').css("display", 'none');
    $('#menu').css("display", 'block');
  }
  else {
    $(".nonactive2").removeClass("active2");
    $("#main_lines").addClass("active2");
    $('#plus').css("display", 'none');
    $('#search').css("display", 'none');
    $('#menu').css("display", 'none');
  }
}

function openDialog(  ) {
  $( "#dialog" ).dialog( "open" );
}


$(function () {
  $( "#dialog" ).dialog({
    autoOpen: false,
    width: 400,
    buttons: [
      {
        text: "Отмена",
        click: function() {
          $( this ).dialog( "close" );
        }
      }
    ]
  });
})


function new_menu() {
  document.getElementById("myDropdown").classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

class Person {
  constructor(x) {
  }
}

console.log(name);

function new_person() {
  let name = prompt('Введите ФИО нового сотрудника');
  var m = document.createElement("div");
  m.className = "message";
  document.getElementById("main_chats").appendChild(m);
  /*var t = document.createElement("div");
  t.className = "text";
  document.getElementsByClassName("message").appendChild(t);*/
}
