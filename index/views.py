from django.utils import html
from django.views.generic import TemplateView


class IndexHTML(TemplateView):
    template_name = "index.html"
    extra_context = {
        "FIO": "Дорохин Степан Геннадьевич",
        "nickname": "@bfswrd",
        "about": html.format_html("""                
                <h2 class="text-center">About me</h2>
                <div class="text-end">
                    <p class="lead mb-0">Я родился в Ельце.</p>
                    <p class="lead mb-0">В 2005 на краю города.</p>
                    <p class="lead mb-3">Что-то рано ударило в голову.</p>
                </div>
                <p class="mb-0 fs-5">Всем привет! Немножко о себе? 17 лет. Не пью. Не курю.
                    Ладно, в сторону лирику!<br>
                    Первое мое знакомство с программированием состоялось в школе (Спасибо Янедкс.Лицею). Было это года 3
                    назад. С того момента я значительно прокачался и, о чудо, начал зарабатывать первые 
                    деньги на фрилансе. Последние
                    два месяца я разрабатываю Крипто-обменник в телеграмме. За эти три года, я узнал много нового,
                    участвовал и побеждал в олимпиадах, освоил несколько языков помимо Python (C++, Js, HTML, CSS, SQL),
                     прокачал
                    много других Soft skills и подтянул английский. Сейчас я учусь в университете ЕГУ им. Бунина,
                     Институт "СПО"
                     по направлению - веб-дизайн. Я
                    осознано не пошел в 11 класс, т.к. понимал, что терять еще два года в школе я не хочу. За это время
                    я лучше подтяну базу, но все же высшее образование я получать планирую. <br>
                    Последний год, в свободное время занимаюсь в секции лыжных гонок. Хоть как то приходится шевелиться
                     и не
                    превращаться в стереотипного хики-прогера. И на удивление, я
                    получаю медали на соревнованиях. Хотя соревноваться мне приходится с Ребятами, которые посвятили
                    спорту большую часть своей жизни.
                </p>"""),
        "telegram": "https://t.me/bfswrd",
        "github": "https://github.com/bfswrd"
    }
