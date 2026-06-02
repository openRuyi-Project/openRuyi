# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname apsw

Name:           python-%{srcname}
Version:        3.50.4.0
Release:        %autorelease
Summary:        Another Python SQLite Wrapper
License:        any-OSI
URL:            https://github.com/rogerbinns/apsw
#!RemoteAsset:  sha256:a817c387ce2f4030ab7c3064cf21e9957911155f24f226c3ad4938df3a155e11
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
APSW is a Python wrapper for the SQLite embedded relational database engine.
It provides a thin, low-level interface that closely mirrors the SQLite C API.

%prep -a
cat > setup.apsw << 'EOF'
[build_ext]
use_system_sqlite_config = true
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/apsw

%changelog
%autochangelog
