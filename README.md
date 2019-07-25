# Lardy Sigh
A simple Rails log parser

## Usage
Lardy Sigh parses rails server log into individual requests and filters requests with specified terms.
Below are some examples:


### Raw log file
```
> cat example.log
I, [2017-01-20T07:30:26.191095 #26619]  INFO -- : Started GET "/microposts/1732" for 198.51.100.87 at 2017-01-20 07:30:26 +0000
I, [2017-01-20T07:30:26.191655 #20920]  INFO -- : Started POST "/microposts" for 203.0.113.187 at 2017-01-20 07:30:26 +0000
I, [2017-01-20T07:30:26.192095 #25847]  INFO -- : Started GET "/microposts/1414" for 198.51.100.187 at 2017-01-20 07:30:26 +0000
I, [2017-01-20T07:30:26.193120 #26619]  INFO -- : Processing by MicropostsController#show as JSON
I, [2017-01-20T07:30:26.193181 #26619]  INFO -- :   Parameters: {"micropost_id"=>"1732"}
I, [2017-01-20T07:30:26.194120 #25847]  INFO -- : Processing by MicropostsController#show as JSON
I, [2017-01-20T07:30:26.194181 #25847]  INFO -- :   Parameters: {"micropost_id"=>"1414"}
I, [2017-01-20T07:30:26.195677 #26619]  INFO -- : Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
I, [2017-01-20T07:30:26.196177 #20920]  INFO -- : Processing by MicropostsController#create as JSON
I, [2017-01-20T07:30:26.196243 #20920]  INFO -- :   Parameters: {"micropost"=>{"title"=>"Lardy Sigh", "content"=>"Pang"}}
I, [2017-01-20T07:30:26.196677 #25847]  INFO -- : Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
I, [2017-01-20T07:30:26.207898 #20920]  INFO -- : Completed 201 Created in 16ms (Views: 0.6ms | ActiveRecord: 4.2ms)

```


### Simple Parsing
```
> cat example.log | python lds.py
================================================================================
2017-01-20T07:30:26.191095 Started GET "/microposts/1732" for 198.51.100.87 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.193120 Processing by MicropostsController#show as JSON
2017-01-20T07:30:26.193181 Parameters: {"micropost_id"=>"1732"}
2017-01-20T07:30:26.195677 Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
================================================================================
2017-01-20T07:30:26.192095 Started GET "/microposts/1414" for 198.51.100.187 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.194120 Processing by MicropostsController#show as JSON
2017-01-20T07:30:26.194181 Parameters: {"micropost_id"=>"1414"}
2017-01-20T07:30:26.196677 Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
================================================================================
2017-01-20T07:30:26.191655 Started POST "/microposts" for 203.0.113.187 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.196177 Processing by MicropostsController#create as JSON
2017-01-20T07:30:26.196243 Parameters: {"micropost"=>{"title"=>"Lardy Sigh", "content"=>"Pang"}}
2017-01-20T07:30:26.207898 Completed 201 Created in 16ms (Views: 0.6ms | ActiveRecord: 4.2ms)
================================================================================
```


### Single term filtering
Only show the requests with the term *show* in it.
```
> cat example.log | python lds.py show
show
================================================================================
2017-01-20T07:30:26.191095 Started GET "/microposts/1732" for 198.51.100.87 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.193120 Processing by MicropostsController#show as JSON
2017-01-20T07:30:26.193181 Parameters: {"micropost_id"=>"1732"}
2017-01-20T07:30:26.195677 Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
================================================================================
2017-01-20T07:30:26.192095 Started GET "/microposts/1414" for 198.51.100.187 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.194120 Processing by MicropostsController#show as JSON
2017-01-20T07:30:26.194181 Parameters: {"micropost_id"=>"1414"}
2017-01-20T07:30:26.196677 Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
================================================================================
```


### Multile terms filtering
Only show the requests with both the term *show* and the IP *198.51.100.87*.
```
> cat example.log | python lds.py show 198.51.100.87
show
198.51.100.87
================================================================================
2017-01-20T07:30:26.191095 Started GET "/microposts/1732" for 198.51.100.87 at 2017-01-20 07:30:26 +0000
2017-01-20T07:30:26.193120 Processing by MicropostsController#show as JSON
2017-01-20T07:30:26.193181 Parameters: {"micropost_id"=>"1732"}
2017-01-20T07:30:26.195677 Completed 200 OK in 2ms (Views: 0.2ms | ActiveRecord: 0.4ms)
================================================================================
```


## About
> Lardy sees the messy log file of a rails server, sighs, and wrote this utility.


