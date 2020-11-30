const { Telegraf } = require('telegraf');
let bot = new Telegraf(process.env.BOT_TOKEN); //before set the token
let FLAG = '';
let USER_INPUT_VALUE;
const HELP_TEXT = 
`
bot developed by HeyJOe,
the bot is able to:
1. factorial of a number
2. square root 
3. n square of a number
4. power
5. text-formatter
6. mask calculator /n
`;

///variabili per le funzioni
let base = undefined;  
let thpower = undefined;
let radical = undefined;

function clear(){
  FLAG = '';
  USER_INPUT_VALUE = undefined;
}

function fattorial(ctx){
  function _factorial(n){
    let fact = 1;
    for(n;n>0;n--){
        fact*=n;
      }
    return fact;
  }
  let number = parseInt(USER_INPUT_VALUE);
  if(isNaN(number))ctx.reply('not valid number');
    else if(number<= 0 || number>=171)ctx.reply('number must be between 1 and 170');
    else ctx.reply("the factorial of " + number + " is " + _factorial(number)); 
    clear();
}

function power(ctx){
  if(base == undefined){
    base = parseFloat(USER_INPUT_VALUE);
    if(isNaN(base)){
      ctx.reply('base not valid');
      base = undefined;
      clear();
    }
    else ctx.reply('insert l\'thpower:');
  }
  else if(thpower == undefined){
    thpower = parseFloat(USER_INPUT_VALUE);
    if(isNaN(thpower)){
      ctx.reply('power not valid');
      thpower = undefined;
      base = undefined;
      clear();
    }
  }
  if(base != undefined && thpower != undefined){
    ctx.reply(base + ' root ' + thpower +' = '+Math.pow(base,thpower));
    base = undefined;
    thpower = undefined;
    clear();
  }
}

function text(ctx){
  let stringa_adattata = "\'";
    let testo = USER_INPUT_VALUE;
    for(let i=0;i<testo.length;i++)
        {
          let word = testo[i];
          if(word == `\n`) word= `\\n`;
          if(word == `'`) word = `\\'`;
          if(word == `"`) word = `\\"`;
          if(word == `\\`) word = `\\\\`;
          stringa_adattata += word;                  
        }
    stringa_adattata += "\'";
    ctx.reply(stringa_adattata);
  clear();
}

function sqrt(ctx){
  let number = parseFloat(USER_INPUT_VALUE);
  if (isNaN(number)) ctx.reply('number not valid');
  else if (number<0) ctx.reply('complex number');
  else ctx.reply(Math.sqrt(number));
  clear();
}

function sqrn(ctx){
  if(base == undefined){
    base = parseInt(USER_INPUT_VALUE);
    if(isNaN(base) || base <= 0){
      base = undefined;
      ctx.reply('base not valid');
      clear();
    }
    else ctx.reply('insert radical:');
  }
  else if(radical == undefined){
    radical = parseFloat(USER_INPUT_VALUE);
    if(isNaN(radical)){
      base = undefined;
      radical = undefined;
      ctx.reply('radical not valid');
      clear();
    }
  }
  if(base != undefined && radical != undefined){
    if (base%2 == 0 && radical<0) ctx.reply('impossible calculate root ' + base+ 'of a negative number');
    else ctx.reply("root "+base+" of "+radical+" is: "+Math.pow(radical,1/base));
    base = undefined;
    radical = undefined;
    clear();
  }
}

function maskcalc(ctx){
    let maskn = parseInt(USER_INPUT_VALUE);
    let long_mask = '';
    let byte = 0;
    if(isNaN(maskn) || maskn>32 || maskn<1)ctx.reply('mask not valid');
    else{
      for(let i=0;i<Math.floor(maskn/8);i++){long_mask+='255.';byte++;}
      let r = maskn%8;
      switch (r){
          case 1:{
          long_mask += '128';
          break;
        }
          case 2:{
          long_mask += '192';
          break;
        }
          case 3:{
          long_mask += '224';
          break;
        }
          case 4:{
          long_mask += '240';
          break;
        }
          case 5:{
          long_mask += '248';
          break;
        }
          case 6:{
          long_mask += '252';
          break;
        }
          case 7:{
          long_mask += '254';
          break;
        }
      }
      if(maskn%8 != 0){
        byte++;
        if(byte<4) long_mask += '.';
      }
      for(byte+1;byte<4;byte++){
        long_mask+='0';
        if(byte < 3)long_mask += '.';
      }
    }
    ctx.reply("mask is: " + long_mask);
  clear();
}

bot.start((ctx) => {ctx.reply('Welcome! To HeyJOe\'s bot\n digit /help to view the possible commands');});
bot.help((ctx) => ctx.reply(HELP_TEXT));

bot.command('/fact',     (ctx) => {FLAG = 'fact';     ctx.reply("insert a number between 1 and 170:");});
bot.command('/sqrt',     (ctx) => {FLAG = 'sqrt';     ctx.reply("insert the number for the square root");});
bot.command('/sqrn',     (ctx) => {FLAG = 'sqrn';     ctx.reply("insert base of root");});
bot.command('/pow',      (ctx) => {FLAG = 'pow';      ctx.reply("insert base of the power");});
bot.command('/text',     (ctx) => {FLAG = 'text';     ctx.reply('insert text:');});
bot.command('/maskcalc', (ctx) => {FLAG = 'maskcalc'; ctx.reply('insert a mask between 8 and 30:');});


bot.on('text',(ctx) => {
  USER_INPUT_VALUE = ctx.message.text;
  if      (FLAG == 'fact')     fattorial(ctx);
  else if (FLAG == 'pow')      power(ctx);
  else if (FLAG == 'sqrt')     sqrt(ctx);
  else if (FLAG == 'sqrn')     sqrn(ctx);
  else if (FLAG == 'text')     text(ctx);
  else if (FLAG == 'maskcalc') maskcalc(ctx);
});

bot.launch();