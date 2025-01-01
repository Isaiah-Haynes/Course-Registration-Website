# Course Registration Website

website accessible from http://crs-lab002group6.s3-website-us-east-1.amazonaws.com/
Since this is a development website, you will need to add the above URL to the "treat insecure origins as secure" option in chrome://flags

Please utilize google chrome to access the website, or do some research on how to do the above in your preferred browser.


## Runing Locally

Running this website locally is not recommended, but instructions to setup your environment can be found below.

### Nodejs

Install Nodejs from [their website](https://nodejs.org/en)

### Project Setup

Whenever you clone this project, or change the contents of `package.json`, be sure to run the following command in your terminal:

```sh
npm install
```

### Compile and Hot-Reload for Development

Whenever you want to run the local development server, which will allow you to view the application in your browser, run this command in your terminal:

```sh
npm run dev
```

### Compile and Minify for Production

Whenever you want to create the files that you would serve in a production environment (like Amazon S3), run this command in your terminal:

```sh
npm run build
```
