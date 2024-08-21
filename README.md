# Mockfeed

A simple mock RSS feed API designed specifically for testing [lazyfeed](https://github.com/dnlzrgz/lazyfeed). While it may not be my finest piece of work, it does function and helps me simulate the responses I want to test in a "live" environment without hurting anyone.  
The two main endpoints are `/{site}/rss/`, which returns a randomly generated RSS feed, and `/{site}/blog/{slug}`, which returns a randomly generated HTML page for the specified blog post.  
And that's all. Have a nice day!
