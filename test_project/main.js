require('helpers.js');

// main method
function main () {
    nice_print('This is the main file!');
    nice_print(add(2, 8));

    var x = createDivWithH1();

    console.log(x);
};

main();
