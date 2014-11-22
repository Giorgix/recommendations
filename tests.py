import recommendations
import unittest

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0},
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5},
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0},
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5},
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0},
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5},
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0}}


class TestRecommendations(unittest.TestCase):
    def setUp(self):
        self.item_sim = recommendations.calculateSimilarItems(critics)

    def test_pearson_formula(self):
        self.assertAlmostEqual(
            recommendations.similarity_pearson(
                critics, 'Lisa Rose', 'Gene Seymour'), 0.396059017191, 5)

    def test_topMatches_result(self):
        self.assertAlmostEqual(recommendations.topMatches(critics, 'Toby', n=3),
                               [(0.99124070716192991, 'Lisa Rose'),
                                (0.92447345164190486, 'Mick LaSalle'),
                                (0.89340514744156474, 'Claudia Puig')], 5)

    def test_getRecommendations_result(self):
        self.assertAlmostEqual(recommendations.getRecommendations(critics, 'Toby'),
                               [(3.3477895267131013, 'The Night Listener'),
                                (2.8325499182641614, 'Lady in the Water'),
                                (2.5309807037655645, 'Just My Luck')], 5)

    def test_getRecommendedItems(self):
        self.assertAlmostEqual(recommendations.getRecommendedItems(critics, self.item_sim, 'Toby'),
                               [(3.182634730538922, 'The Night Listener'),
                                (2.5983318700614575, 'Just My Luck'),
                                (2.4730878186968837, 'Lady in the Water')], 5)
if __name__ == '__main__':
    unittest.main()
