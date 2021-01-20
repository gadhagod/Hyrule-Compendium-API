base="http://botw-compendium.herokuapp.com/api/v1"

function fail {
    echo "ERROR: Endpoint \"$1\" returned a non-200 code"
    exit 1
}

function test_endpoint {
    if [[ $1 = "" ]]; then
        speaker_endpoint="/"
    else
        speaker_endpoint=$1
    fi
    curl -f -s -I "$base$1" &>/dev/null && echo "Tested endpoint \"$speaker_endpoint\" successfuly" || fail $speaker_endpoint
}