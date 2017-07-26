|license| |build| |covecov| |codacy|

PDF Converter
*************

Introduction
============

The Python library pdfconv can be used to convert a variety of different file
types to PDF. It can be used on Windows as well as Linux.

To do the actual conversion pdfconv relays on comtypes and unoconv.

	* Windows: 
             * comtypes
             * unoconv
	* Linux:
             * unoconv

Dependencies
============

* comtypes (http://starship.python.net/crew/theller/comtypes/)
* unoconv (https://github.com/dagwieers/unoconv)

.. |license| image:: https://img.shields.io/badge/License-GPL%20v2-blue.svg
    :alt: License: GPL v2
    :scale: 100%
    :target: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html

.. |build| image:: https://travis-ci.org/keshrath/pdfconv.svg?branch=master
    :target: https://travis-ci.org/keshrath/pdfconv

.. |covecov| image:: https://codecov.io/gh/keshrath/pdfconv/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/keshrath/pdfconv

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/0c64c4c207b8466b9ed57aa7d0631cb6
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/keshrath/pdfconv?utm_source=github.com&utm_medium=referral&utm_content=keshrath/pdfconv&utm_campaign=badger
