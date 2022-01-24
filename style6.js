function checkWinner(val1, val2, val3, val4, val5, val6) {
    const Nets = (val1 + val2 + val3) / 3;
    const Knicks = (val4 + val5 + val6) / 3;

    if (Nets > Knicks && Nets >= 100) {
        console.log(`Nets wins the trophy`);
        alert(`Nets wins the trophy`);
    }
    else if (Knicks > Nets && Knicks >= 100) {

        console.log("Knicks wins the trophy");
        alert("Knicks wins the trophy");
    }

    else if (Nets === Knicks && Nets >= 100 || Knicks >= 100) {
        console.log('The game is a Draw');
        alert('The game is a Draw');
    }

    else {

        console.log("No team wins");
        alert("No team wins");
    }

}

checkWinner(80, 82, 100, 80, 90, 106);
checkWinner(98, 110, 101, 108, 92, 110);




function tipCal(bill) {

    switch (bill) {
        case bill <= 100:
        case bill >= 30:
            tip = 0.15 * bill;
            alert(`The bill was ${bill}, the tip was ${tip}, and the total value ${tip + bill}`);
            console.log(`The bill was ${bill}, the tip was ${tip}, and the total value ${tip + bill}`);

            break;

        default:
            tip = 0.20 * bill;
            alert(`The bill was ${bill}, the tip was ${tip}, and the total value ${tip + bill}`);
            console.log(`The bill was ${bill}, the tip was ${tip}, and the total value ${tip + bill}`);
            break;
    }


}


tipCal(285);
tipCal(26);
tipCal(90);





function CovertCelsiusToFahrenheit(celsius) {
    fahrenheit = (celsius * 9 / 5) + 32;
    console.log(`${celsius}°C is ${fahrenheit}°F"`);
    alert(`${celsius}°C is ${fahrenheit}°F"`);

}

CovertCelsiusToFahrenheit(100);
CovertCelsiusToFahrenheit(0);
CovertCelsiusToFahrenheit(10);

function CovertFahrenheitToCelsius(fahrenheit) {

    celcius = (fahrenheit - 32) * (5 / 9);
    console.log(`${fahrenheit}°F is ${celcius}°C"`);
    alert(`${fahrenheit}°F is ${celcius}°C"`);

}

CovertFahrenheitToCelsius(32);
CovertFahrenheitToCelsius(10);
CovertFahrenheitToCelsius(102);