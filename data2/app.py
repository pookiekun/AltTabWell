# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Sample data, identical to the one in your React component
sample_activities = [
    {
      "id": 12345678987654321,
      "athlete": { "id": 134815, "name": "Niyati " },
      "name": "Happy Friday",
      "distance": 28099,
      "moving_time": 4207,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 6.679,
      "max_speed": 18.5,
      "average_watts": 185.5,
      "max_watts": 743,
      "total_elevation_gain": 516,
      "calories": 870.2,
      "kudos_count": 19,
      "start_date": "2018-02-16T14:52:54Z"
    },
    {
      "id": 12345678987654322,
      "athlete": { "id": 134816, "name": "Rakshita K." },
      "name": "Morning Climb",
      "distance": 32500,
      "moving_time": 3890,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 8.35,
      "max_speed": 22.1,
      "average_watts": 210.3,
      "max_watts": 890,
      "total_elevation_gain": 720,
      "calories": 1050.8,
      "kudos_count": 25,
      "start_date": "2018-02-16T15:30:12Z"
    },
    {
      "id": 12345678987654323,
      "athlete": { "id": 134817, "name": "Vishal R." },
      "name": "Epic Trail Ride",
      "distance": 41200,
      "moving_time": 5120,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 8.05,
      "max_speed": 25.8,
      "average_watts": 195.7,
      "max_watts": 820,
      "total_elevation_gain": 980,
      "calories": 1340.5,
      "kudos_count": 32,
      "start_date": "2018-02-17T08:15:30Z"
    },
    {
      "id": 12345678987654324,
      "athlete": { "id": 134818, "name": "Preethi L." },
      "name": "Speed Session",
      "distance": 25600,
      "moving_time": 3200,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 8.0,
      "max_speed": 28.4,
      "average_watts": 220.1,
      "max_watts": 950,
      "total_elevation_gain": 320,
      "calories": 780.3,
      "kudos_count": 18,
      "start_date": "2018-02-17T16:45:20Z"
    },
    {
      "id": 12345678987654325,
      "athlete": { "id": 134819, "name": "Niyati B." },
      "name": "Endurance Challenge",
      "distance": 55800,
      "moving_time": 7890,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 7.07,
      "max_speed": 19.3,
      "average_watts": 175.8,
      "max_watts": 680,
      "total_elevation_gain": 1250,
      "calories": 1890.7,
      "kudos_count": 45,
      "start_date": "2018-02-18T07:00:00Z"
    },
    {
      "id": 12345678987654326,
      "athlete": { "id": 134820, "name": "Pujita P." },
      "name": "Quick Ride",
      "distance": 18900,
      "moving_time": 2340,
      "type": "Ride",
      "sport_type": "MountainBikeRide",
      "average_speed": 8.08,
      "max_speed": 24.7,
      "average_watts": 205.4,
      "max_watts": 780,
      "total_elevation_gain": 290,
      "calories": 620.1,
      "kudos_count": 12,
      "start_date": "2018-02-18T12:30:15Z"
    }
]

@app.route('/')
def dashboard():
    # --- Data Processing ---

    # Helper function to get leaderboard for a specific metric
    def get_leaderboard(metric, limit=5):
        return sorted(sample_activities, key=lambda x: x.get(metric, 0), reverse=True)[:limit]

    # Calculate leaderboards
    distance_leaders = get_leaderboard('distance')
    speed_leaders = get_leaderboard('average_speed')
    power_leaders = get_leaderboard('average_watts')
    elevation_leaders = get_leaderboard('total_elevation_gain')
    kudos_leaders = get_leaderboard('kudos_count')

    # Calculate total stats
    total_stats = {
        "activities": len(sample_activities),
        "distance": round(sum(a['distance'] for a in sample_activities) / 1000),
        "time": round(sum(a['moving_time'] for a in sample_activities) / 3600),
        "kudos": sum(a['kudos_count'] for a in sample_activities)
    }

    # Prepare data for Chart.js
    chart_data = {
        "distance": {
            "labels": [a['athlete']['name'] for a in distance_leaders],
            "values": [round(a['distance'] / 1000, 1) for a in distance_leaders]
        },
        "speed": {
            "labels": [a['athlete']['name'] for a in speed_leaders],
            "values": [round(a['average_speed'], 1) for a in speed_leaders]
        },
        "power": {
            "labels": [a['athlete']['name'] for a in power_leaders],
            "values": [round(a['average_watts']) for a in power_leaders]
        },
        "elevation": {
            "labels": [a['athlete']['name'] for a in elevation_leaders],
            "values": [a['total_elevation_gain'] for a in elevation_leaders]
        }
    }

    return render_template(
        'index.html',
        total_stats=total_stats,
        distance_leaders=distance_leaders,
        speed_leaders=speed_leaders,
        power_leaders=power_leaders,
        elevation_leaders=elevation_leaders,
        kudos_leaders=kudos_leaders,
        chart_data=chart_data
    )

if __name__ == '__main__':
    app.run(debug=True)