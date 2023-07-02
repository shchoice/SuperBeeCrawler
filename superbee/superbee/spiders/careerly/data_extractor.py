from time import sleep

from selenium.common import NoSuchElementException

from superbee.superbee.mariadb.db_manager import Session, CareerlyPosts


def get_data(driver):
    session = Session()
    posts = driver.find_elements('xpath', '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div/div')

    for i, post in enumerate(posts):
        xpath_base = f'//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div/div[{i + 1}]'

        author = workplace = text = url = ""

        try :
            more_button = post.find_element('xpath', xpath_base + '/div/div[2]/div/p/span/span')
            more_button.click()
        except NoSuchElementException:
            pass

        sleep(1)

        try:
            author = post.find_element('xpath', xpath_base + '/div/div[1]/a/div[2]/p[1]').text
            workplace = post.find_element('xpath', xpath_base + '/div/div[1]/a/div[2]/p[2]/span').text
            title = post.find_element('xpath', xpath_base + '/div/div[2]/p').text
            text = post.find_element('xpath', xpath_base + '/div/div[2]/div/p').text.replace('\n\n', '\n')
            url = post.find_element('xpath', xpath_base + '/div/div[3]/a').get_attribute('href')
        except NoSuchElementException:
            pass

        existing_post = session.query(CareerlyPosts).filter_by(author=author, workplace=workplace, title=title).first()
        if existing_post is None:
            post = CareerlyPosts(author=author, workplace=workplace, title=title, text=text, url=url)
            session.add(post)
            session.commit()
        else:
            print("Post already exists in the database")

    session.close()

