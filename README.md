# Rest Api with Flask used to represent data with Plotly.js
Here are the examples with to start with to send data to the app:
curl "http://127.0.0.1:5000" --data-urlencode "data={""x"": [10,20],""y"":[11,12]}" -X POST
curl "http://127.0.0.1:5000" -H "Content-Type: application/json" -d "{""test2"":{""x"":[1,2],""y"":[3,4]}}" -X POST