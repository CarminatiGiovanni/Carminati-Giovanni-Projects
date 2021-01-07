const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

window.addEventListener("resize", function() { //check if the screen during the game is resized
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
});

const n_color = ["YELLOW", "RED", "BLACK", "GREEN"];
const fruit_and_colors = {
    "YELLOW": ["banana", "lemon", "pineapple", ],
    "ORANGE": ["orange", "peach"],
    "RED": ["apple", "cherry", "kiwi"],
    "BLACK": ["bomb"],
    "GREEN": ["avocado", "pear"]
};
const able_fruits = [
    "./IMG/FRUITS/apple.svg", "./IMG/FRUITS/avocado.svg",
    "./IMG/FRUITS/banana.svg", "./IMG/FRUITS/cherry.svg",
    "./IMG/FRUITS/kiwi.svg", "./IMG/FRUITS/lemon.svg",
    "./IMG/FRUITS/pineapple.svg", "./IMG/FRUITS/orange.svg",
    "./IMG/FRUITS/peach.svg", "./IMG/FRUITS/pear.svg",
];
const able_cutted_fruits = [
    "./IMG/CUTTEDFRUITS/apple.svg", "./IMG/CUTTEDFRUITS/avocado.svg",
    "./IMG/CUTTEDFRUITS/banana.svg", "./IMG/CUTTEDFRUITS/cherry.svg",
    "./IMG/CUTTEDFRUITS/kiwi.svg", "./IMG/CUTTEDFRUITS/lemon.svg",
    "./IMG/CUTTEDFRUITS/pineapple.svg", "./IMG/CUTTEDFRUITS/orange.svg",
    "./IMG/CUTTEDFRUITS/peach.svg", "./IMG/CUTTEDFRUITS/pear.svg",
];

const n_splashs_for_color = 6;
let gameOver = false;
const range_of_force = 450;
const min_force = 200;
let painting = false;
let id;
let dict = {};
const max_life = 5;
let life = 5;
let dict_size = 0;
let imageSizeX = 100,
    imageSizeY = 100;
let splashSizeX = 100,
    splashSizeY = 100;
let LifeSizeX = 50,
    LifeSizeY = 50;
let listOfActiveSplash = [];
let listOfFallingFruitPiecies = [];
let SCORE = 0;

class Fruit {
    spin;
    spinSpeed;
    x;
    y;
    vx;
    static G = 1;
    m;
    F;
    image;
    state;
    fruitName;
    fruitColor;
    constructor(img, x, y, vx, F) {
        this.spin = Math.floor(Math.random() * 360);
        this.spinSpeed = randomSpin();
        this.image = img;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.F = F;
        this.m = mass(this);
        this.state = "integer" //cutted or integer
        this.fruitName = "";
        this.fruitColor = "BLACK";
        this.defineThisName();
    }

    defineThisName = function() {
        let s = this.image.src;
        let n = s.search("/IMG/FRUITS/");
        s = s.substr(n + 12, (s.length) - n - 12 - 4);
        this.fruitName = s;
        this.defineThisColor();
    }

    defineThisColor = function() {
        for (let key in fruit_and_colors) {
            if (fruit_and_colors[key].includes(this.fruitName)) {
                this.fruitColor = key;
                return;
            }
        }
        this.fruitColor = "BLACK";
    }
}

class Splash {
    spin;
    image;
    time;
    duration;
    x;
    y;
    constructor(img, x, y) {
        this.spin = Math.floor(Math.random() * 360);
        this.image = img;
        this.time = 0;
        this.duration = 100;
        this.x = x;
        this.y = y;
    }
}

class CuttedFruit {
    x;
    spin;
    spinSpeed;
    y;
    vx;
    image;
    F;
    m;
    constructor(img, x, y, vx) {
        this.spin = Math.floor(Math.random() * 360);
        this.spinSpeed = randomSpin();
        this.image = img;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.F = 0;
        this.m = 10;
    }
}

function animate() {
    if (life < 1) gameOver = true;
    if (!gameOver) {
        //generare i frutti
        createFruit();
        //muovere i frutti
        moveFruit();
        //disegnare i frutti
        draw();
    } else {
        gameOverText();
    }

}

const WaveProprieties = {
    max_n_of_fruit: 6, //6
    max_n_of_bombs: 3, //3
    min_delay: 20,
    max_delay: 40,
}

