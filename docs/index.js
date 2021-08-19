var req = new XMLHttpRequest();

/**
 * Makes a request to a given API endpoint and writes response to @param resElemId
 * @param {string} endpoint API endpoint
 * @param {{key: string, val: string}[]} params URL parameters
 * @param {string} resElemId ID of `div` element to contain API JSON response
 * @param {string} loaderElemId ID of `div` element to contain loader
 */
function createButton(endpoint, params, resElemId, loaderElemId) {
    var url = `https://botw-compendium.herokuapp.com/api/v2${endpoint}?foo=foo`;
    params.forEach((item) => {
        url += `&${encodeURIComponent(item.key)}=${encodeURIComponent(item.val)}`;
    })

    var loader = document.getElementById(loaderElemId);
    loader.setAttribute("class", "loader");

    req.onreadystatechange = () => {
        if(req.readyState == 4) {
            loader.removeAttribute("class");
        }
        if(req.status == 200) {
            res = JSON.parse(req.responseText);

            if (!document.getElementById(resElemId + "Json")) {
                var div = document.getElementById(resElemId);

                var pre = document.createElement("pre");
                pre.setAttribute("v-pre", "");
                pre.setAttribute("data-lang", "json");

                var code = document.createElement("code");
                code.setAttribute("id", resElemId + "Json");
                code.setAttribute("class", "lang-json");
                code.innerHTML = JSON.stringify(res, null, 4);

                pre.appendChild(code);
                div.appendChild(pre);
            } else {
                var code = document.getElementById(resElemId + "Json");
                code.innerHTML = JSON.stringify(res, null, 4);
            }
            Prism.highlightElement(code);
        }
    }

    req.open("GET", url, true);
    req.send();
}