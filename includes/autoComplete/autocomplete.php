<?php
require "../login.php";
// Get search term
$searchTerm = $_GET['txtpname'];

// Modify the query temporarily (remove prepared statement for debugging)
$searchTerm = $_GET['txtpname'];
$searchTermWithWildcard = $searchTerm . "%";

// Construct the SQL query
$query = "SELECT PlayerID, Name FROM player WHERE firstName LIKE '$searchTermWithWildcard' or  lastName LIKE '$searchTermWithWildcard' or  middleName LIKE '$searchTermWithWildcard' or name like '$searchTermWithWildcard' ORDER BY Name ASC";


// Execute the query
$result = mysqli_query($conn, $query);


// Generate array with possible names
$nameData = array();

// Fetch results
while ($row = mysqli_fetch_assoc($result)) {
    $data['id'] = $row['PlayerID'];
    $data['value'] = $row['Name'];
    array_push($nameData, $data);
}

// Return results as a JSON-encoded array
echo json_encode($nameData);

// Close connection
mysqli_close($conn);
?>
