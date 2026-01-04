/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() { 
    a=0;
    b=1;
    while(true) {
        yield a;
        s = a+b;
        a = b;
        b = s;
    }
};
