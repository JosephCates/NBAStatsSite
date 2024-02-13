<?php
function printTable($colNames, $data, $caller) {
    echo "<table border='1'>";
    echo "<tr>";
    // Print the header
    foreach ($colNames as $colName) {
        echo "<th>$colName</th>";
    }
    echo "</tr>";

    // Print the rows
    foreach ($data as $row) {
        echo "<tr>";
        foreach ($colNames as $colName) {
            echo "<td>".$row[$colName]."</td>";
          }
        echo "</tr>";
      }
    echo "</table>";
}
?>
