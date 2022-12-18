import allure
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
from allure_commons.types import Severity


# 1 - Чистый selene


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("holder", "nvfedo")
@allure.feature("Поиск Issue в Github")
@allure.story("Поиск Issue в Github по названию 'Test issue'")
@allure.link("https://github.com/nvfedo/qa_guru_python_3_7/tree/main/tests", name="Link with tests")
def test_search_github_issue():
    browser.open('https://github.com/')
    browser.element('.header-search-input').type('nvfedo/qa_guru_python_3_7').press_enter()
    browser.element(by.link_text('nvfedo/qa_guru_python_3_7')).click()
    browser.element('#issues-tab').click()
    browser.element('#issue_1_link').should(have.exact_text('Test issue'))


# 2 - Лямбда шаги


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("holder", "nvfedo")
@allure.feature("Поиск Issue в Github")
@allure.story("Поиск Issue в Github по названию 'Test issue' с помощью шагов")
@allure.link("https://github.com/nvfedo/qa_guru_python_3_7/tree/main/tests", name="Link with tests")
def test_with_steps_search_github_issue():
    with allure.step('Открываем стартовую страницу Github'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').type('nvfedo/qa_guru_python_3_7').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('nvfedo/qa_guru_python_3_7')).click()

    with allure.step('Переходим на вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с определенным названием'):
        browser.element('#issue_1_link').should(have.exact_text('Test issue'))


# 3 - Шаги с декоратором


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("holder", "nvfedo")
@allure.feature("Поиск Issue в Github")
@allure.story("Поиск Issue в Github по названию 'Test issue' с помощью декоратора")
@allure.link("https://github.com/nvfedo/qa_guru_python_3_7/tree/main/tests", name="Link with tests")
def test_with_decorators_search_github_issue():
    open_github_main_page()
    search_repository('nvfedo/qa_guru_python_3_7')
    click_to_repostirory('nvfedo/qa_guru_python_3_7')
    open_issues_list()
    should_have_issue_with_name('Test issue')


@allure.step('Открываем стартовую страницу Github')
def open_github_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def search_repository(repository):
    browser.element('.header-search-input').type('nvfedo/qa_guru_python_3_7').press_enter()


@allure.step('Переходим по ссылке репозитория')
def click_to_repostirory(repository):
    browser.element(by.link_text('nvfedo/qa_guru_python_3_7')).click()


@allure.step('Переходим на вкладку Issues')
def open_issues_list():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue с определенным названием')
def should_have_issue_with_name(issue_name):
    browser.element('#issue_1_link').should(have.exact_text('Test issue'))
