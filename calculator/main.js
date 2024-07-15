function append(value) {
    document.getElementById('result').value += value;
}

function clearInput() {
    document.getElementById('result').value = '';
}

function calculate() {
    let input = document.getElementById('result').value;
    let result = eval(input);
    document.getElementById('result').value = result;
}
