# Course Registration Website

website accessible from http://crs-lab002group6.s3-website-us-east-1.amazonaws.com/
Since this is a development website, you will need to add the above URL to the "treat insecure origins as secure" option in chrome://flags

Please utilize google chrome to access the website, or do some research on how to do the above in your preferred browser.

## Login Page
![Screenshot 2024-12-31 at 7 56 33 PM](https://github.com/user-attachments/assets/0634ce57-b139-4294-85be-c951c531ba61)

![Screenshot 2024-12-31 at 8 04 29 PM](https://github.com/user-attachments/assets/c6b5d755-5c65-4d65-8146-a314c2e34f8d)

## Student Search and Enrollment
![Screenshot 2024-12-31 at 7 57 36 PM](https://github.com/user-attachments/assets/36f51784-07d4-4d88-a124-d41ac3a0dfae)

## Student Schedule View
![Screenshot 2024-12-31 at 7 58 13 PM](https://github.com/user-attachments/assets/1599a9b2-f6d4-4af4-b508-b4ba5acac467)

## Professor Schedule View
![Screenshot 2024-12-31 at 7 58 44 PM](https://github.com/user-attachments/assets/f92ad62d-2e74-4054-8983-bf16f7228088)

## Admin Views
![Screenshot 2024-12-31 at 8 01 11 PM](https://github.com/user-attachments/assets/06d1cb44-b446-4e6d-b080-2aad7f781c89)
![Screenshot 2024-12-31 at 8 00 14 PM](https://github.com/user-attachments/assets/5a7dd5a9-cf6a-4c25-a3f8-8843909cc22b)
![Screenshot 2024-12-31 at 8 00 22 PM](https://github.com/user-attachments/assets/dec042cb-b79f-48f5-98d5-c4939ba09bd6)

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

### Replace example values with your own

Some files will not run properly until the proper values are added. This is why it is not recommended that you run this website locally. In an attempt to achieve some sence of security, values such as API keys, URLs, and other sensitive information are not publicly acessible in this repo and will need to be replaced with your own values or contact the owner of this repo to gain access to the values used for the pictures above (coming soon). The files with missing values are listed below:

`.env`
All python files in `src/amazonServices/dynamoDB/` (replace `AWS_REGION` with your AWS region)
