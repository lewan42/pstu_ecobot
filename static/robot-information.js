$.ajax({
  url: "http://0.0.0.0:8008/test"
})
  .done(function(data) {

      console.log(data);
      console.log(data.angle_wheels.angle_wheels);
     
      $(".robot-information").append("<h3 class='robot-information-h'> Angle wheels</h3>");
      $(".robot-information").append("<p class='robot-information-p'> Angle wheels = " + data.angle_wheels.angle_wheels +"</p>");
      $(".robot-information").append("<p class='robot-information-p'> State = " + data.angle_wheels.state +"</p>");

      //$(".robot-information").append("<h3 class='robot-information-h'> Camera zoom</h3>");
      //$(".robot-information").append("<p class='robot-information-p'> Camera zoom = " + data.camera_zoom.camera_zoom +"</p>");
      //$(".robot-information").append("<p class='robot-information-p'> State = " + data.camera_zoom.state +"</p>");

      $(".robot-information").append("<h3 class='robot-information-h'> Position</h3>");
      $(".robot-information").append("<p class='robot-information-p'> Position X = " + data.position.posX +"</p>");
      $(".robot-information").append("<p class='robot-information-p'> Position Y = " + data.position.posY +"</p>");
      $(".robot-information").append("<p class='robot-information-p'> State = " + data.position.state +"</p>");

      $(".robot-information").append("<h3 class='robot-information-h'> Speed</h3>");
      $(".robot-information").append("<p class='robot-information-p'> Speed = " + data.speed.speed +"</p>");
      $(".robot-information").append("<p class='robot-information-p'> State = " + data.speed.state +"</p>");

      //$(".robot-information").append("<h3 class='robot-information-h'> Time</h3>");
      //$(".robot-information").append("<p class='robot-information-p'> Time = " + data.time.time +"</p>");
      //$(".robot-information").append("<p class='robot-information-p'> State = " + data.time.state +"</p>");

    
  });


