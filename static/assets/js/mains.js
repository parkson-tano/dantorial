$(document).ready(function () {
  $(".likebtn").click(function (event) {
    event.preventDefault();
    var profile_id = $(this).attr("id");
    console.log(profile_id);
    console.log("clicked:" + profile_id);
    $.ajax({
      url: $(this).data("url"),
      type: "GET",
      data: {
        profile_id: profile_id,
        action: "get",
      },
      success: function (response) {
        $("#like_count").text(response["total_favourites"]);
        console.log("clicked:" + profile_id);
        console.log("response: number  " + response.total_favourites);
        console.log("response: flag  " + response.flag);
        // console.log("response  " + response)
        if (response.flag == true) {
          document.getElementById("co").style.color = "blue";

          console.log("successfully  added to favorites");
        } else {
          $("#" + profile_id).removeClass("text-success");
          document.getElementById("co").style.color = "black";
          console.log("successfully removed to favorites");
        }
      },
      error: function (rs, e) {
        console.log("error: " + rs.response, profile_id);
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
