##############################################################################
#
# Copyright (c) 2009 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Principal Annotation Tests

$Id$
"""
import unittest
from zope.component import provideAdapter
from zope.testing import doctest
from zope.interface import Interface
from zope.security.interfaces import IPrincipal
from zope.site.testing import siteSetUp, siteTearDown

from zope.principalannotation.utility import annotations

def setUp(test):
    site = siteSetUp(site=True)
    test.globs['root'] = site
    provideAdapter(annotations)
    provideAdapter(annotations, (IPrincipal, Interface))

def tearDown(test):
    siteTearDown()

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            'README.txt',
            setUp=setUp, tearDown=tearDown,
            optionflags=doctest.ELLIPSIS)
        ))


'''
from unittest import TestCase, TestLoader, TextTestRunner

import zope.component
from zope.interface import implements
from zope.security.interfaces import IPrincipal

from zope.app.component.testing import PlacefulSetup
from zope.app.testing import setup

from zope.principalannotation.interfaces import IPrincipalAnnotationUtility
from zope.principalannotation.utility import PrincipalAnnotationUtility

class Principal(object):
    implements(IPrincipal)

    def __init__(self, id):
        self.id = id


class PrincipalAnnotationTests(PlacefulSetup, TestCase):

    def setUp(self):
        PlacefulSetup.setUp(self)
        sm = self.buildFolders(site='/')
        self.util = PrincipalAnnotationUtility()
        zope.component.provideUtility(self.util, IPrincipalAnnotationUtility)

    def testGetSimple(self):
        prince = Principal('somebody')
        self.assert_(not self.util.hasAnnotations(prince))

        princeAnnotation = self.util.getAnnotations(prince)
        # Just getting doesn't actualy store. We don't want to store unless
        # we make a change.
        self.assert_(not self.util.hasAnnotations(prince))

        princeAnnotation['something'] = 'whatever'

        # But now we should have the annotation:
        self.assert_(self.util.hasAnnotations(prince))

    def testGetFromLayered(self):
        princeSomebody = Principal('somebody')
        sm1 = self.makeSite('folder1')
        subUtil = setup.addUtility(sm1, '', IPrincipalAnnotationUtility,
                                   PrincipalAnnotationUtility())

        parentAnnotation = self.util.getAnnotations(princeSomebody)

        # Just getting doesn't actualy store. We don't want to store unless
        # we make a change.
        self.assert_(not subUtil.hasAnnotations(princeSomebody))

        parentAnnotation['hair_color'] = 'blue'

        # But now we should have the annotation:
        self.assert_(self.util.hasAnnotations(princeSomebody))

        subAnnotation = subUtil.getAnnotations(princeSomebody)
        self.assertEquals(subAnnotation['hair_color'], 'blue')

        subAnnotation['foo'] = 'bar'

        self.assertEquals(parentAnnotation.get("foo"), None)

def test_suite():
    loader=TestLoader()
    tests = loader.loadTestsFromTestCase(PrincipalAnnotationTests)
    import zope.principalannotation.utility
    tests.addTest(doctest.DocTestSuite(zope.principalannotation.utility,
                                       setUp=setup.placelessSetUp,
                                       tearDown=setup.placelessTearDown))
    return tests

if __name__=='__main__':
    TextTestRunner().run(test_suite())
'''