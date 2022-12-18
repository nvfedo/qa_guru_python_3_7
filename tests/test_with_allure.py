import allure
import json
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure import attachment_type

#Степы
def test_dynamic_search_github_issue():
    with allure.step("Открываем стартовую страницу"):
        browser.open('https://github.com/')

        #
        # browser.driver.maximize_window()
        # browser.config.hold_browser_open = True

    with allure.step("Ищем репозиторий"):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issues #81"):
        browser.element(by.partial_text('#81')).should(be.visible)
    # browser.config.quit_driver()

#Декоратор
def test_decorator_search_github_issue():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repostirory("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_nubmer("81")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com/')


@allure.step("Ищем репозиторий")
def search_for_repository(repo):
    browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()


@allure.step("Переходим по ссылке репозитория")
def go_to_repostirory(repo):
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step("Переходим по ссылке репозитория")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем наличие Issues #81")
def should_see_issue_with_nubmer(number):
    browser.element(by.partial_text('#81')).should(be.visible)

# Аттачи
def test_attachments():
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world!<h1>", name="HTML", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="JSON", attachment_type=attachment_type.JSON)
