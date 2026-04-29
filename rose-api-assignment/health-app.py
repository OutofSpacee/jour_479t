# load libraries
from flask import Flask, jsonify, request
import pandas as pd
import os

# start app
app = Flask(__name__)

# load the health data once when the app starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
health_data = pd.read_csv(os.path.join(BASE_DIR, 'data', 'U.S._Chronic_Disease_Indicators.csv'))

# clean column names by stripping white space
health_data.columns = [col.strip() for col in health_data.columns]


# defining a function that converts a dataframe into a list of JSON dictionaries
def rows_to_json(df):
    """Convert a dataframe to a list of dictionaries, handling NaN values."""
    return df.where(pd.notna(df), None).to_dict(orient='records')


def apply_location_filter(df, state):
    """Filter a dataframe by state abbreviation or location description."""
    state_value = state.strip().lower()
    location_abbr = df['LocationAbbr'].fillna('').str.lower()
    location_desc = df['LocationDesc'].fillna('').str.lower()
    return df[(location_abbr == state_value) | (location_desc == state_value)]


def apply_exact_text_filter(df, column, value):
    """Filter a dataframe with a case-insensitive exact text match."""
    return df[df[column].fillna('').str.lower() == value.strip().lower()]


@app.route('/')  # defines the URL endpoint: /
def index():
    return jsonify({
        # we can customize what is shown on this page. It will be shown as JSON, but
        # other API endpoints for landing pages might have fancier built-out pages to show information
        'description': 'CDC Chronic Disease Indicators API',
        'endpoints': [
            {
                'path': '/api/indicators',  # this links to /api/state
                'method': 'GET',
                'description': 'Return all indicators for a state in one year',
                'params': ['year_end', 'state', 'topic']
            },
            {
                'path': '/api/indicators/search',
                'method': 'GET',
                'description': 'Search by indicator topic. Returns all records with case-insensitive partial matches to the query.',
                'params': ['indicator topic (required)']
            },
            {
                'path': '/api/indicator/questions',
                'method': 'GET',
                'description': 'List all unique indicator questions.',
                'params': []
            },
            {
                'path': '/api/indicator/rank_of_state_by_topic',
                'method': 'GET',
                'description': 'Ranks states by topic data value.',
                'params': ['state', 'topic', 'question', 'year_end']
            },
        ]
    })


"""
Endpoint 1: GET /api/indicators
   Returns all records.
   Supports optional query parameters

   Examples of parameters:
     ?year_end=2020
     ?state=Maryland
     ?topic=Cancer
"""
@app.route('/api/indicators')
def get_indicators():
    df = health_data.copy()

    year_end = request.args.get('year_end', type=int)
    state = request.args.get('state')
    topic = request.args.get('topic')

    if year_end is not None:
        df = df[df['YearEnd'] == year_end]
    if state:
        df = apply_location_filter(df, state)
    if topic:
        df = apply_exact_text_filter(df, 'Topic', topic)
    # limit to 100 results to keep responses fast
    df = df.head(100)
    return jsonify({
        'count': len(df),
        'results': rows_to_json(df)
    })


"""
Endpoint 2: GET /api/indicators/search?topic=

Topic parameter is required.
Example: GET /api/indicators/search?topic=Cancer

Case-insensitive partial-match search on the "Topic" column.
"""
@app.route('/api/indicators/search')
def search_by_topic():
    topic = request.args.get('topic', '')

    if not topic:
        return jsonify({'error': 'Provide a ?topic= query parameter'}), 400

    df = health_data[health_data['Topic'].str.contains(topic, case=False, na=False)]
    # limit to 100 results to keep responses fast
    df = df.head(100)
    return jsonify({
        'count': len(df),
        'results': rows_to_json(df)
    })


"""
Endpoint 3: GET /api/indicator/questions
Returns a list of all unique questions in the dataset.
No parameters.
"""
@app.route('/api/indicator/questions')
def get_questions():
    questions = sorted(health_data['Question'].dropna().unique().tolist())
    return jsonify({'questions': questions})


"""
Endpoint 4: GET /api/indicator/rank_of_state_by_topic

Ranks a state within a filtered set of records.
Required parameters:
  state, topic, question, year_end
"""
@app.route('/api/indicator/rank_of_state_by_topic')
def rank_of_state_by_topic():
    state = request.args.get('state', '')
    topic = request.args.get('topic', '')
    question = request.args.get('question', '')
    year_end = request.args.get('year_end', type=int)

    if not state or not topic or not question or year_end is None:
        return jsonify({
            'error': 'Provide ?state=, ?topic=, ?question=, and ?year_end= query parameters'
        }), 400

    df = health_data.copy()
    df = df[df['YearEnd'] == year_end]
    df = apply_exact_text_filter(df, 'Topic', topic)
    df = apply_exact_text_filter(df, 'Question', question)
    df = df[df['DataValue'].notna()].copy()
    df = df.sort_values(['DataValue', 'LocationAbbr'], ascending=[False, True])
    df['Rank'] = df['DataValue'].rank(method='dense', ascending=False).astype(int)
    df = apply_location_filter(df, state)
    # limit to 100 results to keep responses fast
    df = df.head(100)

    return jsonify({
        'count': len(df),
        'results': rows_to_json(df)
    })


if __name__ == '__main__':
    # debug=True gives you auto-reload when you save the file
    # port=5000 tells Flask which port to run the server on
    # so you can access it at http://127.0.0.1:5000/
    app.run(debug=True, port=5000)