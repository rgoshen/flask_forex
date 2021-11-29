from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False


class ConverterViewsTestCase(TestCase):

    def test_redirect_to_form(self):
        with app.test_client() as client:
            res = client.get('/')

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/convert')

    def test_redirect_to_form_followed(self):
        with app.test_client() as client:
            res = client.get('/', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<form id="conversion-form"', html)

    def test_show_conversion_form(self):
        with app.test_client() as client:
            res = client.get('/convert')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<form id="conversion-form"', html)

    def test_show_results(self):
        with app.test_client() as client:
            res = client.get('/results?sym=US%24&total=1.00')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('US$ 1.00', html)
