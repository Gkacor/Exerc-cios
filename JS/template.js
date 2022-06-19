let meuNome = 'GC';
let meuSobrenome = 'Coradin'
let minhaProfissao = 'Desenvolvedor'

//Sem template string
console.log('Olá, eu sou ' + 
                meuNome +
             meuSobrenome + 
             " e a minha profissão é: "
              + minhaProfissao);


//com template string
console.log(`Olá, meu nome é ${meuNome} ${meuSobrenome} e minha profissão é: ${minhaProfissao}`);

console.log(`O resiltado da soma de 1 + 1 é: ${1 + 1}`);

console.log(`O objeto json ${{chave: 'valor'}}`);

let meuObjeto = {
   chave: 'novo valor'
}
