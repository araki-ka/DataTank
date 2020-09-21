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
    $.getJSON("https://raw.githubusercontent.com/araki-ka/DataTank/master/data/pcr_positive_daily.json", function (resp) {
      var feat = resp.features,
        tableData = [];

      // Iterate over the JSON object
      for (var row = 0, len = feat.length; row < len; i++) {
        tableData.push({
          "data": feat[row].data,
          "positive": feat[row].positive
        });
      }

      table.appendRows(tableData);
      doneCallback();
    });
  };
  tableau.registerConnector(myConnector);

  // Create event listeners for when the user submits the form
  $(document).ready(function () {
    $("#submitButton").click(function () {
      tableau.connectionName = "PCR CSV"; // This will be the data source name in Tableau
      tableau.submit(); // This sends the connector object to Tableau
    });
  });
})();
