const fs = require('fs');

// 注文時の処理
const button = document.querySelector('button[type="submit"]')
console.log(button)
button.addEventListener('click', function(event) {
    const price = Number(this.getAttribute('data-price'));
    const name = this.getAttribute('data-name');
    console.log(name, price)
    const logMessage = `${name} ¥np${price}\n`;
    fs.appendFileSync('log.txt', logMessage, 'utf8');
});