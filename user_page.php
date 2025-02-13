<?php

@include 'config.php';

session_start();

if(!isset($_SESSION['user_name'])){
   header('location:login_form.php');
}

?>

<!DOCTYPE html>
<html lang="en">
<head>

    <title>AI PROJECT</title>
    <link rel="stylesheet" href="style.css">
    
</head>
<body>
     <header>
            <div class="main">
                <div class="logo">
                    <h1>WALL-E</h1>
                </div>
                <ul>
                    <li class="active"><a href="index.html">HOME</a></li>
                    <li><a href="about.html">ABOUT</a></li>
                    <li><a href="contact.html">CONTACT</a></li>
                    <li><img src="userlogo.png"></li>
                </ul>
            </div>
          <div class="title">
              <h1>ARTIFICIAL INTELLIGENCE</h1>
          </div>
          <div class="button">
             <a href="#"  id="letsTalkBtn" class="btn">LET'S TALK</a>
             <a href="service.html" class="btn">SERVICES</a>
          </div>
          </header>
          <script>
            document.getElementById("letsTalkBtn").addEventListener("click", function() {
                window.open("vscode://"); // Open Visual Studio Code
                setTimeout(function() {
                    // Execute a command or script in Visual Studio Code
                    const vscode = acquireVsCodeApi();
                    vscode.postMessage({ command: 'runMainScript', scriptPath: 'main.py' });
                }, 2000); // Wait for 2 seconds before running the script
            });
        </script>
</body>
</html>
