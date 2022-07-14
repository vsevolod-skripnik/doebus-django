from django.db.models import F
from django.db.models import Sum

from app.base.services import BaseService
from products.models import Product


class ReportGenerator(BaseService):
    def __init__(self, report):
        self.report = report

    def get_annotated_products(self):
        return Product.objects \
            .filter() \
            .annotate(
                income=Sum(
                    (F('order_items__price') - F('order_items__cost'))
                    * F('order_items__amount'),
                ),
                revenue=Sum(F('order_items__price') * F('order_items__amount')),
                sold_count=Sum('order_items__amount'),
            )

    def get_report_data(self, products):
        return {
            product.id: {
                'income': float(product.income),
                'revenue': float(product.revenue),
                'sold_count': product.sold_count,
            }
            for product in products
        }

    def set_report_data(self, report_data):
        self.report.data = report_data
        self.report.save()
        return self.report

    def act(self):
        products = self.get_annotated_products()
        report_data = self.get_report_data(products)
        return self.set_report_data(report_data)
