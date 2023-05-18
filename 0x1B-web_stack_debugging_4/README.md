# 0x1B. Web stack debugging #4

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows us to simulate HTTP requests to a web server. In this case, we will make 2000 requests to our server with 100 requests at a time. We can see that some requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are our best friends!

### Command
   ab -c 100 -n 2000 localhost/
