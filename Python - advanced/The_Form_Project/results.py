from flask import Blueprint, render_template, session, redirect, request
from log import add_log
from definitions_of_results import id_question_which_answer, answers_of_question, count_answers, percentage_share, verify_questions_without_answer, add_to_results_questions_without_answer

form_results = Blueprint('/wyniki', __name__)


@form_results.route('/wyniki', methods=['GET', 'POST', 'HEAD'])
def results():
    log = add_log()
    if not session:
        log.warning('Brak sesji')

        return redirect('/login')

    if request.method == 'GET':

        if session['is_admin'] == False:
            user = session['user']

            log.warning(f'Użytkowanik {user} próbował się dostać do bazy wyników')

            return redirect('ankieta')

        id_question_which_answer()

        group_by_list_of_answers = []
        for id in id_question_which_answer():
            id = id[0]
            answers = answers_of_question(id)
            result = count_answers(answers)
            group_by_list_of_answers.append(result)

        results = []
        for i in group_by_list_of_answers:
            result = percentage_share(i)
            results.append(result)

        verify_questions_without_answer()

        no_answers_results = add_to_results_questions_without_answer()
        for element in no_answers_results:
            results.append(element)
        # print('add: ', results)

        context = {'results': results}

        log.info(f'Wszytskie results obliczeń: {results}')
        return render_template('results.html', **context)
