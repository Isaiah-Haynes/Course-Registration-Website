import { callExternalApi } from "./call-external-api";

const apiFilterTableUrl = import.meta.env.VITE_FILTER_TABLE_API_URL;


//searches courseCatalog for filter in course_name
export const searchMultipleCourseCatalog = async(filter) => {
    console.log("getCourseFromCourseCatalog()");
    
    //gets api url from .env and uses filter from StudentEnrollView.vue
    const url = `${apiFilterTableUrl}tableFilter=${filter}`;
    //adds required options for fetch to config
    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({"tableColumn": "course_name"})
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