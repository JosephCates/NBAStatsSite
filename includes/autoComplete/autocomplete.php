<?php
require "../login.php";
$searchTerm = $_GET['txtpname'];
$searchTermWithWildcard = $searchTerm . "%";

$stmt = $conn->prepare("
    SELECT PlayerID, Name FROM player 
    WHERE firstName LIKE ? 
    OR lastName LIKE ? 
    OR middleName LIKE ? 
    OR name LIKE ? 
    ORDER BY Name ASC
");
$stmt->bind_param("ssss", $searchTermWithWildcard, $searchTermWithWildcard, $searchTermWithWildcard, $searchTermWithWildcard);
$stmt->execute();
$result = $stmt->get_result();

$nameData = array();
while ($row = $result->fetch_assoc()) {
    $data['id'] = $row['PlayerID'];
    $data['value'] = $row['Name'];
    array_push($nameData, $data);
}

echo json_encode($nameData);
mysqli_close($conn);
?>