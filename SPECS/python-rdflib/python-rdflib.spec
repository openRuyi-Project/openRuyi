# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rdflib

Name:           python-rdflib
Version:        7.5.0
Release:        %autorelease
Summary:        Python library for working with RDF
License:        BSD-3-Clause
URL:            https://github.com/RDFLib/rdflib
#!RemoteAsset:  sha256:663083443908b1830e567350d72e74d9948b310f827966358d76eebdc92bf592
Source:         https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://github.com/RDFLib/rdflib/issues/3083
Patch0:         0001-Fix-py3.14-test-failure-due-to-NotImplemented-change.patch

BuildOption(install):  %{srcname}
# If we add python3dist(httpx) here, then the tests will fail.
BuildOption(check):  -e rdflib.contrib.graphdb.client
BuildOption(check):  -e rdflib.contrib.rdf4j.client

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
RDFLib is a pure Python package for working with RDF. RDFLib contains most
things you need to work with RDF, including parsers and serializers for
RDF/XML, N3, NTriples, N-Quads, Turtle, TriX, Trig and JSON-LD, a Graph
interface which can be backed by any one of a number of Store implementations,
store implementations for in-memory, persistent on disk (Berkeley DB) and
remote SPARQL endpoints, a SPARQL 1.1 implementation - supporting SPARQL 1.1
Queries and Update statements - and SPARQL function extension mechanisms.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -k "not test_sparqleval and not test_parser"\
        -m "not webtest"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
%autochangelog