let Wave = {
    n_of_fruit: 0,
    n_of_bombs: 0, //in better version can change in the difficulty
    wavetype: { type: "group", delay: 0, time_passed: 0 }, //group, 0 ---- onebyone, time,
    placed_fruits: 0,
    placed_bombs: 0,
    fruit_remaining: 0,
}

function createFruit() {

    if (Wave.fruit_remaining == 0 && listOfFallingFruitPiecies.length == 0) {
        let f = Math.floor(Math.random() * WaveProprieties.max_n_of_fruit);
        let b = Math.floor(Math.random() * WaveProprieties.max_n_of_bombs);

        Wave.n_of_fruit = f;
        Wave.n_of_bombs = b;
        let wt = Math.floor(Math.random() * 2);
        if (wt == 0) Wave.wavetype = { type: "group", delay: 0, time_passed: 0 };
        else {
            Wave.wavetype = {
                type: "onebyone",
                delay: Math.floor(Math.random() * (WaveProprieties.max_delay - WaveProprieties.min_delay) + WaveProprieties.min_delay),
                time_passed: 0
            };
            //console.log(Wave.wavetype.delay);
        }
        Wave.placed_bombs = 0;
        Wave.fruit_remaining = b + f;
        Wave.placed_fruits = 0;
    }
    //console.log(Wave);

    if (Wave.placed_bombs + Wave.placed_fruits < Wave.n_of_fruit + Wave.n_of_bombs) {
        if (Wave.wavetype.type == "group") {
            for (let i = 0; i < Wave.n_of_fruit; i++) {
                f = new Fruit(
                    generateImageObject(imageSizeX, imageSizeY, chooseFruit(), String(id)),
                    Math.floor(Math.random() * (canvas.width - imageSizeX - 5)),
                    canvas.height - imageSizeY, Math.floor(Math.random() * 20) - 10,
                    Math.floor(Math.random() * range_of_force) + min_force
                );
                dict[String(id)] = f;
                dict_size++;
                id++;
                Wave.placed_fruits++;
            }
            for (let g = 0; g < Wave.n_of_bombs; g++) {
                f = new Fruit(
                    generateImageObject(imageSizeX, imageSizeY, "./IMG/FRUITS/bomb.svg", String(id)),
                    Math.floor(Math.random() * (canvas.width - imageSizeX - 5)),
                    canvas.height - imageSizeY, Math.floor(Math.random() * 20) - 10,
                    Math.floor(Math.random() * range_of_force) + min_force
                );
                dict[String(id)] = f;
                dict_size++;
                id++;
                Wave.placed_bombs++;
            }
        } else {
            if (Wave.wavetype.time_passed < Wave.wavetype.delay) Wave.wavetype.time_passed++;
            else {
                //console.log(Wave);
                Wave.wavetype.time_passed = 0;
                let n = Math.floor(Math.random() * (Wave.n_of_bombs - Wave.placed_bombs + Wave.n_of_fruit - Wave.placed_fruits));
                if (n < Wave.n_of_bombs - Wave.placed_bombs) { //piazza bomba
                    f = new Fruit(
                        generateImageObject(imageSizeX, imageSizeY, "./IMG/FRUITS/bomb.svg", String(id)),
                        Math.floor(Math.random() * (canvas.width - imageSizeX - 5)),
                        canvas.height - imageSizeY, Math.floor(Math.random() * 20) - 10,
                        Math.floor(Math.random() * range_of_force) + min_force
                    );
                    dict[String(id)] = f;
                    dict_size++;
                    id++;
                    Wave.placed_bombs++;
                } else { //piazza frutto
                    //Wave.wavetype.delay = 0;
                    f = new Fruit(
                        generateImageObject(imageSizeX, imageSizeY, chooseFruit(), String(id)),
                        Math.floor(Math.random() * (canvas.width - imageSizeX - 5)),
                        canvas.height - imageSizeY, Math.floor(Math.random() * 20) - 10,
                        Math.floor(Math.random() * range_of_force) + min_force
                    );
                    dict[String(id)] = f;
                    dict_size++;
                    id++;
                    Wave.placed_fruits++;
                }

            }
        }
    }

}

