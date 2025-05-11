<h1>Django Channels</h1>

<p>Django is an open-source, high-level Python framework for web development. It’s known to be reliable, fast, and secure. The Django framework is built on Web Server Gateway Interface (WSGI), an interface for Python applications to handle synchronous requests. 

And here’s where Django Channels (or just Channels) comes in. Unlike the core Django framework, Channels isn’t underpinned by WSGI; instead, it’s built on a newer Python spec called Asynchronous Server Gateway Interface (ASGI) which supports both synchronous and asynchronous style programming. Channels extends Django’s capabilities, making it possible to handle not only HTTP, but also WebSockets (and other protocols, like MQTT). 

Since its release in 2016, Channels has opened a new world of possibilities for Django developers, allowing them to build and deliver realtime features like chat, powered by WebSockets.

Django Channels consists of several packages:

  <li>Channels – the Django integration layer.</li>

  <li>Daphne – the HTTP and WebSocket termination server. Daphne supports automatic negotiation of protocols, and there’s no need for URL prefixing to determine WebSocket vs. HTTP endpoints. </li>

  <li>asgiref – a package that includes ASGI base libraries for sync-to-async and async-to-sync function wrappers, server base classes, and a WSGI-to-ASGI adapter. </li>

  <li>channels_redis – optional package providing a channel layer backend that uses Redis as a backing store. See the next section for more details about channels and channel layers.</li></p>
