
const originalConsoleLog = console.log;


function redirectConsole(output) {
    console.log = function (...args) {
        output.textContent += args.join(' ') + '\n';
        originalConsoleLog.apply(console, args);
    };
}
function solve_quad(equation) {
    try {

        const [lhs, rhs] = equation.split('=').map(side => side.trim());

    
        const match = lhs.match(/^(-?\d*)\s*\*?\s*([a-z])\^2\s*([\+\-]?)\s*(\d*)\s*\*?\s*\2\s*([\+\-]?)\s*(\d*)$/);

        if (!match) {
            throw new Error("Invalid quadratic equation format.");
        }


        const aStr = match[1]; 
        const varb = match[2]; 
        const bOp = match[3];  
        const bStr = match[4]; 
        const cOp = match[5];  
        const cStr = match[6]; 

        const a = aStr === "" || aStr === "-" ? 
            (aStr === "-" ? -1 : 1) : 
            parseInt(aStr);


        const b = bStr === "" ? 0 : parseInt(bOp + bStr);

 
        const c = cStr === "" ? 0 : parseInt(cOp + cStr);

        const rhsValue = parseInt(rhs) || 0;
        const adjustedC = c - rhsValue;

        if (a === 0) {
            throw new Error("Coefficient of x^2 is zero. This is not a quadratic equation.");
        }

        const discriminant = b ** 2 - 4 * a * adjustedC;
        if (discriminant < 0) {
            return "No real roots.";
        } else if (discriminant === 0) {
            const root = -b / (2 * a);
            return `x = ${root}`;
        } else {
            const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            return `Either x = ${root1}, or x = ${root2}`;
        }
    } catch (error) {
        return "Error: " + error.message;
    }
}
        function solve(equation) {
            try {
                const [lhs, rhs] = equation.split('=').map(side => side.trim());
                let varb, coeff = 0, cons = 0;
        
    
                const match = lhs.match(/(-?\d*)([a-z])\s*([\+\-])\s*(\d+)/);
                if (match) {
                    coeff = parseInt(match[1]) || 1;
                    varb = match[2];
                    cons = parseInt(match[3] + match[4]);
                }
        
                const result = (parseInt(rhs) - cons) / coeff;
                return `${varb} = ${result}`;
            } catch {
                return "Error: Unable to solve the equation.";
            }
        }
        function calculateResistance(rstrs, type = "series") { //rstrs= resistors
            if (type === "series") {
                let total = 0;
                for (let i = 0; i < rstrs.length; i++) {
                    total += rstrs[i];
                }
                return total;
            } else if (type === "parallel") {
                let total = 0;
                for (let i = 0; i < rstrs.length; i++) {
                    total += 1 / rstrs[i];
                }
                return 1 / total;
            }
            return "Invalid circuit type.";
        }
