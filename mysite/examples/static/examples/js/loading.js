/**
 * R:大圆半径，2*R = 外部正方形的边长
 * r:在大圆边上等距排列的小圆的半径
 * counts: 圆的数量
 * 返回值：
 *  [
 *    [x1,y1],
 *    [x2,y2],
 *    ...
 *  ]
 */
function calcXYs(R, r, counts) {
  // 当前度数
  let deg = 0;
  // 单位度数，两小圆和圆心的夹角
  const pDeg = 360 / counts;
  // 存放返回结果
  const arr = [];
  for (let i = 0; i < counts; i++) {
    // 度数以单位度数递增
    deg = pDeg * i;
    // Math.sin接收的参数是弧度制
    const proportion = Math.PI / 180;
    // 以外部DIV左下角为原点，计算小圆圆心的横纵坐标
    let Y = R + R * Math.sin(proportion * deg);
    let X = R + R * Math.cos(proportion * deg);
    // 存放结果
    arr.push([X, Y, deg]);
  }
  return arr;
}
/**
 * R，r，counts：含义同上
 * selector: 获取所有小圆的标志符
 * 作用：根据上一步的坐标计算结果，调整绝对定位的小圆的位置
 */
function resizeCircles(selector, R, r, counts) {
  // 获取所有小圆NodeList的选择器
  let list = document.querySelectorAll(selector);
  //调用calcXYs方法
  const XYs = calcXYs(R, r, counts);
  // 遍历每个小圆的XY坐标
  for (let i = 0; i < list.length; i++) {
    const [X, Y] = XYs[i];
    const e = list[i];
    // 修改小圆距离外部DIV底部和左边的距离
    e.style.left = X + "px";
    e.style.bottom = Y + "px";
  }
}
resizeCircles(".circle", 60, 20, 8);