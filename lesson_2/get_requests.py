from flask import Flask, request
from typing import List, Optional

app = Flask(__name__)


@app.route('/seach/', methods= ['GET'])
def search():

    cell_tower_ids: List[int] = request.args.getlist('cell_tower_id', type=int)

    if not cell_tower_ids:
        return f'You must specify at list one cell_tower_id', 400

    phone_prefix: List[str] = request.args.getlist('phone_prefix')

    protocols: List[str] = request.args.getlist('protocol')

    signal_level: Optional[float] = request.args.get('signal_level', type=float, default=None)


    return (
        f'Seach for {cell_tower_ids} cell tower. Seach criteria: '
        f'phone_prefix = {phone_prefix}'
        f'protocols = {protocols}, '
        f'signal_level = {signal_level}'
    )

if __name__ == '__main__':
    app.run(debug=True)