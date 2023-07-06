<div align='center'>

# GCS Resources for References
</div>

Here is the list of resources that I have collected that would be useful to get yourself familiar with the technologies that we will be using for this year's cycle of NGCP. This document will be further updated in the future should any new development arises. 

Feel free to make commits to this README or add new Markdown documents to add more helpful resources!

<h2 align='center'>Table of Contents</h2>


- [GCS Resources for References](#gcs-resources-for-references)
- [Getting Started](#getting-started)
  - [Version Control](#version-control)
  - [Style Guides](#style-guides)
  - [Docker \& Environment Standardization](#docker--environment-standardization)
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
* [Common Conventions for Writing Commit Titles](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) `docs` `article`

## Style Guides
* [Vue.js Style Guide](https://v2.vuejs.org/v2/style-guide/?redirect=true) `docs` `official`
* [C# at Google Style Guide](https://google.github.io/styleguide/csharp-style.html) `docs` `google`
* [Python Google Style Guide](https://google.github.io/styleguide/pyguide.html) `docs` `google`
* [TypeScript at Google Style Guide](https://google.github.io/styleguide/tsguide.html) `docs` `google`

## Docker & Environment Standardization
* [Never install locally again (An Introduction to Docker & containers)](https://youtu.be/J0NuOlA2xDc) `video` *`recommended`*
* [Learn Docker in 1 Hour - Tutorial for Beginners](https://youtu.be/pTFZFxd4hOI) `video` `tutorial`
* [Running and Building ARM Docker Containers on x86](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/) `tutorial` `vehicle-integration`

---
# User Interface
## [Tauri](https://tauri.app)
* [Tauri in 100 Seconds](https://www.youtube.com/watch?v=-X8evddpu7M) `video`
* [Create Tauri app with Vite](https://tauri.app/v1/guides/getting-started/setup/vite/) `docs`
* [Create Tiny Desktop Apps with Tauri and Vue.js](https://www.smashingmagazine.com/2020/07/tiny-desktop-apps-tauri-vuejs/) `blog` `tutorial` 

## [Vue.js](https://vuejs.org/guide/introduction.html)
[**Last year's Vue.js codebase**](https://github.com/NGCP-GCS-22-23/Front-End) (archived, meant for reference only)
* [Vue.js in 100 Seconds](https://www.youtube.com/watch?v=nhBVL41-_Cw) `video`
* [Using Vue with TypeScript](https://vuejs.org/guide/typescript/overview.html) `docs`
* [Vue.js WebSocket Tutorial](https://tutorialedge.net/javascript/vuejs/vuejs-websocket-tutorial/) `tutorial`
* [Vue.js Examples](https://vuejsexamples.com/) `examples` `source-code`
  * [Maps](https://vuejsexamples.com/tag/maps/)
  * [WebRTC](https://vuejsexamples.com/tag/webrtc/)
  * [WebSocket](https://vuejsexamples.com/tag/websocket/)

## [NASA Web WorldWind](https://worldwind.arc.nasa.gov/web/)
* [Quickstart Guide](https://worldwind.arc.nasa.gov/web/get-started/#anchor) `docs` `tutorial`
* [Hosting Web WorldWind Locally](https://worldwind.arc.nasa.gov/web/tutorials/offline-example/) `docs`
* [How to setup a NASA WorldWind imagery server](https://gist.github.com/emxsys/f8c7a8dd5cf0060387ce50aa3f186bac) `github` 

---
# Database
## C#
* [Working with C# in VS Code](https://code.visualstudio.com/docs/languages/csharp) `vs-code` `docs`
* [Getting Started with C# in VS Code](https://code.visualstudio.com/docs/csharp/get-started) `vs-code` `tutorial` `docs` 
* [C# for Python Programmers](https://gist.github.com/mrkline/8302959) `github`
* [C# for Java Developers](https://download.microsoft.com/download/D/E/E/DEE91FC0-7AA9-4F6E-9FFA-8658AA0FA080/CSharp%20for%20Java%20Developers%20-%20Cheat%20Sheet.pdf) `PDF`

## [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-7.0)
* [Download .NET 7](https://dotnet.microsoft.com/en-us/download) `download`
* [Using .NET in Visual Studio Code](https://code.visualstudio.com/docs/languages/dotnet) `docs`
* [Create a web API with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-7.0&tabs=visual-studio)  `docs` `tutorial`
* [Build minimal APIs in .NET 7 using Entity Framework Core 7](https://www.c-sharpcorner.com/article/build-minimal-apis-in-net-7-using-entity-framework-core-7/) `blog` `tutorial`
* [WebSockets support in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets?view=aspnetcore-7.0) `docs`
* [ASP.NET Core Web API Best Practices](https://code-maze.com/aspnetcore-webapi-best-practices/) `article` `tutorial`
* [.NET Basics: Data Transfer Objects (DTOs)](https://www.telerik.com/blogs/dotnet-basics-dto-data-transfer-object#:~:text=What%20Is%20a%20DTO%3F,in%20itself%20any%20business%20logic.)

## [Redis](https://redis.io/docs/)
* [Getting Started with Redis](https://redis.io/docs/getting-started/)
* [StackExchange.Redis](https://stackexchange.github.io/StackExchange.Redis/) `docs`
* [joeferner/redis-commander](https://github.com/joeferner/redis-commander) `github`
  * UI-based Redis management tool written in Node.js
* [Messaging App using .NET Core, Redis and WebSockets](https://bercovici-adrian-simon.medium.com/ctesiphon-chat-application-using-net-redis-pub-sub-and-websockets-bd12b8032f8b) `medium` `tutorial`
* [Basic Redis Chat App Demo C# (.NET Core 5)](https://github.com/redis-developer/basic-redis-chat-app-demo-dotnet) `github` `tutorial`

---
# Vehicle Integration
## Python
* [Write Robust Python with Static Typing](https://towardsdatascience.com/data-science-write-robust-python-with-static-typing-c71b9c9c8044) `tutorial` `article`
* [@dataclass](https://docs.python.org/3/library/dataclasses.html) `docs`
* [WebSocket Client Library](https://websockets.readthedocs.io/en/stable/) `library` `docs`

## [FastAPI](https://fastapi.tiangolo.com)
* [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) `docs`
* [Testing WebSockets](https://fastapi.tiangolo.com/advanced/testing-websockets/?h=websocket) `docs`
* [How to Use WebSockets with FastAPI](https://medium.com/vacatronics/how-to-use-websocket-with-fastapi-8460db1c074) `medium` `tutorial`
* [Streaming Video with FastAPI](https://stribny.name/blog/fastapi-video/) `tutorial` 
* [MattWeinberg24/pi-stream](https://github.com/MattWeinberg24/pi-stream) `github`
  * Raspberry Pi/FastAPI service for streaming HDMI video/audio over the internet using the WebRTC protocol
* [stribny/fastapi-video](https://github.com/stribny/fastapi-video) `github`
  * Video streaming example with FastAPI

---
# Communications
## WebSockets
* [WebSocket in 100 Seconds](https://www.youtube.com/watch?v=1BfCnjr_Vjg) `video`
* [Writing WebSocket client applications](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications) `docs` `mozilla`
* [Node.js WebSocket Client: 3 Ways to Implement One](https://stateful.com/blog/nodejs-websocket-client) `blog`

## WebRTC & Video Streaming
* [WebRTC on Raspberry Pi: Live HD Video and Audio Streaming](https://www.highvoltagecode.com/post/webrtc-on-raspberry-pi-live-hd-video-and-audio-streaming) `article` `tutorial`
* [How To Stream Live Video From Your Raspberry Pi Camera](https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi) `tutorial`
* [Using Jetson Nano and a Raspberry Pi Camera for Video Streaming](https://maker.pro/nvidia-jetson/tutorial/streaming-real-time-video-from-rpi-camera-to-browser-on-jetson-nano-with-flask) `tutorial`

## Local Area Network
* [How to Set Static IP Address](https://www.trendnet.com/press/resource-library/how-to-set-static-ip-address) `tutorial`
* [DHCP IP reservation or Set a Static IP address for a device](https://support.google.com/googlenest/answer/6274660?hl=en) `google` `blog`