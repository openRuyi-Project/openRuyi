# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname netaddr
%bcond doc 0

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        A pure Python network address representation and manipulation library
License:        BSD-3-Clause
URL:            https://github.com/netaddr/netaddr
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(furo)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A pure Python library for representing and manipulating network addresses.

Netaddr provides support for:

Layer 3 addresses

  - IPv4 and IPv6 addresses, subnets, masks, prefixes
  - iterating, slicing, sorting, summarizing and classifying IP networks
  - dealing with various ranges formats (CIDR, arbitrary ranges and globs, nmap)
  - set based operations (unions, intersections etc) over IP addresses and subnets
  - parsing a large variety of different formats and notations
  - looking up IANA IP block information
  - generating DNS reverse lookups
  - supernetting and subnetting

Layer 2 addresses

  - representation and manipulation MAC addresses and EUI-64 identifiers
  - looking up IEEE organisational information (OUI, IAB)
  - generating derived IPv6 addresses

%prep -a
# Make rpmlint happy, rip out python shebang lines from most python modules
find netaddr -name "*.py" | xargs sed -i -e '1 {/^#!\//d}'

%generate_buildrequires
%pyproject_buildrequires

%build -a
%if %{with doc}
#docs
cd docs
PYTHONPATH='../' sphinx-build-%{python3_version} -b html -d build/doctrees source python3/html
rm -f python3/html/.buildinfo
%endif

%files -f %{pyproject_files}
%license COPYRIGHT.rst
%doc AUTHORS.rst CHANGELOG.rst README.rst THANKS.rst
%if %{with docs}
%doc docs/python3/html
%endif
%{_bindir}/netaddr

%changelog
%{?autochangelog}
