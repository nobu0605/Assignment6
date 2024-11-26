<!DOCTYPE html>
<html>
<head>
    <title>User Input Form</title>
</head>
<body>
    <form action="process.php" method="get">
        <label for="integers">Enter a list of integers (separated by commas):</label><br>
        <input type="text" id="integers" name="integers" placeholder="e.g., 3,5,7,9"><br><br>

        <label for="threshold">Enter a threshold value:</label><br>
        <input type="text" id="threshold" name="threshold" placeholder="e.g., 4"><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
