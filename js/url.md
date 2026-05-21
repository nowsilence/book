```javascript

/**
 * 字符串url参数转成key/value的形式
 * Parses a query string into an object, where the keys and values of the object are the
 * name/value pairs from the query string, decoded. If a name appears multiple times,
 * the value in the object will be an array of values.
 * @function queryToObject
 *
 * @param {String} queryString The query string.
 * @returns {Object} An object containing the parameters parsed from the query string.
 *
 *
 * @example
 * var obj = Cesium.queryToObject('key1=some%20value&key2=a%2Fb&key3=x&key3=y');
 * // obj will be:
 * // {
 * //   key1 : 'some value',
 * //   key2 : 'a/b',
 * //   key3 : ['x', 'y']
 * // }
 *
 * @see objectToQuery
 */
function queryToObject(queryString) {
  //>>includeStart('debug', pragmas.debug);
  if (!defined(queryString)) {
    throw new DeveloperError("queryString is required.");
  }
  //>>includeEnd('debug');

  var result = {};
  if (queryString === "") {
    return result;
  }
  // /\+/g：全局匹配所有+号替换成%20（URL 里的空格）
  // 原因：URL 会把空格编码成 +，所以要先还原成空格
  // &：普通 URL 参数分隔符 a=1&b=2
  // ;：也是合法的 URL 参数分隔符（部分后端用）
  // split(/[&;]/)  按 & 或 ; 分割字符串
  var parts = queryString.replace(/\+/g, "%20").split(/[&;]/);
  for (var i = 0, len = parts.length; i < len; ++i) {
    var subparts = parts[i].split("=");

    var name = decodeURIComponent(subparts[0]);
    var value = subparts[1];
    if (defined(value)) {
      value = decodeURIComponent(value);
    } else {
      value = "";
    }

    var resultValue = result[name];
    if (typeof resultValue === "string") {
      // expand the single value to an array
      result[name] = [resultValue, value];
    } else if (Array.isArray(resultValue)) {
      resultValue.push(value);
    } else {
      result[name] = value;
    }
  }
  return result;
}

```