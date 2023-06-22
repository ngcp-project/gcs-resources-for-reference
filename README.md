<h1 align="center">GCS Resources for References</h1>

Here is the list of resources that I have collected that would be useful to get yourself familiar with the technologies that we will be using for this year's cycle of NGCP. This document will be further updated in the future should any new development arises. 

Feel free to make commits to this README or add new Markdown documents to add more helpful resources!
<h2 align="center">Table of Contents</h2>

- [Getting Started](#getting-started)
  - [Version Control](#version-control)
- [User Interface](#user-interface)
  - [Tauri](#tauri)
  - [Vue.js](#vuejs)
  - [NASA Web WorldWind](#nasa-web-worldwind)
- [Database](#database)
  - [C#](#c)
  - [ASP.NET Core](#aspnet-core)
  - [Redis](#redis)
- [Vehicle Integration](#vehicle-integration)
  - [Python](#python)
  - [FastAPI](#fastapi)
- [Communications](#communications)
  - [WebSockets](#websockets)
  - [WebRTC \& Video Streaming](#webrtc--video-streaming)
  - [Local Area Network](#local-area-network)


# Getting Started
## Version Control
* [GitHub Pull Requests in 100 Seconds](https://www.youtube.com/watch?v=8lGpZkjnkt4) `video`
* [Using Git in VS Code](https://www.youtube.com/watch?v=lYiE5lBS13E) `video`
* [An Intro to Git and GitHub for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) `blog`
* [Git Commands Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) `PDF`

---
# User Interface
## [Tauri](https://tauri.app)
* [Tauri in 100 Seconds](https://www.youtube.com/watch?v=-X8evddpu7M) `video`
* [Create Tauri app with Vite](https://tauri.app/v1/guides/getting-started/setup/vite/) `documentation`
* [Create Tiny Desktop Apps with Tauri and Vue.js](https://www.smashingmagazine.com/2020/07/tiny-desktop-apps-tauri-vuejs/) `blog` `tutorial` 

## [Vue.js](https://vuejs.org/guide/introduction.html)
* [Vue.js in 100 Seconds](https://www.youtube.com/watch?v=nhBVL41-_Cw) `video`
* [Using Vue with TypeScript](https://vuejs.org/guide/typescript/overview.html) `documentation`
* [Vue.js WebSocket Tutorial](https://tutorialedge.net/javascript/vuejs/vuejs-websocket-tutorial/) `tutorial`
* [Vue.js Examples](https://vuejsexamples.com/) `examples` `source-code`
  * [Maps](https://vuejsexamples.com/tag/maps/)
  * [WebRTC](https://vuejsexamples.com/tag/webrtc/)
  * [WebSocket](https://vuejsexamples.com/tag/websocket/)

## [NASA Web WorldWind](https://worldwind.arc.nasa.gov/web/)
* [Quickstart Guide](https://worldwind.arc.nasa.gov/web/get-started/#anchor) `documentation` `tutorial`
* [Hosting Web WorldWind Locally](https://worldwind.arc.nasa.gov/web/tutorials/offline-example/) `documentation`
* [How to setup a NASA WorldWind imagery server](https://gist.github.com/emxsys/f8c7a8dd5cf0060387ce50aa3f186bac) `github` 

---
# Database
## C#
* [C# for Python Programmers](https://gist.github.com/mrkline/8302959) `github`
* [C# for Java Developers](https://download.microsoft.com/download/D/E/E/DEE91FC0-7AA9-4F6E-9FFA-8658AA0FA080/CSharp%20for%20Java%20Developers%20-%20Cheat%20Sheet.pdf) `PDF`

## [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-7.0)
* [Using .NET in Visual Studio Code](https://code.visualstudio.com/docs/languages/dotnet) `documentation`
* [Create a web API with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-7.0&tabs=visual-studio)  `documentation` `tutorial`
* [Build minimal APIs in .NET 7 using Entity Framework Core 7](https://www.c-sharpcorner.com/article/build-minimal-apis-in-net-7-using-entity-framework-core-7/) `blog` `tutorial`
* [WebSockets support in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets?view=aspnetcore-7.0) `documentation`

## [Redis](https://redis.io/docs/)
* [Getting Started with Redis](https://redis.io/docs/getting-started/)
* [StackExchange.Redis](https://stackexchange.github.io/StackExchange.Redis/) `documentation`
* [joeferner/redis-commander](https://github.com/joeferner/redis-commander) `github`
  * UI-based Redis management tool written in Node.js
* [Messaging App using .NET Core, Redis and WebSockets](https://bercovici-adrian-simon.medium.com/ctesiphon-chat-application-using-net-redis-pub-sub-and-websockets-bd12b8032f8b) `medium` `tutorial`
* [Basic Redis Chat App Demo C# (.NET Core 5)](https://github.com/redis-developer/basic-redis-chat-app-demo-dotnet) `github` `tutorial`

---
# Vehicle Integration
## Python
* [Write Robust Python with Static Typing](https://towardsdatascience.com/data-science-write-robust-python-with-static-typing-c71b9c9c8044) `tutorial` `article`
* [@dataclass](https://docs.python.org/3/library/dataclasses.html) `documentation`

## [FastAPI](https://fastapi.tiangolo.com)
* [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) `documentation`
* [Testing WebSockets](https://fastapi.tiangolo.com/advanced/testing-websockets/?h=websocket) `documentation`
* [How to Use WebSockets with FastAPI](https://medium.com/vacatronics/how-to-use-websocket-with-fastapi-8460db1c074) `medium` `tutorial`
* [Streaming Video with FastAPI](https://stribny.name/blog/fastapi-video/) `tutorial` 
* [MattWeinberg24/pi-stream](https://github.com/MattWeinberg24/pi-stream) `github`
  * Raspberry Pi/FastAPI service for streaming HDMI video/audio over the internet using the WebRTC protocol
* [stribny/fastapi-video](https://github.com/stribny/fastapi-video) `github`
  * Video streaming example with FastAPI

---
# Communications
## WebSockets
* [WebSocket in 100 Seconds](https://www.youtube.com/watch?v=1BfCnjr_Vjg)

## WebRTC & Video Streaming
* [WebRTC on Raspberry Pi: Live HD Video and Audio Streaming](https://www.highvoltagecode.com/post/webrtc-on-raspberry-pi-live-hd-video-and-audio-streaming) `article` `tutorial`
* [How To Stream Live Video From Your Raspberry Pi Camera](https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi) `tutorial`
* [Using Jetson Nano and a Raspberry Pi Camera for Video Streaming](https://maker.pro/nvidia-jetson/tutorial/streaming-real-time-video-from-rpi-camera-to-browser-on-jetson-nano-with-flask) `tutorial`

## Local Area Network
* [How to Set Static IP Address](https://www.trendnet.com/press/resource-library/how-to-set-static-ip-address) `tutorial`
* [DHCP IP reservation or Set a Static IP address for a device](https://support.google.com/googlenest/answer/6274660?hl=en) `google` `blog`