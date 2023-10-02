(function () {
  // Create the connector object
  var myConnector = tableau.makeConnector();

  // Define the schema
  myConnector.getSchema = function (schemaCallback) {
    var cols = [{
      id: "date",
      dataType: tableau.dataTypeEnum.date
    }, {
      id: "tests",
      dataType: tableau.dataTypeEnum.int
    }, {
      id: "positives",
      dataType: tableau.dataTypeEnum.int
    }];

    var tableSchema = {
      id: "covid_report_in_japan",
      alias: "COVID Report in Japan",
      columns: cols
    };

    schemaCallback([tableSchema]);
  };

  // Download the data
  myConnector.getData = function (table, doneCallback) {
    $.getJSON("https://raw.githubusercontent.com/araki-ka/DataTank/master/data/COVID/covid_report.json", function (data) {
      var tableData = [];

      // Iterate over the JSON object
      for (var row = 0, len = data.length; row < len; row++) {
        tableData.push({
          "date": data[row].date,
          "tests": data[row].tests,
          "positives": data[row].positives
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
      tableau.connectionName = "COVID Report in Japan";
      tableau.submit();
    });
  });
})();
