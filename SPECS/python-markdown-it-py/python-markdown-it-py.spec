# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name markdown_it_py

%global srcname markdown-it-py

Name:           python-%{srcname}
Version:        4.0.0
Release:        %autorelease
Summary:        Python port of markdown-it
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l markdown_it

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Markdown parser done right. It follows the CommonMark spec, has configurable
syntax, and is pluggable.

%generate_buildrequires
%pyproject_buildrequires

%check
# No tests here.

%files -f %{pyproject_files}
%license LICENSE LICENSE.markdown-it
%doc README.md
%{_bindir}/markdown-it

%changelog
%{?autochangelog}
