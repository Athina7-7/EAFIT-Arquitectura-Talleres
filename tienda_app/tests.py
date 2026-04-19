from unittest.mock import MagicMock, patch

from django.http import Http404
from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory

from tienda_app.api.views import CompraAPIView


class CompraAPIViewTests(SimpleTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('tienda_app.api.views.PaymentFactory.get_processor')
    @patch('tienda_app.api.views.CompraService.ejecutar_compra')
    def test_retorna_404_si_falta_libro_o_inventario(
        self,
        mock_ejecutar_compra,
        mock_get_processor,
    ):
        mock_get_processor.return_value = MagicMock()
        mock_ejecutar_compra.side_effect = Http404()

        request = self.factory.post(
            '/api/v1/comprar/',
            {
                'libro_id': 1,
                'direccion_envio': 'Calle 123',
                'cantidad': 1,
            },
            format='json',
        )

        response = CompraAPIView.as_view()(request)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {'error': 'Libro o inventario no encontrado.'})
