---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a first-year graduate student from [MSCS program](https://web.cs.dartmouth.edu/), [Dartmouth College](https://home.dartmouth.edu/), advised by [Prof.Bo Zhu](https://faculty.cc.gatech.edu/~bozhu/). My research interests lie in computer graphics, computational physics, and artificial intelligence. I received my B.E. from Nankai University, where I was advised by [Prof. Bo Ren](https://ren-bo.net/).

Email: [taiyuan.zhang.gr@dartmouth.edu](mailto: taiyuan.zhang.gr@dartmouth.edu), [imaginer.tai@gmail.com](imaginer.tai@gmail.com) / [Github]

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
