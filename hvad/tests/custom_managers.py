# -*- coding: utf-8 -*-
from hvad.test_utils.data import DOUBLE_NORMAL
from hvad.test_utils.testcase import NaniTestCase
from hvad.test_utils.project.app.models import CustomManagerProxy
from hvad.test_utils.fixtures import TwoTranslatedNormalMixin


class CustomManagersTests(NaniTestCase, TwoTranslatedNormalMixin):
    def test_simple_filter(self):
        qs = CustomManagerProxy.objects.language('en').having_translated_field('English1')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        self.assertEqual(obj.translated_field, DOUBLE_NORMAL[1]['translated_field_en'])
        qs = CustomManagerProxy.objects.language('ja').having_translated_field(u'日本語一')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        self.assertEqual(obj.translated_field, DOUBLE_NORMAL[1]['translated_field_ja'])

    def test_any_language_filter(self):
        from hvad.utils import get_translation_aware_manager
        qs = CustomManagerProxy.objects.any_language().having_translated_field('English1')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        qs = CustomManagerProxy.objects.any_language().having_translated_field(u'日本語一')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])

    def test_translation_aware_manager(self):
        from hvad.utils import get_translation_aware_manager
        manager = get_translation_aware_manager(CustomManagerProxy)
        qs = manager.having_translated_field('English1')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        qs = manager.having_translated_field(u'日本語一')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])

    def test_translation_aware_queryset(self):
        from hvad.utils import get_translation_aware_manager
        manager = get_translation_aware_manager(CustomManagerProxy)
        qs = manager.all().having_translated_field('English1')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        qs = manager.all().having_translated_field(u'日本語一')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
