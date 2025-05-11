from flask import Blueprint, request, jsonify, current_app
import requests, base64

execute_bp = Blueprint('execute_bp', __name__)

@execute_bp.route('/', methods=['POST'])
def execute():
    data = request.get_json()
    src_b64 = base64.b64encode(data['source'].encode()).decode()
    payload = {
      'source_code': src_b64,
      'language_id': data['lang_id'],
      'stdin': base64.b64encode(data.get('stdin','').encode()).decode()
    }
    try:
        resp = requests.post(
            f"{current_app.config['JUDGE0_URL']}/submissions?base64_encoded=true&wait=true",
            json=payload,
            timeout=current_app.config['JUDGE0_TIMEOUT']
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        return jsonify(error=str(e)), 503

    result = resp.json()
    return jsonify({
      'stdout': base64.b64decode(result.get('stdout') or '').decode(),
      'stderr': base64.b64decode(result.get('stderr') or '').decode(),
      'compile_output': base64.b64decode(result.get('compile_output') or '').decode()
    })
