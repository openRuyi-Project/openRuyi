# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname colorlog

Name:           python-%{srcname}
Version:        6.10.1
Release:        %autorelease
Summary:        Colored formatter for the Python logging module
License:        MIT
URL:            https://github.com/borntyping/python-colorlog
#!RemoteAsset
Source:         https://github.com/borntyping/python-colorlog/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install): -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
colorlog.ColoredFormatter is a formatter for use with Python's logging module
that outputs records using terminal colors.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest -v

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
