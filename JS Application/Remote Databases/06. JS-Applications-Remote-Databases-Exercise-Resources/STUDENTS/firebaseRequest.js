export const apiKey = ""; // firebase url

export const postStudents = studentBody => {
    return fetch(apiKey + "students.json", {
        method: "POST",
        body: JSON.stringify(studentBody)
    })
    .then(x => x.json());
};

export const getStudents = () => {
    return fetch(apiKey + "students.json")
    .then(x => x.json())
};