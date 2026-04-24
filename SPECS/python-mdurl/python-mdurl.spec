# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mdurl

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Markdown URL utilities
License:        MIT
URL:            https://github.com/executablebooks/mdurl
#!RemoteAsset:  sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
URL utilities for markdown-it parser.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
