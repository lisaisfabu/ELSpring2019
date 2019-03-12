myclick();

function myclick(){
    console.log("print");
    
    $.getJSON('/fetch', function(data) {
            
        for(var line in data){
            console.log(data[line])
            for(var i in data[line])
                console.log(data[line][i]);
        }


        $("#basicTable tr").remove();

        var trace = {x:[], y:[], mode: 'lines+markers'}
        mytable = $('<table></table>').attr({ id: "basicTable" });
        var head = $('<tr></tr>').attr({ class: ["class1"].join(' ') }).appendTo(mytable)
        $('<th></th>').text("date/time").appendTo(head); 
        $('<th></th>').text("C").appendTo(head); 
        $('<th></th>').text("F").appendTo(head); 

        for (var line in data) {
            var row = $('<tr></tr>').attr({ class: ["class1"].join(' ') }).appendTo(mytable);
            trace.x.push(data[line][0])

            trace.y.push(data[line][2]);
            for (var i in data[line]) {
                $('<td></td>').text(data[line][i]).appendTo(row); 
            }
                    
        }
        var data = [ trace ];
        var layout = {};
        mytable.appendTo("#box");	 

        Plotly.newPlot('myGraph', data, layout, {showSendToCloud: true});

        console.log(data);
    });
}