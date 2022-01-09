$(".btn").click(function() {
  var label = $(".btn").text().trim();
  if(label == "Hide") {
    $(".btn").text("Show");
    $(".myText").hide();
  }
  else {
    $(".btn").text("Hide");
    $(".myText").show();
  }
});