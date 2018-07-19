function nice_print(out) {
    console.log('*** ' + out + ' ***');
}

function noop() {};

function createDivWithH1 () {
    return HTML`
        <div>
            <h1>THIS IS A DIV WITH H1</h1>
        </div>
    `;
};
