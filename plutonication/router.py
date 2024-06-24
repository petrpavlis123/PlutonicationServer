from flask import render_template, request
from .dapp_icons import app
from .authentication import auth
import os


@app.route("/")
@app.route("/docs")
def main_page():
    return render_template("main_page.html")


@app.route("/docs/flask-server")
def flask_server_docs_page():
    return render_template("flask_server_docs_page.html")


@app.route("/docs/javascript")
def plutonication_javascript_page():
    return render_template("plutonication_javascript_page.html")


@app.route("/docs/react-example")
def plutonication_react_example_page():
    return render_template("plutonication_react_example_page.html")


@app.route("/docs/csharp")
def plutonication_csharp_page():
    return render_template("plutonication_csharp_page.html")


@app.route("/digital_ocean_deploy_guide")
@app.route("/deploy")
@app.route("/deploy/flask")
@app.route("/deploy/flask-digital-ocean")
def digital_ocean_deployment_page():
    return render_template("digital_ocean_deployment_page.html")


# Pluto wallet part
@app.route("/plutowallet/latest-version")
def get_plutowallet_latest_version():
    return {
        "message": "",
        "versionString": "1.10",
        "version": 11,
    }


# Galaxy Logic Game part
@app.route("/glg/validate-game", methods=["POST"])
def validate_game():
    file = open("games.txt", "a")

    file.write(str(request.data))
    file.write(",\n")

    file.close()

    return "Ok"


@app.route("/glg/get-validated-games/<password>")
def get_validated_games(password):
    if not auth(password):
        return "Bad password"

    file_name = "games.txt"

    if not os.path.exists(file_name):
        return "No games registered"
    
    file = open(file_name, "r")
    
    validatedGames = file.read()

    file.close()

    return validatedGames


@app.route("/glg/delete-validated-games/<password>")
def delete_validated_games(password):
    if not auth(password):
        return "Bad password"

    # Specify the file name
    file_name = "games.txt"

    # Check if the file exists to avoid an error
    if os.path.exists(file_name):
        os.remove(file_name)
        return "Removed successfully"
    
    return "File did not exist"


@app.route("/supported-wallets")
def get_supported_wallets():
    return [
        {
            "name": "PlutoWallet",
            "icon": "https://rostislavlitovkin.pythonanywhere.com/plutowalleticonwhite",
            "downloadAndroid": "https://play.google.com/store/apps/details?id=com.rostislavlitovkin.plutowallet",
            "downloadIOS": None,
            "github": "https://github.com/rostislavLitovkin/plutowallet",
            "description": "",
        },
        {
            "name": "Other test wallet",
            "icon": "https://rostislavlitovkin.pythonanywhere.com/image",
            "downloadAndroid": None,
            "downloadIOS": None,
            "github": "https://github.com/rostislavLitovkin/Nothing",
            "description": "Test description",
        }
    ]


@app.route("/plutowallet/terms-and-conditions")
def pluto_wallet_terms_and_conditions_page():
    return render_template("pluto_wallet_terms_and_conditions_page.html")
