clickMe();
setInterval(() => {
    clickMe()
}, 10000);

function clickMe() {
    $.getJSON('/catch', function(data) {
        for(var line in data) {
            console.log(data[line])

            for(var i in data[line])
                console.log(data[line][i])
        }

        $("#myTable tr").remove();
        $("#heading").remove();

        var trace = {x:[], y:[], name:'IN', type:'bar'}
        var trace2 = {x:[], y:[], name:'OUT', type:'bar'}

        var total = 0

        lisaTable = $('<table></table>').attr({ id: "myTable" });
        var head = $('<tr></tr>').attr({ class: ["class1"].join(' ') }).appendTo(lisaTable)
        $('<th></th>').text("date/time IN").appendTo(head); 
        $('<th></th>').text("IN").appendTo(head); 
        $('<th></th>').text("date/time OUT").appendTo(head);
        $('<th></th>').text("OUT").appendTo(head);
        $('<th></th>').text("TOTAL").appendTo(head);

        total = data[0][4]

        for (var line in data) {
            var row = $('<tr></tr>').attr({ class: ["class1"].join(' ') }).appendTo(lisaTable);
            
            trace.x.push(data[line][0])
            trace.y.push(data[line][1])
            trace2.x.push(data[line][2])
            trace2.y.push(data[line][3])

            for (var i in data[line]) {
                $('<td></td>').text(data[line][i]).appendTo(row); 
            }

                    
        }

        var data = [ trace, trace2 ];
        var layout = {barmode: 'group'};

        var totalNow = $("<h1></h1>").text("Total People in Room: " + total).attr({ id:"heading"}).appendTo("#table")

        lisaTable.appendTo("#table")

        Plotly.newPlot('myGraph', data, layout, {}, {showSendToCloud: true})
    })
}