export const callExternalApi = async (options) => {
    console.log("callExternalApi()");

    try {
        const url = 'https://rr0ix1pdq0.execute-api.us-east-1.amazonaws.com/finalStage/courseCatalog?tableFilter=10';
        // const response = await fetch(options.config.url, options.config.method, options.config.headers, options.config.body);
        const response = await fetch(options.url, options.config);
        // console.log(response);
        const data = await response.json();
        // console.log(data);
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

// export const callExternalApi = async (options) => {
//     console.log("callExternalApi()");
//     await fetch(options.config.url, options.config.methods,)
// }