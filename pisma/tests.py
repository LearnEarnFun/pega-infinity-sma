from typing import List

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from pisma.models import PegaNode
from pisma.views.services import get_default_context


def populate_nodes() -> None:
    """
    Populate PegaNodes for test cases
    """
    PegaNode.objects.create(name='SANDBOX', production_level=PegaNode.ProductionLevels.SANDBOX)
    PegaNode.objects.create(name='DEVELOPMENT', production_level=PegaNode.ProductionLevels.DEVELOPMENT)
    PegaNode.objects.create(name='QA', production_level=PegaNode.ProductionLevels.QA)
    PegaNode.objects.create(name='PRELIVE', production_level=PegaNode.ProductionLevels.PRELIVE)
    PegaNode.objects.create(name='PRODUCTION', production_level=PegaNode.ProductionLevels.PRODUCTION)


class PegaNodeTestCases(TestCase):
    """
    Test PegaNode db interactions
    """

    def setUp(self) -> None:
        populate_nodes()

    def test_names(self) -> None:
        """
        Test PegaNode names
        """
        all_nodes: List[PegaNode] = PegaNode.objects.all()

        for node in all_nodes:
            self.assertEqual(node.name, str(node))

    def test_production_levels(self) -> None:
        """
        Test PegaNode production level choices
        """
        all_nodes: List[PegaNode] = PegaNode.objects.all()

        for node in all_nodes:
            if node.name == 'SANDBOX':
                self.assertEqual(node.production_level, 1)
                continue

            if node.name == 'DEVELOPMENT':
                self.assertEqual(node.production_level, 2)
                continue

            if node.name == 'QA':
                self.assertEqual(node.production_level, 3)
                continue

            if node.name == 'PRELIVE':
                self.assertEqual(node.production_level, 4)
                continue

            if node.name == 'PRODUCTION':
                self.assertEqual(node.production_level, 5)
                continue

    def test_get_default_context(self) -> None:
        """
        Test get_default_context() view service without node_id param
        """
        all_nodes: List[PegaNode] = PegaNode.objects.all()

        context = get_default_context()
        for node in all_nodes:
            self.assertIn(node, context['nodes'])

    def test_get_default_context_for_node(self) -> None:
        """
        Test get_default_context() view service with node_id param
        """
        all_nodes: List[PegaNode] = PegaNode.objects.all()

        for node in all_nodes:
            context = get_default_context(node_id=node.id)
            self.assertIn(node, context['nodes'])
            self.assertEqual(node, context['node'])


class LoginTestCases(TestCase):
    """
    Test login
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='pega', password='rules')

    def test_login(self) -> None:
        self.client.login(username='pega', password='rules')
        response = self.client.get(reverse('pisma:index'))
        self.assertEqual(response.status_code, 200)


class LogoutTestCases(TestCase):
    """
    Test logout
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='pega', password='rules')
        self.client.login(username='pega', password='rules')

    def test_logout(self) -> None:
        response = self.client.get(reverse('pisma:index'))
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(reverse('pisma:index'))
        self.assertEqual(response.status_code, 302)


class PismaIndexViewTestCases(TestCase):
    """
    Test index view for PISMA application
    """

    def setUp(self) -> None:
        populate_nodes()
        self.user = User.objects.create_user(username='pega', password='rules')
        self.client.login(username='pega', password='rules')

    def test_index_view(self) -> None:
        """
        Test that index view has all populated nodes in its context
        """
        all_nodes: List[PegaNode] = PegaNode.objects.all()

        response = self.client.get(reverse('pisma:index'))

        self.assertQuerysetEqual(
            list(response.context['nodes']),
            ['<PegaNode: SANDBOX>',
             '<PegaNode: DEVELOPMENT>',
             '<PegaNode: QA>',
             '<PegaNode: PRELIVE>',
             '<PegaNode: PRODUCTION>']
        )
