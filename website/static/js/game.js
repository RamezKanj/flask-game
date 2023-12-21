function updateContent() {

    $.get('/get_random_data', function(data) {
        $('#random_value').text(data.random_value)

        var answers = [data.random_key, data.incorrect_key_one, data.incorrect_key_two]
        
        for (let i = answers.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1))

            [answers[i], answers[j]] = [answers[j], answers[i]]
        }

        $('#random_key').text(answers[0])
        $('#incorrect_key_one').text(answers[1])
        $('#incorrect_key_two').text(answers[2])

    })
}

$('#random_key, #incorrect_key_one, #incorrect_key_two').on('click', function() {
    updateContent()
});