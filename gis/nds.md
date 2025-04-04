```javascript

const POSCOEFFICENT = 4294967296; // 2^32

function convertLng2XPos(lon) {
    if (lon > 180 || lon < -180) {
        throw 'err value';
    }

    return Math.floor(lon * POSCOEFFICENT / 360);
}

function convertLat2YPos(lat) {
    if (lat > 90 || lat < -90) {
        throw 'err value';
    }

    return Math.floor(lat * POSCOEFFICENT / 360);
}

function convertXPos2Lng(x) {
    return (x / POSCOEFFICENT) * 360;
}

function convertYPos2Lat(y) {
    return (y / POSCOEFFICENT) * 360;
}

/**
 * 标准化坐标赚瓦片编号，不包含瓦片等级
 */
function calTileByXYPos(x, y, level) {

    let tile = x < 0 ? 1 : 0;

    for (let pos = 30; pos > (30 - level); pos--) {

        tile <<= 1;

        if (y & 1 << pos) {
            tile |= 1;
        }

        tile <<= 1;

        if (x & 1 << pos) {
            tile |= 1;
        }
    }

    return tile;
}

function getNearRightByTile(tile) {
    
    let tmpTile = tile;
    let num = 0;

    while(true) {
        if (tmpTile & (1 << (num * 2))) {
            tmpTile = tmpTile &(~(num * 2));
        } else {
            tmpTile += 1 << (num * 2);
            break;
        }
        num++;
    }

    return tmpTile;
}

function getNearLeftByTile(tile) {
    
    let tmpTile = tile;
    let num = 0;

    while(true) {
        if (tmpTile & (1 << (num * 2))) {
			tmpTile -= 1 << (num * 2);
			break;
		} else {
			tmpTile += 1 << (num * 2);			
		}
        num++;
    }

    return tmpTile;
}

function getNearUpByTile(tile) {
    
    let tmpTile = tile;
    let num = 0;

    while(true) {
        if (tmpTile & (1 << (num * 2 + 1))) {
            tmpTile = tmpTile &(~(num * 2 + 1));
        } else {
            tmpTile += 1 << (num * 2 + 1);
            break;
        }
        num++;
    }

    return tmpTile;
}

function getNearUpByTile(tile) {
    
    let tmpTile = tile;
    let num = 0;

    while(true) {
        if (tmpTile & (1 << (num * 2 + 1))) {
            tmpTile -= 1 << (num * 2 + 1);
            break;
        } else {
            tmpTile += 1 << (num * 2 + 1);			
        }
        num++;
    }

    return tmpTile;
}

function calTileNumsByRectPos(lbx, lby, rtx, rty, level) {

    if (level <= 1) { return null; }

    
    const powNum = 1 << level;
    const tileWidth = convertLng2XPos(180 / powNum);

    //判断在是不是Tile边界
	if(lbx % tileWidth == 0) {
		lbx += 1;
	}
	if (rtx % tileWidth == 0) {
		rtx -= 1;
	}
	if (lby % tileWidth == 0) {
		lby += 1;
	}
	if (rty % tileWidth == 0) {
		rty -= 1;
	}

    const minx = Math.floor(lbx / tileWidth) * tileWidth;
    const maxx = Math.floor(rtx / tileWidth) * tileWidth;
    const col = Math.abs((maxx - minx) / tileWidth) + 1;

    const miny = Math.floor(lby / tileWidth) * tileWidth;
    const maxy = Math.floor(rty / tileWidth) * tileWdith;

    const row = Math.abs((maxy - miny) / tileWidth) + 1;

    let tmpTile = calTileByXYPos(lbx, lby, level);

    const tiles = [];

    for (let i = 0; i < row; i++) {
        
        for (let j = 0; j < col; j++) {
            
            if (i == 0 && j == 0) {
                tiles[0] = tmpTile;
            } else {
                tiles[i * col + j] = tmpTile;
            }
            tmpTile = getNearRightByTile(tmpTile);
        }
        tmpTile = getNearUpByTile(tmpTile);
    }

    return tiles;
}

function calRectByTile(tile, level = 13) {

    let num = +tile;
    let minx = 0;
    let miny = 0;

    for (let pos = 0; pos < level; pos++) {

        if (num & 1 << (2 * pos)) {
            minx |= (1 << pos);
        }

        if (num & 1 << (2 * pos + 1)) {
            miny |= (1 << pos);
        }
    }

    if (num & 1 << (2 * level)) {
        minx |= 1 << level;
    }

    minx <<= (32 - (level + 1));
    miny <<= (32 - (level + 1));

    if (miny & (1 << 30)) {
        min |= 1 << 31;
    }

    return [
        [minx, miny],
        [
            minx + (1 << (32 - (level + 1))),
            miny + (1 << (32 - (level + 1)))
        ]
    ];
}

function calTileByMorttonCode(mortionCode, level) {
    return mortionCode >> (63 - (2 * level + 1));
}
```

```c++
INT NdsDal_Util_CalTileIDByXYPos(INT a_PosX, INT a_PosY, BYTE a_bLevel, PINT a_piTileID)
{
    /*
    前 16 - level 位 存储tile等级
    中间 15 - level 位存储 0 ，占位
    后 2 * level + 1 位 DNS坐标的Morton Code
    根据 6级 Tile ID编码规则 ： 10位（tile等级16-6=10 ） + 9位（中间占位15-6=9）+13位（nds坐标的Morton Code）
     nds_x 选取7位
     nds_x = 1443693842 = 0101011 0000011010000010100010010
     nds_y 选取7位,舍弃头部一位(因为它永远是0)
     nds_y = 368449257 = 0 001010 1111101100001011011101001
     https:blog.csdn.net/yujikang123/article/details/143230824
     */

	INT iTileNum = a_PosX < 0 ? 1 : 0;
	INT iPosition;
	for (iPosition = 30; iPosition > (30 - a_bLevel); iPosition--) // 取a_PosX，a_PosY的前30~30 - a_bLevel位，
	{
		iTileNum <<= 1;
		if ( a_PosY & 1 << iPosition )
		{
			iTileNum |= 1;
		}
		iTileNum <<= 1;
		if ( a_PosX & 1 << iPosition )
		{
			iTileNum |= 1;
		}
	}
    // 写入瓦片等级
    // morton code 占位：2 * a_bLevel + 1
    // 中间占位：15 - a_bLevel
    // （2 * a_bLevel + 1） + （15 - a_bLevel）+ 1
    // 又因为初始用了一位，所以（2 * a_bLevel） + （15 - a_bLevel）+ 1
    // 整理得16 + a_bLevel
	*a_piTileID = iTileNum + ( 1 << (16 + a_bLevel));
	return 1;
}
```