31

To help you understand the maths (not a precise calculation, it's just for illustration):

Google's web map tile has 256 pixels of width
let's say your computer monitor has 100 pixels per inch (PPI). That means 256 pixels are roughly 6.5 cm of length. And that's 0.065 m.

on zoom level 0, the whole 360 degrees of longitude are visible in a single tile. You cannot observe this in Google Maps since it automatically moves to the zoom level 1, but you can see it on OpenStreetMap's map (it uses the same tiling scheme).

360 degress on the Equator are equal to Earth's circumference, 40,075.16 km, which is 40075160 m

divide 40075160 m with 0.065 m and you'll get 616313361, which is a scale of zoom level 0 on the Equator for a computer monitor with 100 DPI

so the point is that the scale depends on your monitor's PPI and on the latitude (because of the Mercator projection)
for zoom level 1, the scale is one half of that of zoom level 0
...
for zoom level N, the scale is one half of that of zoom level N-1
Also check out:

[参考](https://gis.stackexchange.com/questions/7430/what-ratio-scales-do-google-maps-zoom-levels-correspond-to)