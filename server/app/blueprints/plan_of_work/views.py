from flask import(
    Blueprint,
    request,
    url_for,
    jsonify
)
# Models
from app.blueprints.plan_of_work.models import (
        PlanOfWork,
        CriticalIssue
)

plans = Blueprint('plan_of_work', __name__)

@plans.route('/plans')
def show_plans():
    pows = PlanOfWork.query.all()
    return jsonify([ p.serialize for p in pows])


@plans.route('/plans/<int:plan_id>')
def show_single_plan(plan_id):
    pow = PlanOfWork.query.filter_by(id=plan_id).first()
    return jsonify( pow.serialize )


@plans.route('/plans/<int:id>/edit', methods=['POST'])
def edit_plan(id):
    return f"Edit plan with id {id}"


@plans.route('/plans/<int:id>/delete')
def delete_plan(id):
    return f"Delete plan with id {id}"

