var score = 0;
var data = {};  // Declare data globally

function updateContent() {
    $.get('/get_random_data', function(responseData) {
        data = responseData;  // Update the global data variable
        $('#random_value').text(data.random_value);

        var answers = [data.random_key, data.incorrect_key_one, data.incorrect_key_two];

        for (let i = answers.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1));

            // Swap array[i] and array[j]
            [answers[i], answers[j]] = [answers[j], answers[i]];
        }

        $('#random_key').text(answers[0]);
        $('#incorrect_key_one').text(answers[1]);
        $('#incorrect_key_two').text(answers[2]);
    });
}

// Event handler for all answer buttons
$('#random_key, #incorrect_key_one, #incorrect_key_two').on('click', function() {
    var selectedAnswer = $(this).text();
    updateContent();  // Fetch new data

    // Check if the selected answer is correct
    if (selectedAnswer === data.random_key) {
        score = score + 1;
    } else {
        if (score > 0) {
            score = score - 1;
        }
    }

    $('#score').text(score);
});


updateContent();


var timerValue = 30
var time_control = timerValue

var countdownTimer

function increaseTimer(){
    timerValue = 60
    time_control = timerValue
    $('#timer').text(timerValue)
}

function decreaseTimer(){
    timerValue = 30
    time_control = timerValue
    $('#timer').text(timerValue)
}

$('#timerSecondButton').on('click', function(){
    increaseTimer()
})

$('#timerFirstButton').on('click', function(){
    decreaseTimer()
})

var initialTimerValue = parseInt($('#timer').text())


function updateLeaderboard() {
    $.get('/get_leaderboard', function(response) {
        // Clear existing leaderboard entries
        $('#leaderboard-list-30').empty();
        $('#leaderboard-list-60').empty();

        // Populate the 30-second leaderboard
        response.leaderboard_30.forEach(entry => {
            $('#leaderboard-list-30').append(`<li>${entry.name}: ${entry.score}</li>`);
        });

        // Populate the 60-second leaderboard
        response.leaderboard_60.forEach(entry => {
            $('#leaderboard-list-60').append(`<li>${entry.name}: ${entry.score}</li>`);
        });
    });
}



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

                $.post('/update_score', { score: score, time_control: time_control}, function(response) {
                    if (response.success) {
                        updateLeaderboard();
                        console.log('Score updated successfully');
                    } else {
                        console.error('Failed to update score:', response.error);
                    }
                })

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

        score = 0
        $('#score').text(score)

    }
}


$('#startButton').on('click', function(){
    toggleStart()
})



updateLeaderboard();