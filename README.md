![sot.png](sot.png)

# Stack Of Transpilers
> All your transpilers, at one place, for _any_ type of source code.

## What is a transpiler?
> A source-to-source compiler, transcompiler or transpiler is a type of
> compiler that takes the source code of a program written
> in one programming language as its input and produces the equivalent
> source code in another programming language.  

> For more, look at [this](https://en.wikipedia.org/wiki/Source-to-source_compiler)

## Using SOT
> Some use cases for `SOT` are:

* transpiling Javascript
* transpiling templates
* transpiling markup
* transpiling configuration files
* transpile __anything__!

> With `SOT` you can write your own micro transpilers _(or use existing ones)_
> and use them in your projects,
> no matter what language you are programming in.

### Using SOT in your project
> To use `SOT` in your project, you will need a `sot.json`
> file in your project.  
> Below is an example of when being used in a javascript project:

    {
        "main": "main.js",
        "out": "bundle.js",
        "transpilers": [
            {
                "path": "./bin/require.js"
            },
            {
                "path": "./bin/js_minifier.py"
            }
        ]
    }

> So here we are telling `SOT` that the program starts in `main.js` and
> we want the transpiled version of our program to be in `bundle.js`.

> We are also telling `SOT` to use two transpilers, we can point the `path`
> variable to any binary that we want. In our case I am pointing the first one
> to `./bin/require.js` which is a transpiler that lets us use
> `require(<filename>)` in our javascript project.  
> The other is pointing to `./bin/js_minifier.py` which simply minifies
> the code.

> The order of the transpilers in the `transpilers` section in the `sot.json`
> file is important, we would not want to _minify_ before we have _require_
> implemented for example, therefore the order above.

#### Starting the SOT watchdog
> Once you have the `sot.json` file in your project, you can start the `SOT`
> watchdog by running:

    $ sot .

> while standing in your project.  
> This will write the `bundle` file that we specified above whenever a file
> changes.

# Important note
> `SOT` __can__ be used in __any__ project! It does not matter what
> language you are programming in.

> The transpiler binaries can be written in any language as well,
> they do not even have to be programmed in the same language as your project.
