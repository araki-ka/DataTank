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
      id: "pcr_positive",
      alias: "PCR Positive",
      columns: cols
    };

    schemaCallback([tableSchema]);
  };

  // Download the data
  myConnector.getData = function (table, doneCallback) {
    $.getJSON("https://raw.githubusercontent.com/araki-ka/DataTank/master/data/PCR/pcr_positive_daily.json", function (data) {
      var tableData = [];

      // Iterate over the JSON object
      for (var row = 0, len = data.length; row < len; row++) {
        tableData.push({
          "date": data[row].date,
          "positive": data[row].positive
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
      tableau.connectionName = "PCR Positive";
      tableau.submit();
    });
  });
})();
