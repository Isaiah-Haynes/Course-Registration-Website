export const callExternalApi = async (options) => {
    console.log("callExternalApi()");

    try {
        const response = await fetch(options.config);
        const { data } = await response;
        console.log(response);
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