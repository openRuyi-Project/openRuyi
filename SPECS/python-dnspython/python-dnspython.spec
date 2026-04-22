# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dnspython

Name:           python-%{srcname}
Version:        2.8.0
Release:        %autorelease
Summary:        DNS toolkit for Python
License:        ISC
URL:            https://www.dnspython.org/
VCS:            git:https://github.com/rthalley/dnspython
#!RemoteAsset:  sha256:181d3c6996452cb1189c4046c61599b84a5a86e099562ffde77d26984ff26d0f
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  dns

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%generate_buildrequires
%pyproject_buildrequires -r -x dnssec -x idna -x trio -x doh -x doq

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
