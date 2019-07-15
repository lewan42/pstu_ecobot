// var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };

var today  = new Date();

Number.prototype.pad = function(size) {
    var s = String(this);
    while (s.length < (size || 2)) {s = "0" + s;}
    return s;
  }

function toggleRouteOn()
{
    var nav = document.getElementById('route-container')
    if (nav.style.display == "block")
    {
        nav.style.display = "none";
    }
    else
    {
        nav.style.display = 'block';
    }
}

function setMapHeight()
{
    // basicW = 2256;
    // basicH = 1476;
    basicW = 1770;
    basicH = 1110;
    var container = document.getElementsByClassName("container")[0];
    // container.style.width = (basicW / basicH) * container.clientHeight + "px";
    container.style.height = (basicH / basicW) * container.clientWidth + "px";
}

// function printMousePos(event) {
//     console.log("clientX: " + event.clientX + " - clientY: " + event.clientY);
//   }

function showName(event, name)
{
    var tooltip = document.getElementsByClassName("object-title")[0];
    tooltip.style.display = 'block';
    tooltip.style.left = event.clientX+"px";
    tooltip.style.top = (event.clientY - 30)+"px";
    tooltip.innerHTML = name;
    // alert(name);
}

function hideName()
{
    var obj = document.getElementsByClassName("object-title")[0];
    if (obj.style.display == "block")
    {
        obj.style.display = "none";
    }
}

function setBotMarker(basicW, bot_x, bot_y)
{
    var container = document.getElementsByClassName("container")[0];
    var scale = container.clientWidth / basicW;
    var bot = document.getElementById("bot");
    bot.style.left = bot_x*scale+"px";
    bot.style.top = bot_y*scale+"px";
    // bot.style.width = 30 * scale + "px";
}

function setMapImage(mapfile)
{
    console.log(mapfile);
    if (mapfile)
    {
        console.log(1);
        var container = document.getElementsByClassName("container")[0];
        container.style.backgroundImage = 'url("'+mapfile+'")';
    }

}

function loadData(basicW, basicH, data)
{
    // document.addEventListener("click", printMousePos);
    var layer = document.getElementsByClassName("object-layer")[0];
    // container.style.width = (basicW / basicH) * container.clientHeight + "px";
    layer.style.height = (basicH / basicW) * layer.clientWidth + "px";
    var scale = layer.clientWidth / basicW;
    // var scaleH =  layer.clientHeight / basicH;
    // console.log(layer.clientWidth, layer.clientHeight);
    // console.log(scale, scaleH);
    Array.forEach(data, function(element) {

        var el = document.createElement('div');
        // console.log(element);
        el.style.position = 'absolute';
        el.style.left = element.loc[0]*scale + "px";
        el.style.top = element.loc[1]*scale + "px";
        // el.style.top =  (element.loc[1] / element.loc[0]) * (element.loc[0]*scaleH) + "px";;
        el.style.width = element.size[0]*scale + "px";
        el.style.height = element.size[1]*scale + "px";
        // el.style.height = (element.size[1] / element.size[0]) * (element.size[0]*scale) + "px";
        el.style.border = "3px solid red";
        el.onclick = function(event) { showName(event, element.name) };
        // console.log(el.style.left,  el.style.top)
        // console.log(el.style.width, el.style.height);
        layer.appendChild(el);
    });
}

function getPath2()
{
    let objectName = document.getElementById('route-to').value;    
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4)
            {
                //let points = JSON.parse(xmlHttp.responseText);
                let points = xmlHttp.responseText;
                //let arr = [[1,1], [2,5], [3,6], [5,6], [7,7]]
                console.log("points " + points); 
                drawPath(points);
            }
    }
    console.log(objectName);
    xmlHttp.open("POST", '/setroute?name='+objectName+'', true); // true for asynchronous 
    xmlHttp.send();
}

function getPath()
{
            $.ajax({
              type: 'POST',
              url: "/setroute2",
              contentType: "application/x-www-form-urlencoded",
              data: {"route_to": document.getElementById('route-to').value},
              success: function(response) {
                console.log(response)
              }
            });
}

// function getPathPromise(objectName)
// {
//     return new Promise(function(resolve, reject)
//     {
//         var xhr = new XMLHttpRequest();
//         xhr.open('GET', '/setroute?name='+objectName+'', true);

//         xhr.onload = function()
//         {
//             if (this.status == 200)
//             {
//                 console.log(this.responseText);
//                 resolve(this.responseText);
//             }
//             else
//             {
//                 var error = new Error(this.statusText);
//                 error.code = this.status;
//                 reject(error);
//             }
//         };

//         xhr.onerror = function()
//         {
//             reject(new Error("Network Error"));
//         };

//         xhr.send();
//     });
// }

function drawPath(points)
{
    let cont = document.getElementById('svg-c')
    while (cont.firstChild)  // нужно очистить контейнер от старого пути, если таковой был
    {
        cont.removeChild(cont.firstChild);
    }
    let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg")
    svg.setAttribute('viewBox', '0 0 1710 1110')
    let pl = document.createElementNS("http://www.w3.org/2000/svg", "polyline")
    for (value of points)
    {
        let p =  svg.createSVGPoint();
        p.x = value[0]-10;
        p.y = value[1]
        // p.x = value[0]-20;
        // p.y = value[1]-5
        pl.points.appendItem(p)
    }
    pl.style.stroke = 'blue';
    pl.style.fill = 'none';
    pl.style.strokeWidth = '3';
    svg.appendChild(pl);
    cont.appendChild(svg);
}
