from decimal import Decimal
import pytest

from reports.models import Report
from reports.services import ReportGenerator

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def order_item(factory, product, order):
    return factory.order_item(
        order=order,
        product=product,
        amount=10,
        price=Decimal('2499.99'),
        cost=Decimal('1499.99'),
    )


def test_report_generator_get_annotated_products(order_item, report):
    report_generator = ReportGenerator(report)

    products = report_generator.get_annotated_products()

    assert products[0].income == Decimal('10000.00')
    assert products[0].revenue == Decimal('24999.9')
    assert products[0].sold_count == 10


def test_report_generator_get_report_data(product, order_item, report):
    report_generator = ReportGenerator(report)
    products = report_generator.get_annotated_products()

    report_data = report_generator.get_report_data(products)

    assert report_data == {
        product.id: {
            'income': 10000.00,
            'revenue': 24999.9,
            'sold_count': 10,
        },
    }


def test_report_generator_set_report_data(report):
    report_generator = ReportGenerator(report)

    report_generator.set_report_data({'foo': 'bar'})

    report = Report.objects.get(id=report.id)
    assert report.data == {'foo': 'bar'}


def test_report_generator(product, order_item, report):
    report_generator = ReportGenerator(report)

    report = report_generator()

    assert report.data == {
        product.id: {
            'income': 10000.00,
            'revenue': 24999.9,
            'sold_count': 10,
        },
    }
