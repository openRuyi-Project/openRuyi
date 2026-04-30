# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyxnat

Name:           python-%{srcname}
Version:        1.6.4
Release:        %autorelease
Summary:        XNAT client library for Python
License:        BSD-3-Clause
URL:            https://github.com/pyxnat/pyxnat
#!RemoteAsset:  sha256:68f918e80f5ee8b8039fa5a972afb5b16ecda8851d7da9bfce60f152c9a5a859
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# pathlib is part of the Python 3 standard library.
Patch2000:      2000-drop-pathlib-backport-dependency.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pyxnat provides a Python interface for XNAT and XNAT Central, including
querying, data management, and automation workflows.

%generate_buildrequires
%pyproject_buildrequires

%check
# Tests require remote or local XNAT instances and Docker.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/sessionmirror.py

%changelog
%autochangelog
