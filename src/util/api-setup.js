import { callExternalApi } from "./call-external-api";

const apiFilterTableUrl = import.meta.env.VITE_FILTER_TABLE_API_URL;

export const getCourseFromCourseCatalog = async(filter) => {
    console.log("getCourseFromCourseCatalog()");
    
    // const url = 'https://rr0ix1pdq0.execute-api.us-east-1.amazonaws.com/finalStage/courseCatalog?tableFilter=10';
    const url = `${apiFilterTableUrl}tableFilter=${filter}`;
    const config = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({"tableColumn": "course_name"})
    };
    console.log(url);
    const { data, error } = await callExternalApi({url, config });
    // console.log(data);
    return {
        data: data || null,
        error,
    };
};