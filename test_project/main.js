require('helpers.js');
require('Greeter.ts');


function main () {
    nice_print('This is the main file!');
    nice_print(add(2, 8));

    var greeter = new Greeter();

    nice_print(createDivWithH1());
    nice_print(greeter.greet());
};

main();
