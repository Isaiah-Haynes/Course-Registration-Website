//DO NOT CHANGE THIS FUNCTION!! all necessary data will be returned
//in "data" and can be accessed in whichever file called the function
//in api-setup.js

export const callExternalApi = async (options) => {
    console.log("callExternalApi()");

    try {
        //assigns response to return from fetch call
        const response = await fetch(options.url, options.config);
        // console.log(response);

        //gets data from fetch response
        const data = await response.json();
        // console.log(data);

        //returns the data from fetch response, values in data should be parsed
        //where needed, e.g. when used to filter courseCatalog, courses will be
        //retrieved from data.courses in whichever view called this function
        return {
            data,
            error: null,
        };
    } catch (error) {
        return {
            data: null,
            error,
        };
    };

};