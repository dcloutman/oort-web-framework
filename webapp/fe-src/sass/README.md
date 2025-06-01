# Sass for Site-Wide Styles

Sass is a tool for abstracting CSS. It allows front-end developers to create reusable code that includes variables, mixins, etc. The version of Sass that Oort uses is written in Dart and is the newer version of Sass.

## Installation

Before using the Sass tool for the first time, you will need to install the Sass library. We assume you already have npm up and running on your maching. To install Sass, execute the following command:

```
npm install
```

`npm` should run and pull in a bunch of libraries.

## Usage

The file `main.scss` is a Sass file. It is intended that it should transpile and be written to the target file, `/static/css/main.css`. The following command will start the tranpilation:

```
npm run sass-build
```

Do not edit the target file directly as subsequent transpilations will overwrite such changes. Only write to .scss files in this directory.
