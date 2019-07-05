window.onload = function() {

     var req = new XMLHttpRequest();
     req.responseType = 'json';
     req.open("GET", "http://0.0.0.0:8008/test", true); 
     req.onload = function(){
         var jr = req.response;
         var json = JSON.stringify(jr);
          
         alert(json.lenght);

        
     };
     req.send(null);
    /*
     var x = "hello";
     var canvas = document.getElementById("canvas-robot-info");
     var ctx = canvas.getContext("2d");
     ctx.font = "30px Arial";
     ctx.fillText(x, 10, 50);
    */
   }