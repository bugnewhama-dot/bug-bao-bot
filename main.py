from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home(): return "API Online"
@app.route('/info')
def info():
    return jsonify({"basicInfo":{"accountId":"9811998438","level":4,"liked":10270,"nickname":"XP OPU","region":"BD"},"clanBasicInfo":{"clanName":"TEAM XP"}})
if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)