function moveFruit() { //da rivedere prima della fine
    function moveXside(x, vx) {
        x += vx;
        if (x < 0) {
            vx = vx * (-1);
            x = x * (-1);
        } else if ((x + imageSizeX) > canvas.width) {
            vx = vx * (-1);
            x = x - (2 * (x + imageSizeX - canvas.width));
        }
        return [x, vx];
    }

    function moveYside(F, m, y) {
        let ah = F / m; //accelerazione verso l'alto
        let a = -ah + Fruit.G; //-a + G
        y = y + a / 2;
        F = -a * m;
        if (y < 0) {
            y = 0;
            F = 0;
        }
        return [F, y];
    }

    for (key in dict) {
        if (dict[key].y < canvas.height - imageSizeY + 1) {
            let l = moveXside(dict[key].x, dict[key].vx);
            dict[key].x = l[0];
            dict[key].vx = l[1];

            l = moveYside(dict[key].F, dict[key].m, dict[key].y);
            dict[key].F = l[0];
            dict[key].y = l[1];

        } else {
            dict_size--;
            if (dict[key].image.src.search("bomb.svg") == -1) {
                life--;
            }
            delete dict[key];
            Wave.fruit_remaining--;
        }
    }
    for (a in listOfFallingFruitPiecies) {
        if (listOfFallingFruitPiecies[a].y < canvas.height - imageSizeY + 1) {
            //movimento del pezzo
            let l;
            l = moveXside(listOfFallingFruitPiecies[a].x, listOfFallingFruitPiecies[a].vx);
            listOfFallingFruitPiecies[a].x = l[0];
            listOfFallingFruitPiecies[a].vx = l[1];

            l = moveYside(listOfFallingFruitPiecies[a].F, listOfFallingFruitPiecies[a].m, listOfFallingFruitPiecies[a].y);

            listOfFallingFruitPiecies[a].y = l[1];
            listOfFallingFruitPiecies[a].F = l[0];
            ////////////////////////////////////7

        } else {
            listOfFallingFruitPiecies.splice(a, 1);
        }
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (a in listOfActiveSplash) { //draw splashes
        if (listOfActiveSplash[a].time < listOfActiveSplash[a].duration) {
            ctx.save();
            ctx.translate(listOfActiveSplash[a].x + listOfActiveSplash[a].image.width / 2, listOfActiveSplash[a].y + listOfActiveSplash[a].image.height / 2);
            ctx.rotate(listOfActiveSplash[a].spin * Math.PI / 180);
            ctx.translate(-listOfActiveSplash[a].image.width / 2, -listOfActiveSplash[a].image.height / 2);
            ctx.drawImage(listOfActiveSplash[a].image, 0, 0, listOfActiveSplash[a].image.width, listOfActiveSplash[a].image.height);
            listOfActiveSplash[a].time++;
            ctx.restore();
        } else listOfActiveSplash.splice(a, 1);
    }

    for (a in listOfFallingFruitPiecies) { //draw falling piecies of cutted fruit

        ctx.save();
        ctx.translate(listOfFallingFruitPiecies[a].x + listOfFallingFruitPiecies[a].image.width / 2, listOfFallingFruitPiecies[a].y + listOfFallingFruitPiecies[a].image.height / 2);
        ctx.rotate(listOfFallingFruitPiecies[a].spin * Math.PI / 180);
        listOfFallingFruitPiecies[a].spin += listOfFallingFruitPiecies[a].spinSpeed;
        ctx.translate(-listOfFallingFruitPiecies[a].image.width / 2, -listOfFallingFruitPiecies[a].image.height / 2);
        ctx.drawImage(listOfFallingFruitPiecies[a].image, 0, 0, listOfFallingFruitPiecies[a].image.width, listOfFallingFruitPiecies[a].image.height);
        ctx.restore();
    }
    for (key in dict) { //draw the fruit 
        ctx.save();
        ctx.translate(dict[key].x + dict[key].image.width / 2, dict[key].y + dict[key].image.height / 2);
        ctx.rotate(dict[key].spin * Math.PI / 180);
        dict[key].spin += dict[key].spinSpeed;
        ctx.translate(-dict[key].image.width / 2, -dict[key].image.height / 2);
        ctx.drawImage(dict[key].image, 0, 0, dict[key].image.width, dict[key].image.height);
        ctx.restore();
    }

    life_and_informations();
}

function checkCollision(mx, my, ix, iy, w, h) {
    //console.log(mx + " " + my + " " + ix + " " + iy + " ");
    if (mx > ix && mx < ix + w && my > iy && my < iy + h) return true;
    else return false;
}

function add_cutted_elements(cuttedFruit) {
    if (cuttedFruit.image.src.search("bomb.svg") == -1) {
        for (let i = 0; i < 2; i++) {
            f = new CuttedFruit(
                generateImageObject(imageSizeX, imageSizeY, imagecutted(cuttedFruit.image.src), ""),
                cuttedFruit.x, cuttedFruit.y,
                Math.floor(Math.random() * 20) - 10
            );
            listOfFallingFruitPiecies.push(f);
        }
        createSplashEffect(cuttedFruit);
    } else {
        //gameOver = true;
        life -= 2;
    }

}

function createSplashEffect(fruit) {
    let n = Math.floor(Math.random() * splashSizeX) + splashSizeY; //splashSizeX == splashSizeY
    let splash = new Splash(
        generateImageObject(n, n, "./IMG/SPOT/" + fruit.fruitColor + "/spot" + Math.floor(Math.random() * n_splashs_for_color + 1) + ".svg", ""),
        fruit.x,
        fruit.y
    );
    listOfActiveSplash.push(splash);
}

function imagecutted(i) {
    let n = i.search("/IMG/FRUITS/");
    i = i.substr(n + 12, (i.length) - n - 12 - 4);
    if (able_cutted_fruits.includes("./IMG/CUTTEDFRUITS/" + i + ".svg")) return able_cutted_fruits[able_cutted_fruits.indexOf("./IMG/CUTTEDFRUITS/" + i + ".svg")];
    return "./IMG/fruitsalad.svg";

}

window.addEventListener("load", () => { //funzioni prese da un programma di disegno
    function startPosition() {
        painting = true;
        countCombo = true;
    }

    function finishedPosition() {
        painting = false;
        ctx.beginPath();
    }

    function knife_animation(e) {
        if (!painting) return;
        ctx.lineWidth = 10;
        ctx.lineCap = "round"
        ctx.shadowColor = "red";
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);
        for (key in dict) {
            if (checkCollision(e.clientX, e.clientY, dict[key].x, dict[key].y, imageSizeX, imageSizeY)) {
                add_cutted_elements(dict[key]);
                if (dict[key].image.src.search("bomb.svg") == -1) {
                    SCORE++;

                }
                delete dict[key];
                dict_size--;
                Wave.fruit_remaining--;
            }
        }
    }
    canvas.addEventListener("mousedown", startPosition);
    canvas.addEventListener("mouseup", finishedPosition);
    canvas.addEventListener("mousemove", knife_animation);
});