//yo bartosz checkpoint for you
function getElement(element) {
            const periodicT = {
                H: { name: "Hydrogen", atomicN: 1 },
                He: { name: "Helium", atomicN: 2 },
                Li: { name: "Lithium", atomicN: 3 },
                Be: { name: "Beryllium", atomicN: 4 },
                B: { name: "Boron", atomicN: 5 },
                C: { name: "Carbon", atomicN: 6 },
                N: { name: "Nitrogen", atomicN: 7 },
                O: { name: "Oxygen", atomicN: 8 },
                F: { name: "Fluorine", atomicN: 9 },
                Ne: { name: "Neon", atomicN: 10 },
                Na: { name: "Sodium", atomicN: 11 },
                Mg: { name: "Magnesium", atomicN: 12 },
                Al: { name: "Aluminum", atomicN: 13 },
                Si: { name: "Silicon", atomicN: 14 },
                P: { name: "Phosphorus", atomicN: 15 },
                S: { name: "Sulfur", atomicN: 16 },
                Cl: { name: "Chlorine", atomicN: 17 },
                Ar: { name: "Argon", atomicN: 18 },
                K: { name: "Potassium", atomicN: 19 },
                Ca: { name: "Calcium", atomicN: 20 },
                Sc: { name: "Scandium", atomicN: 21 },
                Ti: { name: "Titanium", atomicN: 22 },
                V: { name: "Vanadium", atomicN: 23 },
                Cr: { name: "Chromium", atomicN: 24 },
                Mn: { name: "Manganese", atomicN: 25 },
                Fe: { name: "Iron", atomicN: 26 },
                Co: { name: "Cobalt", atomicN: 27 },
                Ni: { name: "Nickel", atomicN: 28 },
                Cu: { name: "Copper", atomicN: 29 },
                Zn: { name: "Zinc", atomicN: 30 },
                Ga: { name: "Gallium", atomicN: 31 },
                Ge: { name: "Germanium", atomicN: 32 },
                As: { name: "Arsenic", atomicN: 33 },
                Se: { name: "Selenium", atomicN: 34 },
                Br: { name: "Bromine", atomicN: 35 },
                Kr: { name: "Krypton", atomicN: 36 },
                Rb: { name: "Rubidium", atomicN: 37 },
                Sr: { name: "Strontium", atomicN: 38 },
                Y: { name: "Yttrium", atomicN: 39 },
                Zr: { name: "Zirconium", atomicN: 40 },
                Nb: { name: "Niobium", atomicN: 41 },
                Mo: { name: "Molybdenum", atomicN: 42 },
                Tc: { name: "Technetium", atomicN: 43 },
                Ru: { name: "Ruthenium", atomicN: 44 },
                Rh: { name: "Rhodium", atomicN: 45 },
                Pd: { name: "Palladium", atomicN: 46 },
                Ag: { name: "Silver", atomicN: 47 },
                Cd: { name: "Cadmium", atomicN: 48 },
                In: { name: "Indium", atomicN: 49 },
                Sn: { name: "Tin", atomicN: 50 },
                Sb: { name: "Antimony", atomicN: 51 },
                Te: { name: "Tellurium", atomicN: 52 },
                I: { name: "Iodine", atomicN: 53 },
                Xe: { name: "Xenon", atomicN: 54 },
                Cs: { name: "Cesium", atomicN: 55 },
                Ba: { name: "Barium", atomicN: 56 },
                La: { name: "Lanthanum", atomicN: 57 },
                Ce: { name: "Cerium", atomicN: 58 },
                Pr: { name: "Praseodymium", atomicN: 59 },
                Nd: { name: "Neodymium", atomicN: 60 },
                Pm: { name: "Promethium", atomicN: 61 },
                Sm: { name: "Samarium", atomicN: 62 },
                Eu: { name: "Europium", atomicN: 63 },
                Gd: { name: "Gadolinium", atomicN: 64 },
                Tb: { name: "Terbium", atomicN: 65 },
                Dy: { name: "Dysprosium", atomicN: 66 },
                Ho: { name: "Holmium", atomicN: 67 },
                Er: { name: "Erbium", atomicN: 68 },
                Tm: { name: "Thulium", atomicN: 69 },
                Yb: { name: "Ytterbium", atomicN: 70 },
                Lu: { name: "Lutetium", atomicN: 71 },
                Hf: { name: "Hafnium", atomicN: 72 },
                Ta: { name: "Tantalum", atomicN: 73 },
                W: { name: "Tungsten", atomicN: 74 },
                Re: { name: "Rhenium", atomicN: 75 },
                Os: { name: "Osmium", atomicN: 76 },
                Ir: { name: "Iridium", atomicN: 77 },
                Pt: { name: "Platinum", atomicN: 78 },
                Au: { name: "Gold", atomicN: 79 },
                Hg: { name: "Mercury", atomicN: 80 },
                Tl: { name: "Thallium", atomicN: 81 },
                Pb: { name: "Lead", atomicN: 82 },
                Bi: { name: "Bismuth", atomicN: 83 },
                Po: { name: "Polonium", atomicN: 84 },
                At: { name: "Astatine", atomicN: 85 },
                Rn: { name: "Radon", atomicN: 86 },
                Fr: { name: "Francium", atomicN: 87 },
                Ra: { name: "Radium", atomicN: 88 },
                Ac: { name: "Actinium", atomicN: 89 },
                Th: { name: "Thorium", atomicN: 90 },
                Pa: { name: "Protactinium", atomicN: 91 },
                U: { name: "Uranium", atomicN: 92 },
                Np: { name: "Neptunium", atomicN: 93 },
                Pu: { name: "Plutonium", atomicN: 94 },
                Am: { name: "Americium", atomicN: 95 },
                Cm: { name: "Curium", atomicN: 96 },
                Bk: { name: "Berkelium", atomicN: 97 },
                Cf: { name: "Californium", atomicN: 98 },
                Es: { name: "Einsteinium", atomicN: 99 },
                Fm: { name: "Fermium", atomicN: 100 },
                Md: { name: "Mendelevium", atomicN: 101 },
                No: { name: "Nobelium", atomicN: 102 },
                Lr: { name: "Lawrencium", atomicN: 103 },
                Rf: { name: "Rutherfordium", atomicN: 104 },
                Db: { name: "Dubnium", atomicN: 105 },
                Sg: { name: "Seaborgium", atomicN: 106 },
                Bh: { name: "Bohrium", atomicN: 107 },
                Hs: { name: "Hassium", atomicN: 108 },
                Mt: { name: "Meitnerium", atomicN: 109 },
                Ds: { name: "Darmstadtium", atomicN: 110 },
                Rg: { name: "Roentgenium", atomicN: 111 },
                Cn: { name: "Copernicium", atomicN: 112 },
                Nh: { name: "Nihonium", atomicN: 113 },
                Fl: { name: "Flerovium", atomicN: 114 },
                Mc: { name: "Moscovium", atomicN: 115 },
                Lv: { name: "Livermorium", atomicN: 116 },
                Ts: { name: "Tennessine", atomicN: 117 },
                Og: { name: "Oganesson", atomicN: 118 }
            };
            
        
            const elementInfo = periodicT[element];
            if (elementInfo) {
                return `Name: ${elementInfo.name}, Atomic Number: ${elementInfo.atomicN}`;
            }
            return "Element not found.";
        }
     function getTable(n){
        let table = [];
        for(let i = 1; i <= 10; i++){
            table.push(n * i);
        }
            return table;
        }
