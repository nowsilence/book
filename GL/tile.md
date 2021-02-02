const distance; // 点到相机距离
const resolution0; // 0级瓦片分辨率

const resolution = (2.0 * Math.tan(camera.fov / 2.0) * distance) / screen[1];  // 米/像素
const twoToTheLevelPower = resolution0 / resolution;
const level = Math.round(Math.log2(twoToTheLevelPower))
// const level = Math.log(twoToTheLevelPower) / Math.log(2);