function startGame() {
    id = 0;
    window.onload = setInterval(animate, 1000 / 30); //chiamata alla funzione animate
}

function chooseFruit() {
    return able_fruits[Math.floor(Math.random() * able_cutted_fruits.length)];
}

function mass(a) {
    return 10;
}

function gameOverText() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (canvas.height > canvas.width) {
        height = Math.floor(canvas.width * 0.8);
        width = height;
        offseth = Math.floor((canvas.height - height) / 2);
        offsetw = Math.floor(canvas.width * 0.1);
    } else { //width>height
        height = Math.floor(canvas.height * 0.8);
        width = height;
        offseth = Math.floor(canvas.height * 0.1);
        offsetw = Math.floor((canvas.width - width) / 2);
    }
    ctx.drawImage(generateImageObject(width, height, "./IMG/gameOver.svg", ""), offsetw, offseth, width, height);
}

function life_and_informations() {
    for (let i = 0; i < max_life; i++) {
        if (i < life) {
            ctx.drawImage(generateImageObject(LifeSizeX, LifeSizeY, "./IMG/heart_red.svg", ""), canvas.width - (LifeSizeX * (max_life - i)) - LifeSizeX, LifeSizeY / 2, LifeSizeX, LifeSizeY);
        } else {
            ctx.drawImage(generateImageObject(LifeSizeX, LifeSizeY, "./IMG/heart_black.svg", ""), canvas.width - (LifeSizeX * (max_life - i)) - LifeSizeX, LifeSizeY / 2, LifeSizeX, LifeSizeY);
        }
    }

    ctx.font = 'bold 30pt Menlo';
    ctx.textBaseline = "middle";
    ctx.fillStyle = '#FF1D25';
    ctx.fillText('SCORE: ' + SCORE, LifeSizeX / 2, LifeSizeY);

}

function generateImageObject(width, height, src, id) {
    let img = new Image(width, height)
    img.src = src;
    if (id != "") img.id = id;
    return img;
}

function randomSpin() {
    return Math.floor(Math.random() * 10) - 5;
}