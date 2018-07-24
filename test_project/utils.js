// just a print method
function nice_print(stdout) {
    console.log('*** ' + stdout + ' ***');
}

function createDivWithH1() {
    return HTML`
        <div>
            <h1>Hello World</h1>
        </div>
    `;
};
