### responseType ###
是XMLHttpRequest对象和fetch API（在 JavaScript 用于获取网络资源）中的一个属性，用于指定**希望**（实际可能不一致）服务器返回数据的类型。
它允许开发者明确地告诉浏览器如何处理和解析从服务器接收到的数据。

### content-type ###
是一个 HTTP 头部字段，用于表示请求或响应中实体（通常是消息体）的媒体类型。
在请求中，它告诉服务器发送的数据格式；
在响应中，它告诉客户端（如浏览器）返回的数据格式。
常见的content-type值有text/html（HTML 文档）、application/json（JSON 数据）、text/plain（纯文本）、image/jpeg（JPEG 图像）等。服务器会根据content-type来正确地解析请求数据，客户端也会根据content - type来决定如何显示或处理响应数据。

### overrideMimeType ###

overrideMimeType是XMLHttpRequest对象的一个方法。
它用于覆盖服务器返回数据的content-type（MIME 类型）。
通常在服务器返回的content-type不准确或者开发者希望以特定方式解析数据时使用。

当overrideMimeType被使用时，它会改变浏览器解析服务器返回数据的方式，而这种改变可能与服务器发送的content-type（通过 HTTP 头部字段发送）不一致。
responseType和overrideMimeType都在客户端（浏览器）这一侧用于处理数据解析，content-type则是服务器和客户端之间沟通数据格式的一个重要桥梁。
例如，如果responseType被设置为"json"，但服务器返回的content-type是text/plain，并且使用overrideMimeType将其强制改为application/json，那么浏览器仍然会尝试将数据解析为 JSON 对象，这就体现了它们之间的相互作用。

### 预检请求（Pre - flight Request）机制 ###
非简单请求在实际发送请求之前，浏览器会自动发起一个预检请求（OPTIONS 方法）到服务器。
这是因为非简单请求可能会对服务器资源产生更多的潜在影响，比如跨域情况下修改服务器数据等操作。
预检请求的目的是询问服务器是否允许真正的请求发送，它会携带一些信息，如请求方法、请求头和 Content-Type 等。
例如，一个带有自定义头部 “X-Custom-Header: value” 的 PUT 请求，预检请求会包含这个头部信息，让服务器确认是否接受带有此头部的 PUT 请求。
服务器收到预检请求后，会根据自身的策略进行响应。如果服务器允许该请求，会返回一个包含允许的方法、头部等信息的响应，响应中会包含如 Access-Control-Allow-Methods（允许的请求方法）、Access-Control-Allow-Headers（允许的请求头部）等头部字段。

### 非简单请求 ###

在 HTTP 中，非简单请求是相对于简单请求而言的。简单请求是指满足以下条件的请求：
* 请求方法是 GET、POST 或 HEAD。
* 除了被用户代理自动设置的首部（例如 Connection、User - Agent）和在 Fetch 规范中定义为禁止修改的首部（如 Range）之外，请求首部不包含自定义的其他首部。
* 请求中的 Content - Type 仅限于 application/x - www - form - urlencoded、multipart/form - data 或 text/plain。
不满足以上这些条件的请求就是非简单请求。例如，使用 PUT、DELETE 等其他 HTTP 方法的请求，或者包含自定义首部（如 Authorization: Bearer xxx）且内容类型不是简单类型的请求等