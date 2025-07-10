import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';
import json from 'rollup-plugin-json';
import pkg from './package.json';

export default [
  // browser-friendly UMD build
  {
    input: 'src/bg/background.js',
    output: {
      name: 'background',
      file: pkg.browser,
      format: 'umd',
      globals: {url: 'url'}
    },
    plugins: [
      resolve({preferBuiltins: true}), // so Rollup can find `ms`
      commonjs(), // so Rollup can convert `ms` to an ES module
      json({
        // All JSON files will be parsed by default,
        // but you can also specifically include/exclude files
        include: 'node_modules/**',

        // for tree-shaking, properties will be declared as
        // variables, using either `var` or `const`
        preferConst: true, // Default: false

        // specify indentation for the generated default export —
        // defaults to '\t'
        indent: '  ',

        // ignores indent and generates the smallest code
        compact: true, // Default: false

        // generate a named export for every property of the JSON object
        namedExports: true // Default: true
      })
    ]
  }
];
