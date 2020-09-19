(function () {
  // Create the connector object
  var myConnector = tableau.makeConnector();

  // Define the schema
  myConnector.getSchema = function (schemaCallback) {
    var cols = [{
      id: "date",
      dataType: tableau.dataTypeEnum.date
    }, {
      id: "positive",
      dataType: tableau.dataTypeEnum.int
    }];

    var tableSchema = {
      id: "pcr",
      alias: "PCR CSV",
      columns: cols
    };

    schemaCallback([tableSchema]);
  };

  // Download the data
  myConnector.getData = function (table, doneCallback) {
    var settings = {
      "url": "https://raw.githubusercontent.com/araki-ka/DataTank/master/data/pcr_positive_daily.csv",
      "method": "GET",
      "timeout": 0,
      "headers": {
        "Content-Type": "text/csv"
      },
    };

    $.ajax(settings).done(function (response) {
      console.log(response);
      var feat = response.features,
        tableData = [];

      // Iterate over the CSV object
      for (var i = 0, len = feat.length; i < len; i++) {
        tableData.push({
          "data": feat[i][0],
          "positive": feat[i][2]
        });
      }

      table.appendRows(tableData);
      doneCallback();
    });
  };
  tableau.registerConnector(myConnector);

    // Create event listeners for when the user submits the form
    $(document).ready(function() {
        $("#submitButton").click(function() {
            tableau.connectionName = "PCR CSV"; // This will be the data source name in Tableau
            tableau.submit(); // This sends the connector object to Tableau
        });
    });
})();
