<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quote Generator</title>
  <style>
    /* This section controls how everything looks */

    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
      font-family: sans-serif;
    }

    .card {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 16px;
      padding: 40px;
      max-width: 500px;
      width: 90%;
      text-align: center;
    }

    h1 {
      color: #ffffff;
      font-size: 22px;
      font-weight: 500;
      margin: 0 0 32px 0;
    }

    .quote-text {
      color: #ffffff;
      font-size: 18px;
      line-height: 1.7;
      font-style: italic;
      margin: 0 0 16px 0;
      min-height: 80px;
    }

    .quote-author {
      color: rgba(255, 255, 255, 0.5);
      font-size: 14px;
      margin: 0 0 32px 0;
    }

    button {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      border: none;
      padding: 14px 36px;
      border-radius: 50px;
      font-size: 15px;
      cursor: pointer;
    }

    button:hover {
      opacity: 0.85;
    }

    .loading {
      color: rgba(255,255,255,0.4);
      font-size: 14px;
      margin-top: 12px;
      min-height: 20px;
    }
  </style>
</head>
<body>

  <div class="card">
    <h1>✨ Daily Quote Generator</h1>

    <!-- This is where the quote will appear -->
    <p class="quote-text" id="quote-text">Click the button to get your first quote!</p>
    <p class="quote-author" id="quote-author"></p>

    <!-- This button triggers the API call -->
    <button onclick="getQuote()">Get New Quote</button>

    <p class="loading" id="loading"></p>
  </div>

  <script>
    // IMPORTANT: Replace this with YOUR API Gateway URL
    const API_URL = "https://dszrqsbiui.execute-api.eu-west-2.amazonaws.com/prod/quotes";

    async function getQuote() {
      // Show a loading message while we wait
      document.getElementById("loading").textContent = "Loading...";

      // Call your API and wait for the response
      const response = await fetch(API_URL);
      const data = await response.json();

      // Put the quote on the page
      document.getElementById("quote-text").textContent = data.text;
      document.getElementById("quote-author").textContent = "— " + data.author;
      document.getElementById("loading").textContent = "";
    }
  </script>

</body>
</html>