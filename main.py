# class note sited from Prof. Eric Charnesky at:
# https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Week2/main.py
class SprayBottle:

    def __init__(self, max_volume_in_milliliters ):
        self._current_volume_in_milliliters = 0
        self._max_volume_in_milliliters = max_volume_in_milliliters

    def get_current_volume_in_milliliters(self):
        return self._current_volume_in_milliliters

    def get_max_volume_in_milliliters(self):
        return self._max_volume_in_milliliters

    def add_liquid(self, milliliters_to_add):
        if milliliters_to_add > 0:
            self._current_volume_in_milliliters += milliliters_to_add

            if self._current_volume_in_milliliters > self._max_volume_in_milliliters:
                self._current_volume_in_milliliters = self._max_volume_in_milliliters
                return False # overfilled
            return True # filled OK
        return False # can't add negative

    def spray(self, amount_to_spray = 10):

        if amount_to_spray > 0:
            self._current_volume_in_milliliters -= amount_to_spray

            if self._current_volume_in_milliliters < 0:
                self._current_volume_in_milliliters = 0
                return False # invalid state

            return True # everything ok

        return False # invalid amount



# hides the code so it only runs when you directly run this file
if __name__ == '__main__':
    bleach = SprayBottle(1000)

    amount_to_add = int(input('How much should we add in milliliters'))
    result = bleach.add_liquid(amount_to_add)

    if result:
        print('You added bleach, good job')
    else:
        print("it didn't work")


    result = bleach.spray()

    while result:
        print('you sprayed some bleach')
        result = bleach.spray()
    print("the bottle is empty")