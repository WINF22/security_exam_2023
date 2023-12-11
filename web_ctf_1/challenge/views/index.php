<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>CTF Command Injection</title>
  <link rel="stylesheet" href="/static/css/style.css">

</head>

<body>
  <main>
    <div id="border">
      <wrapper>
        
        <div id="celia-window">
          <div id="term-container">
            <div id="term"></div>
            <div id="term-entry">
              <div>
                ><input type="text" class="c3" maxlength="140" />
              </div>
            </div>
          </div>
        </div>
      </wrapper>
    </div>
    <sidebar>
      
      <a id="side-celia" class="s" href="#">
        <p>Command</p>
        <img style="height: 70%;" src="/static/images/terminal.png" />
      </a>
    </sidebar>
    
    
  </main>
  <!-- partial -->
  <script src='/static/js/jquery.js'></script>
  <script src="/static/js/script.js"></script>

</body>

</html>
