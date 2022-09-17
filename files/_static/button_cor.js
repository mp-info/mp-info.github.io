function url(pdf) {
    const url_repo_pdf = 'https://mozilla.github.io/pdf.js/web/viewer.html?file=https://raw.githubusercontent.com/mp-info/mp-info.github.io/main/files/'
    return url_repo_pdf + pdf + '#zoom=page-fit&pagemode=none';
}

function button_cor(pdf_enonce, pdf_cor, id_pdf, id_button) {
    let state = "Correction";
    const pub = {};
    $(`#${id_pdf}`).attr('src', url(pdf_enonce));
    $(`#${id_button}`).prop('value', state);

    pub.switch = function () {
        $(`#${id_pdf}`).attr('src', url(state == "Énoncé" ? pdf_enonce : pdf_cor));
        state = state == "Énoncé" ? "Correction" : "Énoncé";
        $(`#${id_button}`).prop('value', state);
    };

    return pub;
};
