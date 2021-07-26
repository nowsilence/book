The WebGL API supports the following additional parameters to pixelStorei.

UNPACK_FLIP_Y_WEBGL of type boolean
If set, then during any subsequent calls to texImage2D or texSubImage2D, the source data is flipped along the vertical axis, so that conceptually the last row is the first one transferred. The initial value is false. Any non-zero value is interpreted as true.
UNPACK_PREMULTIPLY_ALPHA_WEBGL of type boolean
If set, then during any subsequent calls to texImage2D or texSubImage2D, the alpha channel of the source data, if present, is multiplied into the color channels during the data transfer. The initial value is false. Any non-zero value is interpreted as true.
UNPACK_COLORSPACE_CONVERSION_WEBGL of type unsigned long
If set to BROWSER_DEFAULT_WEBGL, then the browser's default colorspace conversion is applied during subsequent texImage2D and texSubImage2D calls taking HTMLImageElement. The precise conversions may be specific to both the browser and file type. If set to NONE, no colorspace conversion is applied. The initial value is BROWSER_DEFAULT_WEBGL.
If the TexImageSource is an ImageBitmap, then these three parameters will be ignored. Instead the equivalent ImageBitmapOptions should be used to create an ImageBitmap with the desired format.