document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById('moodChart');
    if (!ctx) return;

    fetch('/api/mood/chart')
        .then(response => response.json())
        .then(data => {
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Mood Tracker',
                        data: data.values,
                        borderColor: '#8C52FF',
                        backgroundColor: 'rgba(140, 82, 255, 0.2)',
                        borderWidth: 3,
                        tension: 0.4, // Smooth curved line
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: {
                            min: 1,
                            max: 5,
                            ticks: {
                                stepSize: 1,
                                callback: function(value) {
                                    const emojis = {1: '😔', 2: '😕', 3: '😐', 4: '🙂', 5: '😄'};
                                    return emojis[value] || value;
                                }
                            }
                        }
                    }
                }
            });
        });
});
