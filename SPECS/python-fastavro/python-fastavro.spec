# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fastavro

Name:           python-%{srcname}
Version:        1.12.1
Release:        %autorelease
Summary:        Fast Avro for Python
License:        MIT
URL:            https://github.com/fastavro/fastavro
#!RemoteAsset:  sha256:2f285be49e45bc047ab2f6bed040bb349da85db3f3c87880e4b92595ea093b2b
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  fastavro

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The fastavro library was written to offer performance comparable to the Java
library. With regular CPython, fastavro uses C extensions which allow it to
iterate the same 10,000 record file in 1.7 seconds. With PyPy, this drops to
1.5 seconds (to be fair, the JAVA benchmark is doing some extra JSON
encoding/decoding).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/fastavro

%changelog
%autochangelog
