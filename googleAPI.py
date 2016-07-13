from googleplaces import GooglePlaces, types, lang
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        city = request.form['city']
        type = request.form['type']

        GOOGLE_API_KEY = "AIzaSyBCsZBILrxQqRNd2Aji_abzot_15Rm9dIY"

        google_instance = GooglePlaces(GOOGLE_API_KEY)

        query_result = google_instance.nearby_search(
                location=city, keyword=type,
                radius=20000, types=[types.TYPE_FOOD])

        if query_result.has_attributions:
            print (query_result.html_attributions)

        query_result.places[0].get_details()
        address = query_result.places[0].formatted_address
    
        return render_template("results.html", name = query_result.places[0].name, name2 = address)
    else:
        return "Try again from the homepage"


if (__name__ == "__main__"):
    app.run()