===================
pygments-prometheus
===================

---------------------------------------
A pygments lexer for Prometheus metrics
---------------------------------------

Overview
========

This package provides a prometheus metrics_ language lexer for Pygments_.
THe lexer is published as an entry point and, once installed, Pygments
will pick it up automatically.

You can then use the ``prom`` langauge with Pygments::

  $ pygmentize -l prom metrics.prom

.. _metrics: https://prometheus.io/docs/instrumenting/exposition_formats/
.. _Pygments: https://pytments.org/

Installation
============

Use your favorite installer to install pygments-prometheus into the
same Python you have installed Pygments. for example::

  $ pip install pygments-prometheus

TO verify the installation run::

  $ pygmentize -L lexer | grep -A1 -i prometheus
    * prometheus:
      prom (filenames *.prom)
