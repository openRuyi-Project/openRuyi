# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lxml

# We currently don't bundle extra stuff
# Because we don't have python3dist(tox-current-env)
%bcond extras 0

Name:           python-%{srcname}
Version:        6.0.1
Release:        %autorelease
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            https://github.com/lxml/lxml
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:2b3a882ebf27dd026df3801a87cf49ff791336e0f94b0fad195db77e01240690
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# We don't have python-cssselect
BuildOption(check):  -e lxml.cssselect
# We don't have python-bs4 & python-BeautifulSoup
BuildOption(check):  -e lxml.html.ElementSoup
BuildOption(check):  -e lxml.html.html5parser
BuildOption(check):  -e lxml.html.soupparser
# lxml.html.clean module is now a separate project lxml_html_clean
BuildOption(check):  -e lxml.html.clean
# Could not find doctest (only use this function *inside* a doctest)
BuildOption(check):  -e lxml.html.usedoctest
BuildOption(check):  -e lxml.usedoctest

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%if %{with extras}
Suggests:       python3dist(lxml[cssselect])
Suggests:       python3dist(lxml[html5])
Suggests:       python3dist(lxml[htmlsoup])
Suggests:       python3dist(lxml[html_clean])
%endif

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It
provides safe and convenient access to these libraries using the ElementTree It
extends the ElementTree API significantly to offer support for XPath, RelaxNG,
XML Schema, XSLT, C14N and much more.

%if %{with extras}
%pyproject_extras_subpkg -n python-lxml cssselect html5 htmlsoup html_clean
%endif

%prep -a
# Don't run html5lib tests if we are not building with extras
%if %{without extras}
rm src/lxml/html/tests/test_html5parser.py
%endif
# Remove limit for version of Cython
sed -i "s/Cython.*/Cython/" requirements.txt
sed -i 's/"Cython.*",/"Cython",/' pyproject.toml

%generate_buildrequires
# If extras are enabled, generate build requirements for them
# Otherwise, generate basic build requirements without extras
%if %{with extras}
%pyproject_buildrequires -e cssselect,html5,htmlsoup,html_clean
%else
%pyproject_buildrequires
%endif

%build -p
# Remove pregenerated Cython C sources
# We need to do this after %%pyproject_buildrequires because setup.py errors
# without Cython and without the .c files.
find -type f -name '*.c' -print -delete >&2
export WITH_CYTHON=true

%files -f %{pyproject_files}
%license doc/licenses/BSD.txt doc/licenses/elementtree.txt
%doc README.rst

%changelog
%autochangelog
