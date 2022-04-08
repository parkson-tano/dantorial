$(document).ready(function () {
  $(".likebtn").click(function (event) {
    event.preventDefault();
    var ansid = $(this).attr("id");
    console.log(ansid);
    console.log("clicked:" + ansid);
    $.ajax({
      url: $(this).data("url"),
      type: "POST",
      data: {
        profile_id: ansid,
        csrfmiddlewaretoken: "{{csrf_token}}",
        action: "post",
      },
      success: function (response) {
        $("#like_count").text(response["total_favourites"]);
        console.log("clicked:" + ansid);
        console.log("response: number  " + response.total_favourites);
        console.log("response: flag  " + response.flag);
        if (response["flag"] == true) {
          // $('#'+ansid).style.color = 'blue';
          document.getElementById("co").style.color = "blue";
          // alert('you like this profile')

          console.log("successfully  added to favorites");
        } else {
          $("#" + ansid).removeClass("text-success");
          document.getElementById("co").style.color = "black";
          console.log("successfully removed to favorites");
          // alert('u dislike this')
        }
      },
      error: function (rs, e) {
        console.log("error: " + rs.response, ansid);
      },
    });
  });
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
$(".select2").select2({
  placeholder: "Select a subject",
  allowClear: true,
  containerCssClass: ":all:",
  // theme: "classic"
});
$(".town").select2({
  placeholder: "Select town",
  allowClear: true,
  containerCssClass: ":all:",
  // theme: "classic"
});
$(".quater").select2({
  placeholder: "Select Quater",
  allowClear: true,
  containerCssClass: ":all:",
  // theme: "classic"
});