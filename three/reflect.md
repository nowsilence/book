
```js
import * as THREE from 'three';
import { Reflector } from 'three/addons/objects/Reflector.js';

// 镜面平面
const geo = new THREE.PlaneGeometry(20, 20);
const mirror = new Reflector(geo, {
  textureWidth: window.innerWidth * window.devicePixelRatio,
  textureHeight: window.innerHeight * window.devicePixelRatio,
  clipBias: 0.003, // 裁剪偏移，解决反射面的 z-fighting 闪烁，常用 `0.003`, 镜面和裁剪面位置完全相同，会有z值冲突， 正值：把裁剪面往虚拟相机方向偏移一段距离，- 推荐：`0.001 ~ 0.01`- 最常用：`0.003`
  color: 0x889999
});
mirror.rotation.x = -Math.PI / 2; // 放平作为地面
scene.add(mirror);
```

MeshReflectorMaterial，支持模糊 + 距离衰减
```js
import * as THREE from 'three'
import { MeshReflectorMaterial } from '@pmndrs/drei'

// 地面平面
const groundGeo = new THREE.PlaneGeometry(30,30)
const groundMat = new MeshReflectorMaterial({
  resolution: 1024,        // RTT纹理分辨率，类似Reflector的textureWidth
  blur: [200, 200],        // 模糊 [水平,垂直]，0=镜面清晰，越大越磨砂
  mixBlur: 1,              // 模糊和表面roughness混合强度
  mixStrength: 1,          // 反射整体强度 0~1
  mirror: 1,               // 反射强度，0=不反射，1=完全镜面
  mixContrast: 1,          // 反射图对比度
  reflectorOffset: 0.001,  // 等价于原生Reflector的clipBias！解决z-fighting闪烁
  // 深度衰减：远处反射慢慢消失（地面常用）
  depthScale: 1.2,
  minDepthThreshold: 0.8,
  maxDepthThreshold: 1.2,
  depthToBlurRatioBias: 0.25,
  // 继承MeshStandardMaterial所有参数
  color: '#333333',
  metalness: 0,
  roughness: 0.2
})
const ground = new THREE.Mesh(groundGeo, groundMat)
ground.rotation.x = -Math.PI / 2
scene.add(ground)
```