function url(pdf) {
    return 'https://mozilla.github.io/pdf.js/web/viewer.html?file=' + pdf + '#zoom=page-width&pagemode=none';
}

function button_cor(pdf, id_pdf, id_button) {
    let state = "Correction";
    const pub = {};
    $(`#${id_pdf}`).attr('src', url(pdf));
    $(`#${id_button}`).prop('value', state);
    pub.switch = function () {
        $(`#${id_pdf}`).attr('src', url(`${pdf.substring(0, pdf.length-4)}${state == "Correction" ? "_cor" : ""}.pdf`));
        state = state == "Énoncé" ? "Correction" : "Énoncé";
        $(`#${id_button}`).prop('value', state);
    };
    return pub;
};
