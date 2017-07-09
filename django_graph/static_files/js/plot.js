(function(f){
  const webSocketBridge = new channels.WebSocketBridge();
  webSocketBridge.connect('/ws/');
  webSocketBridge.listen();

  webSocketBridge.socket.addEventListener('open', function() {
    console.log('Connected to WebSocket');
    var subscribe = {
      action: 'subscribe',
      data: {
        action: 'create'
      }
    }
    // subscribe to to any 'create' events
    webSocketBridge.stream('random_number').send(subscribe);

    var listRecords = {
      action: "list",
      data: {}
    }

    // fetch initial data
    webSocketBridge.stream('random_number').send(listRecords)

    webSocketBridge.demultiplex('random_number', function(action, stream) {
      // when a "create" event has been fired, update the graph
      if(action.action === 'create') {
        // update graph
        console.log(action.data)
        Plotly.extendTraces('graph', {
          y: [[action.data.number]],
          x: [[action.data.id]]
        }, [0]);
      }

      if(action.action === 'list') {
        // initialize the graph
        var randomNumbers = action.data.map(function(item){return item.number;})
        var trace = {
          type: 'scatter',                    // set the chart type
          mode: 'lines+markers',                      // connect points with lines
          x: action.data.map(function(row) {          // set the x-data
            return row.id;
          }),
          y: action.data.map(function(row) {          // set the x-data
            return row.number;
          }),
          line: {                             // set the width of the line.
            width: 1
          }
        };
        var layout = {
          yaxis: {title: "Random Number"},      // set the y axis title
        };
        Plotly.plot('graph', [trace], layout, {showLink: false});
      }
    });
  })
})();