function getFactorial(n) {
    if (n === 0 || n === 1) return 1;
        return n * getFactorial(n - 1);
        }
        
function runCode() {
    const codeEditor = document.querySelector('.code-editor');
    const output = document.getElementById('output');

  
    const keywordMap = {
        'yap': 'console.log',
        'kick off': 'let',
        'ohhReally': 'if',
        'nahMan': 'else',
        'tellMe': 'prompt',
        'letHimCook': 'function',
        'LoopyLoopy': 'for',
        'solve': 'solve',
        'solve_quad' : 'solve_quad',
        'calculateResistance' : 'calculateResistance',
        'getElement': 'getElement',
        'getTable' : 'getTable',
        'getFactorial' : 'getFactorial'
    };

    let code = codeEditor.value;

    code = code.replace(/(["'`])(?:\\.|[^\1\\])*?\1|(\b(?:yap|kick off|ohhReally|nahMan|tellMe|letHimCook|LoopyLoopy)\b)/g, (match, quoted, keyword) => {
        if (quoted) {
            return match;
        } else if (keyword) {
            return keywordMap[keyword];
        }
        return match;
    });

    console.log("Transformed Code:", code);

    output.textContent = '';


    console.log = originalConsoleLog; 
    redirectConsole(output); 

    try {
        const result = eval(code);
        if (result !== undefined) {
            output.textContent += result;
        } else if (output.textContent.trim() === '') {
            output.textContent = "Code executed successfully.";
        }
    } catch (error) {
        output.textContent = "Error: " + error.message;
    }

    output.scrollIntoView({ behavior: 'smooth', block: 'start' });
}


window.solve = solve;
window.solve_quad = solve_quad;
window.calculateResistance = calculateResistance;
window.getElement = getElement;
window.getTable = getTable;
window.getFactorial = getFactorial;
