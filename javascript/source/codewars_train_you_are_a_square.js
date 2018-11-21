var isSquare = function(n){
  var sqrtN = Math.sqrt(n);
  var intSqrtN = Math.round(sqrtN);
  var isSqrt = intSqrtN * intSqrtN === n;

  return isSqrt;
}

console.log("-1 is perf square?", isSquare(-1));
console.log("1 is perf square?", isSquare(1));
console.log("4 is perf square?", isSquare(4));
console.log("25 is perf square?", isSquare(25));
console.log("26 is perf square?", isSquare(26));
