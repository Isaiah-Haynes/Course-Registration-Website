# Course Registration Website

## DISCLAIMER!!
This website is no longer publicly available as the AWS backend services have been deleted.

## Description
This repository is for a simple course registration website with a backend hosted on AWS (Amazon Web Services) and a frontend built with vue.js framework. The website is designed to have three groups of users: students, professors, and administrators. Each group has an option to log in to thier respective site to perform a variety of options. Students have the ability to search for and enroll in classes, as well as view their schedule of enrolled courses. From the schedule view, students can also unenroll from the course of their choosing.
The professor page simply has the option for a professor to view the schedule of classes that they are teaching.
Finally, the administrator's page has the ability to add, edit, and remove students, professors, and classes. Images showing the main functions of each use case are shown below.

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

In order to establish some sense of security, some files have dummy values. The files with missing values are listed below:

`.env`

All python files in `src/amazonServices/dynamoDB/`
