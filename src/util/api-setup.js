import { callExternalApi } from "./call-external-api";

const apiFilterTableUrl = import.meta.env.FILTER_TABLE_API_URL;

export const getCourseFromCourseCatalog = async(tableFilter) => {
    console.log("getCourseFromCourseCatalog()");
    const config = {
        //url: 'https://rr0ix1pdq0.execute-api.us-east-1.amazonaws.com/finalStage/courseCatalog?tableFilter=10',
        url: `${apiFilterTableUrl}tableFilter=10`,
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({"tableColumn": "course_name"})
    };
    const { data, error } = await callExternalApi({ config });
    console.log(data);
    return {
        data: data || null,
        error,
    };
};