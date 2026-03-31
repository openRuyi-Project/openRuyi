# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lxml

# We currently don't bundle extra stuff
%bcond extras 0

Name:           python-%{srcname}
Version:        6.0.1
Release:        %autorelease
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            https://github.com/lxml/lxml
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  expat

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It
provides safe and convenient access to these libraries using the ElementTree It
extends the ElementTree API significantly to offer support for XPath, RelaxNG,
XML Schema, XSLT, C14N and much more.

%package     -n python3-lxml
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API
%if %{with extras}
Suggests:       python3-lxml+cssselect
Suggests:       python3-lxml+html5
Suggests:       python3-lxml+htmlsoup
Suggests:       python3-lxml+html_clean
%endif

%description -n python3-lxml
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It
provides safe and convenient access to these libraries using the ElementTree It
extends the ElementTree API significantly to offer support for XPath, RelaxNG,
XML Schema, XSLT, C14N and much more.

%if %{with extras}
%pyproject_extras_subpkg -n python3-lxml cssselect html5 htmlsoup html_clean
%endif

%prep
%autosetup -n lxml-%{version} -p1

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

%build
# Remove pregenerated Cython C sources
# We need to do this after %%pyproject_buildrequires because setup.py errors
# without Cython and without the .c files.
find -type f -name '*.c' -print -delete >&2
export WITH_CYTHON=true
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lxml

%files -n python3-lxml -f %{pyproject_files}
%license doc/licenses/BSD.txt doc/licenses/elementtree.txt
%doc README.rst

%changelog
%{?autochangelog}
