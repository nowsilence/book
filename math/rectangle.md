```javascript
function isOverlap(rect0, rect1) {
    const west = Math.max(rect0.west, rect1.west);
    const south = Math.max(rect0.south, rect1.south);
    const east = Math.min(rect0.east, rect1.east);
    const north = Math.min(rect0.north, rect1.north);
    
    return south < north && west < east;
}
```