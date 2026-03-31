# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname expandvars

Name:           python-%{srcname}
Version:        1.1.2
Release:        %autorelease
Summary:        Expand system variables Unix style
License:        MIT
URL:            https://github.com/aio-libs/yarl
#!RemoteAsset:  sha256:6c5822b7b756a99a356b915dd1267f52ab8a4efaa135963bd7f4bd5d368f71d7
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This module is inspired by GNU bash’s variable expansion features. It can be
used as an alternative to Python’s os.path.expandvars function.

A good use case is reading config files with the flexibility of reading values
from environment variables using advanced features like returning a default
value if some variable is not defined.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
