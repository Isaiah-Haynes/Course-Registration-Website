import { callExternalApi } from "./call-external-api";

//urls for calling api in final production stage
const apiUrl = import.meta.env.VITE_API_URL;

//export const getProtectedResource = async () => {
    export const getProtectedResource = async (accessToken) => {  //STEP2

        console.log("getProtectedResource()");
        const url = `${apiUrl}Authentication`
        const config = {
          method: "GET",
          headers: {
            "content-type": "application/json",
            "Authorization": `Bearer ${accessToken}`,  //STEP2
          },
        };
      
        const { data, error } = await callExternalApi({ url, config });
        // console.log(data);
        // console.log(error);
      
        return {
          data: data || null,
          error,
        };
      };


// ------------------------COURSE APIs------------------------------------

// READ
//searches courseCatalog for filter in course_name
export const searchMultipleCourseCatalog = async(filter) => {
    console.log("getCourseFromCourseCatalog()");
    
    //gets api url from .env and uses filter from StudentEnrollView.vue
    // const url = `${apiCourseCatalogUrlBeta}filterCourseCatalog?tableFilter=${filter}`;
    const url = `${apiUrl}courses/filterCourseCatalog?tableFilter=${filter}`;
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

// DELETE
//function to call the api to delete a course from courseCatalog dynamoDB table
export const deleteCourseFromCourseCatalog = async(courseName) => {
    console.log("deleteCourseFromCourseCatalog()");
    
    //beta url for testing
    // const url = `${apiCourseCatalogUrlBeta}deleteCourseFromCourseCatalog?courseName=${courseName}`;
    //api invoke url
    const url = `${apiUrl}courses/deleteCourse?courseName=${courseName}`;

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

// CREATE
//function to call the api to add a course to courseCatalog dynamoDB table
export const addCourseToCourseCatalog = async(courseParams) => {
    console.log("addCourseToCourseCatalog()");

    //api invoke url
    const url = `${apiUrl}courses/addCourse`;

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

// UPDATE
// function that edits a course
export const editCourse = async(courseParams) => {
    console.log("editCourse");

    const url = `${apiUrl}courses/editCourse`;

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
    
    const { data, erro } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};

// ------------------------STUDENT APIs------------------------------------

// CREATE
//function that calls api to add a student given parameters
export const addStudent = async(studentParams) => {
    console.log("addStudent()");

    //api invoke url
    const url = `${apiUrl}students/addStudent`;

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

// DELETE
//function that calls api to delete a student given student id
export const deleteStudent = async(studentID) => {
    console.log("deleteStudent()");

    //api invoke url
    const url = `${apiUrl}students/deleteStudent?id=${studentID}`;

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

// READ
//function that calls api to get student info given student id
export const getStudentInfo = async(studentID) => {
    console.log("getStudentInfo()");
    
    //api invoke url
    const url = `${apiUrl}students/getStudentInfo?id=${studentID}`;

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

// misc.
//function that enrolls student in a course
export const enrollStudent = async(params) => {
    console.log("enrollStudent()");

    const url = `${apiUrl}students/enrollStudent?id=${params.studentID}&course=${params.course}`;

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

// misc.
//function that unenrolls student from a course
export const unenrollStudent = async(params) => {
    console.log("unenrollStudent()");

    const url = `${apiUrl}students/unenrollStudentFromCourse?id=${params.studentID}&course=${params.course}`;

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

// UPDATE
// function that updates a student, cannot update student name
export const editStudent = async(studentParams) => {
    console.log("editStudent()");

    const url = `${apiUrl}students/editStudent?id=${studentParams.id}`;

    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            "major": studentParams.major,
            "minor": studentParams.minor,
            "standing": studentParams.standing,
            "gpa": studentParams.gpa,
            "total_credits": studentParams.total_credits,
            "enrolled_credits": studentParams.enrolled_credits,
            "enrolled_courses": studentParams.enrolled_courses,
            "past_courses": studentParams.past_courses
        })
    };

    const { data, error } = await callExternalApi({ url, config });
    // console.log(config);
    return {
        data: data || null,
        error,
    };
};

// ------------------------PROFESSOR APIs------------------------------------

// CREATE
// adds a professor to professor database
export const addProfessor = async(profParams) => {
    console.log("addProfessor()");

    //api invoke url
    const url = `${apiUrl}professors/addProfessor`;

    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            "id": profParams.id,
            "name": profParams.name,
            "department": profParams.department || "N/A",
            "current_courses": studentParams.current_courses
        })
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};

// DELETE
//function that calls api to delete a student given student id
export const deleteProfessor = async(id) => {
    console.log("deleteProfessor()");

    //api invoke url
    const url = `${apiUrl}professors/deleteProfessor?id=${id}`;

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

// READ
//function that calls api to get professor info given id
export const getProfessorInfo = async(id) => {
    console.log("getProfessorInfo()");
    
    //api invoke url
    const url = `${apiUrl}professors/getProfessorInfo?id=${id}`;

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

// UPDATE
// function that calls api to update professor info
export const editProfessor = async (profParams) => {
    console.log("editProfessor()");

    //api invoke url
    const url = `${apiUrl}professors/editProfessor`

    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            "id": profParams.id,
            "department": profParams.department,
            "current_courses": profParams.currentCourses
        })
    };

    const { data, error } = await callExternalApi({ url, config });

    return {
        data: data || null,
        error,
    };
};