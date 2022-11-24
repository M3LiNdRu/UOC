const express = require('express')
const { createProxyMiddleware } = require('http-proxy-middleware')
var request = require('request')

const app = express()
const port = 3000
const headers = {
  "Connection": "keep-alive"
}
const loglevel = "debug"

app.use(express.json());


app.use('/api/v2/me', createProxyMiddleware({
  target: "https://api.linkedin.com",
  secure: true,
  changeOrigin: true,
  pathRewrite: { "^/api": "" },
  headers: headers,
  logLevel: loglevel
}))

app.use('/api/v2/ugcPosts', createProxyMiddleware({
  target: "https://api.linkedin.com",
  secure: true,
  changeOrigin: true,
  pathRewrite: { "^/api": "" },
  headers: headers,
  logLevel: loglevel
}))

app.use('/oauth/v2/accessToken', function(req, res){
  request.post(
    {
      url:'https://www.linkedin.com/oauth/v2/accessToken',
      form: {
        grant_type: 'authorization_code',
        code: req.body.code,
        client_id: '78412qx611f4v7',
        client_secret: '',
        redirect_uri: 'https://localhost:4200'
      }
    },
    function(error, response, body){
      res.send(body);
    });
});

app.get('/hello', (req, res) => {
  res.send('Hello World!')
})

app.listen(port)