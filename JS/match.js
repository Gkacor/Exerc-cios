const cpf = 'Meu cpf é 123.465.451-22';

const regex = new RegExp('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9{2}');

console.log(cpf.match(regex));