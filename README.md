

Python Django + Rest_Framework 构建前后端分离网站脚手架 demo

* 后端实现了两个API接口，add_book、show_book

``` html
请求： http://localhost:8000/api/show_book
应答： {"list": [{"model": "api.book", "pk": 1, "fields": {"name": "abc", "author": "ABC", "add_date": "2021-01-29T09:46:41.324Z"}}, {"model": "api.book", "pk": 2, "fields": {"name": "iisfree'sbook", "author": "iisfree", "add_date": "2021-01-29T09:47:02.515Z"}}, {"model": "api.book", "pk": 3, "fields": {"name": "iisfree'sbook", "author": "iisfree2", "add_date": "2021-01-29T09:47:08.225Z"}}, {"model": "api.book", "pk": 4, "fields": {"name": "hellobook", "author": "hello", "add_date": "2021-01-29T09:47:28.546Z"}}], "msg": "success", "error_num": 0}

请求：http://localhost:8000/api/add_book?name=ahhaha&author=heihei
应答：{"msg": "success", "error_num": 0}
```

* 前段利用VUE框架，实现数据的展示和新增。

[参考文章：](https://cloud.tencent.com/developer/article/1576599)

