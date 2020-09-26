function fromJsonToHtmlTable(input){    

    function escapeHtml(unsafe) {
        const safe = unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");

            return safe;
    }
    
    let obj = input;
    let outputArr = ["<table>"];
    let keys = "   <tr>"
    for (const key in obj[0]) {
        keys += "<th>" + escapeHtml(`${key}`) + "</th>";
    }
    
    keys += "</tr>";
    outputArr.push(keys);

    for(let i = 0; i < obj.length; i++){
        let values = "   <tr>"
        for (const key in obj[i]) {
            values += "<td>" + escapeHtml(`${obj[i][key]}`) + "</td>";
        }

        values += "</tr>";
        outputArr.push(values);
    }

    outputArr.push("</table>");

    for (const iterator of outputArr) {
        console.log(iterator);
    }
}

fromJsonToHtmlTable([{"Name":"Pesho <div>-a","Age":20,"City":"Sofia"},
{"Name":"Gosho","Age":18,"City":"Plovdiv"},{"Name":"Angel","Age":18,"City":"Veliko Tarnovo"}]
);