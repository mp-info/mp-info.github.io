function url(pdf) {
    const url_repo_pdf = 'https://mozilla.github.io/pdf.js/web/viewer.html?file=https://raw.githubusercontent.com/mp-info/mp-info.github.io/main/files/'
    return url_repo_pdf + pdf + '#zoom=page-fit&pagemode=none';
}

function button_cor(pdf, id_pdf, id_button) {
    let state = "Correction";
    const pub = {};
    $(`#${id_pdf}`).attr('src', url(`${pdf}.pdf`));
    $(`#${id_button}`).prop('value', state);
    pub.switch = function () {
        $(`#${id_pdf}`).attr('src', url(`${pdf}${state == "Correction" ? "_cor" : ""}.pdf`));
        state = state == "Énoncé" ? "Correction" : "Énoncé";
        $(`#${id_button}`).prop('value', state);
    };
    return pub;
};
