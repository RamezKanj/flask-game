
var timerValue = 30

var countdownTimer

function increaseTimer(){
    timerValue = 60
    $('#timer').text(timerValue)
}

function decreaseTimer(){
    timerValue = 30
    $('#timer').text(timerValue)
}

$('#timerSecondButton').on('click', function(){
    increaseTimer()
})

$('#timerFirstButton').on('click', function(){
    decreaseTimer()
})

var initialTimerValue = parseInt($('#timer').text())

console.log(initialTimerValue)

function toggleStart(){
    if ($('#startButton').text() === 'START'){

        document.getElementById("random_key").removeAttribute("disabled");
        document.getElementById("incorrect_key_one").removeAttribute("disabled");
        document.getElementById("incorrect_key_two").removeAttribute("disabled");
        document.getElementById("timerFirstButton").setAttribute("disabled", "true");
        document.getElementById("timerSecondButton").setAttribute("disabled", "true");
        
        $('#startButton').text('STOP')

        countdownTimer = setInterval(function() {
            timerValue--;
            $('#timer').text(timerValue);

            if (timerValue === 0) {
                toggleStart()
            }
        }, 1000)

    }else{
        document.getElementById("random_key").setAttribute("disabled", "true");
        document.getElementById("incorrect_key_one").setAttribute("disabled", "true");
        document.getElementById("incorrect_key_two").setAttribute("disabled", "true");
        document.getElementById("timerFirstButton").removeAttribute("disabled");
        document.getElementById("timerSecondButton").removeAttribute("disabled");

        $('#startButton').text('START')

        timerValue = initialTimerValue
        $('#timer').text(timerValue)
        clearInterval(countdownTimer)
    }
}


$('#startButton').on('click', function(){
    toggleStart()
})

