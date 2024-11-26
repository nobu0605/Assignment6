<?php
if (isset($_GET['integers']) && isset($_GET['threshold'])) {
    $integers = $_GET['integers'];
    $threshold = $_GET['threshold'];

    // Command to call the Python script
    $command = escapeshellcmd("python3 bitwise_operations.py " . escapeshellarg($integers) . " " . escapeshellarg($threshold));
    $output = shell_exec($command);

    // Decode the JSON output from Python
    $result = json_decode($output, true);

    if (isset($result['error'])) {
        echo "<h3>Error: " . htmlspecialchars($result['error']) . "</h3>";
    } else {
        echo "<h3>Bitwise Operations:</h3>";
        echo "AND: " . htmlspecialchars($result['bitwise']['and']) . "<br>";
        echo "OR: " . htmlspecialchars($result['bitwise']['or']) . "<br>";
        echo "XOR: " . htmlspecialchars($result['bitwise']['xor']) . "<br>";

        echo "<h3>Filtered Numbers (greater than threshold):</h3>";
        echo "[" . implode(", ", $result['filtered']) . "]";
    }
} else {
    echo "<h3>Error: Please provide both integers and a threshold.</h3>";
}
?>
