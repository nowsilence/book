WebGL deleteBuffer leaking memory?

It's never a good idea to repeatedly create and delete buffers in your animation loop, as it causes video memory fragmentation. Video memory isn't managed by powerful garbage collectors like in Java or .NET, since it would be in strong contrast to performance. What's freed with "deleteBuffer" might not actually be freed for new use until the complete GL context is deleted.

If you need to use a lot of dynamicly changing buffers, either use the gl.DYNAMIC_DRAW hint which will cause the driver to store the buffer in CPU memory and stream it to the GPU for each individual rendering (at a performance penalty of course) or keep re-using your buffers (over-provisioning its dimension might be advisable).

Many professional 3D engines ever only use one large vertex buffer object for all meshes, using bufferSubData and drawing commands with offsets.