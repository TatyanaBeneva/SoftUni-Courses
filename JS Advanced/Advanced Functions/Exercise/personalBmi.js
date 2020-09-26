function solve(name, age, weight, heightCm){
    const output = {
        name,
        personalInfo: {
            age,
            weight,
            height: heightCm
        }
    }
    const heightInM = heightCm / 100;
    const bmi = Math.round(weight / (heightInM ** 2));
    output['BMI'] = bmi;
    let status = '';
    if(bmi < 18.5){
        status = 'underweight';
    } else if(bmi < 25){
        status = 'normal';
    } else if(bmi < 30){
        status = 'overweight';
    } else{
        status = 'obese';
        output.recommendation = 'admission required';
    }

    output['status'] = status;

    return output;
}

console.log(solve('Peter', 29, 75, 182));