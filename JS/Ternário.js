let isValid = true;

//sem Ternário
function verify(isValid) {
    if(isValid) {
        return true;
    } else {
       return false;
    }
}

console.log(verify(isValid));

//com Ternário
const result = isValid ? true : false;

let zero = 0;

const numeroResultado = zero == 0 ? 0 : -1;

console.log(numeroResultado)