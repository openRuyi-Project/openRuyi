# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch-requirements-txt

Name:           python-hatch-requirements-txt
Version:        0.4.1
Release:        %autorelease
Summary:        Hatchling plugin to read project dependencies from requirements.txt
License:        MIT
URL:            https://github.com/repo-helper/hatch-requirements-txt
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/hatch_requirements_txt-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hatch_requirements_txt

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
%{summary}.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
