let lucasHeight = 1.69;
let lucasMass = 78;
let johnMass = 92;
let johnHeight = 1.95;
let BMILucas = lucasMass / lucasHeight ** 2;
let BMIJohn = johnMass / (johnHeight * johnHeight);
console.log(BMILucas);
console.log(BMIJohn);
let lucasHigherBMI = BMILucas > BMIJohn;
console.log(lucasHigherBMI);

if (BMILucas > BMIJohn) {
    console.log("Lucas BMI is higher than John's!")
    console.log(`Lucas BMI ${BMILucas} is higher than John ${BMIJohn}!`)
}
else {
    console.log("John's BMI is higher than Lucas");
    console.log(`John's BMI ${BMIJohn} is higher than Lucas ${BMILucas}!`)

}