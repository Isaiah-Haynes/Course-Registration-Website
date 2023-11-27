import { callExternalApi } from "./call-external-api";

//urls for calling api in final production stage
const apiCourseCatalogUrl = import.meta.env.VITE_COURSE_CATALOG_API_URL;
const apiStudentsUrl = import.meta.env.VITE_STUDENTS_API_URL;

//urls for testing beta stage api deployment stages 
const apiCourseCatalogUrlBeta = import.meta.env.VITE_COURSE_CATALOG_API_URL_BETA;
const apiStudentsUrlBeta = import.meta.env.VITE_STUDENTS_API_URL_BETA;

// ------------------------COURSE APIs------------------------------------


//searches courseCatalog for filter in course_name
export const searchMultipleCourseCatalog = async(filter) => {
    console.log("getCourseFromCourseCatalog()");
    
    //gets api url from .env and uses filter from StudentEnrollView.vue
    // const url = `${apiCourseCatalogUrlBeta}filterCourseCatalog?tableFilter=${filter}`;
    const url = `${apiCourseCatalogUrl}filterCourseCatalog?tableFilter=${filter}`;
    //adds required options for fetch to config
    const config = {
        method: "GET",
        headers: {
            "content-type": "application/json"
        }
    };

    // console.log(url);

    //assigns data, error to the returned variables from callExternalApi
    const { data, error } = await callExternalApi({ url, config });
    // console.log(data);

    //returns data, error to wherever function was called
    return {
        data: data || null,
        error,
    };
};

//function to call the api to delete a course from courseCatalog dynamoDB table
export const deleteCourseFromCourseCatalog = async(courseName) => {
    console.log("deleteCourseFromCourseCatalog()");
    
    //beta url for testing
    // const url = `${apiCourseCatalogUrlBeta}deleteCourseFromCourseCatalog?courseName=${courseName}`;
    //api invoke url
    const url = `${apiCourseCatalogUrl}deleteCourseFromCourseCatalog?courseName=${courseName}`;

    const config = {
        method: "GET",
        headers: {
            "content-type": "application/json"
        }
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};

//function to call the api to add a course to courseCatalog dynamoDB table
export const addCourseToCourseCatalog = async(courseParams) => {
    console.log("addCourseToCourseCatalog()");

    //api invoke url
    const url = `${apiCourseCatalogUrl}addCourseToCourseCatalog`;

    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            "course_name": courseParams.courseName,
            "num_credits": courseParams.numCredits,
            "course_title": courseParams.courseTitle,
            "course_start": courseParams.courseStart,
            "course_end": courseParams.courseEnd,
            "course_days": courseParams.courseDays,
            "subject": courseParams.subject,
            "professor": courseParams.professor,
            "max_enrollment": courseParams.maxEnrollment,
            "current_enrollment": courseParams.currentEnrollment
        })
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};


// ------------------------STUDENT APIs------------------------------------

//function that calls api to add a student given parameters
export const addStudent = async(studentParams) => {
    console.log("addStudent()");

    //api invoke url
    const url = `${apiStudentsUrl}addStudent`;

    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            "id": studentParams.id,
            "name": studentParams.name,
            "major": studentParams.major || "N/A",
            "minor": studentParams.minor || "N/A",
            "standing": studentParams.standing,
            "gpa": studentParams.gpa,
            "total_credits": studentParams.total_credits,
            "enrolled_credits": studentParams.enrolled_credits,
            "enrolled_courses": studentParams.enrolled_courses,
            "past_courses": studentParams.past_courses
        })
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};

//function that calls api to delete a student given student id
export const deleteStudent = async(studentID) => {
    console.log("deleteStudent()");

    //api invoke url
    const url = `${apiStudentsUrl}deleteStudent?id=${studentID}`;

    const config = {
        method: "GET",
        headers: {
            "content-type": "application/json"
        }
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};

//function that enrolls student in a course
export const enrollStudent = async(params) => {
    console.log("enrollStudent()");

    const url = `${apiStudentsUrl}enrollStudent?id=${params.studentID}&course=${params.course}`;

    const config = {
        method: "GET",
        headers: {
            "content-type": "application/json"
        }
    };
    
    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};