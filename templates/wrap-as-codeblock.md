---
title: "<% (await tp.user.utils()).formatTitle(tp.file.title) %>"
description: ""
tags: [università, <% (await tp.user.utils()).formatTagsFromPath(tp.file.path(true)) %>]
created: <% tp.date.now("YYYY-MM-DD") %>
cssclasses: code
---
/*
```<%* "text" %>*/