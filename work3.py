from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def stat():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Колонизация</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align=center>Анкета претендента</h1>
                            <h2 align=center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name"><br />
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div> <br />
                                    <label for="classSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input id="op1" type="checkbox" name="color"/>
                                        <label for="op1">Инженер-исследователь</label> <br />
                                        <input id="op2" type="checkbox" name="color"/> 
                                        <label for="op2">Инженер-строитель</label> <br />
                                        <input id="op3" type="checkbox" name="color"/>
                                        <label for="op3">Пилот</label> <br />
                                        <input id="op4" type="checkbox" name="color"/>
                                        <label for="op4">Метеоролог</label> <br />
                                        <input id="op5" type="checkbox" name="color"/>
                                        <label for="op5">Инженер по жизнеобеспечению</label> <br />
                                        <input id="op6" type="checkbox" name="color"/>
                                        <label for="op6">Инженер по радиационной защите</label> <br />
                                        <input id="op7" type="checkbox" name="color"/>
                                        <label for="op7">Врач</label> <br />
                                        <input id="op8" type="checkbox" name="color"/>
                                        <label for="op8">Экзобиолог</label>
                                    </div> <br />
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div> <br />
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div> <br />
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div> <br />
                                    <div class="form-group">
                                        <input id="my_check" type="checkbox" name="color"/>
                                        <label for="my_check">Готовы остаться на Марсе?</label>
                                    </div> <br />
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>', methods=['POST', 'GET'])
def planets(planet_name):
    planets = {'Меркурий': ['Самая близкая к солнцу планета',
                            'На дневной стороне температура поднимается до +400 градусов',
                            'На ночной стороне температура доходит до -200 градусов',
                            'У планеты нет спутников',
                            'В римской мифологии - бог торговли'],
               'Венера': ['Она проходит к Земле ближе, чем какая-либо другая планета',
                          'Давление на поверхности около 107 Па',
                          'Найти её на небе проще, чем любую другую планету',
                          'У планеты нет спутников',
                          'Поверхностные породы Венеры близки по составу к земным осадочным породам'],
               'Земля': ['У Земли есть естественный спутник - Луна',
                         'Земля обладает магнитным и электрическим полями',
                         'Жизнь на Земле крайне разнообразна — животные, птицы, рыбы, растения',
                         'На Земле есть океаны, моря, реки — вода',
                         'Диаметр Земли составляет 12 742 км'],
               'Марс': ['Эта планета близка к Земле',
                        'На ней много необходимых ресурсов',
                        'На ней есть вода и атмосфера',
                        'На ней есть небольшое магнитное поле',
                        'Наконец, она просто красива!'],
               'Юпитер': ['Эта планета является самой большой в Солнечной системе',
                          'Сутки на Юпитере длятся 10 часов, а год равен приблизительно 12 земным годам',
                          'Средняя температура на планете составляет -150 градусов Цельсия',
                          'Юпитер имеет огромное количество спутников - 67',
                          'Юпитер в основном состоит из ксенона, аргона и криптона'],
               'Сатурн': ['Эта планета вторая по размерам в Солнечной системе',
                          'Она наиболее схожа по своему составу с Солнцем',
                          'Сатурн уникален тем, что имеет 65 спутников и несколько колец',
                          'Кольца состоят из маленьких частиц льда и каменистых образований',
                          'В ее верхних слоях часто возникают грозы и полярные сияния'],
               'Уран': ['Уран является третьей по размеру планетой в солнечной системе и седьмой по счету от Солнца',
                        'Температура на его поверхности составляет -224 градусов',
                        'Сутки на Уране длятся 17 часов, а год - 84 земных года',
                        'У Урана есть 27 спутников',
                        'Он имеет диаметр 50 724 км'],
               'Нептун': ['Нептун - восьмая планета от Солнца',
                          'По своему составу и размерам он схож со своим соседом Ураном',
                          'Диаметр этой планеты составляет 49 244 км',
                          'Нептун также имеет кольца. У этой планеты их 6',
                          'Сутки на Нептуне длятся 16 часов, а год равен 164 земным годам'],
               'Other': ['Эта планета находится вне Солнечной системы',
                         'Данные отсутвуют',
                         'Данные отсутвуют',
                         'Данные отсутвуют',
                         'Данные отсутвуют']
               }
    planet = planet_name
    if planet_name not in planets.keys():
        planet_name = 'Other'
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <link rel="stylesheet" href="static/css/style.css">
                        <title>Варианты выбора</title>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                      </head>
                      <body>
                        <h1>Моё предложение: {planet}</h1>
                        <h2>{planets[planet_name][0]}</h2>
                        <div class="alert alert-dark" role="alert">
                          {planets[planet_name][1]}
                        </div>
                        <div class="alert alert-success" role="alert">
                          {planets[planet_name][2]}
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          {planets[planet_name][3]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                          {planets[planet_name][4]}
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
