# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname editorconfig

Name:           python-%{srcname}
Version:        0.17.1
Release:        %autorelease
Summary:        EditorConfig Python Core
License:        Python-2.0 AND MIT
URL:            https://editorconfig.org/
VCS:            git:https://github.com/editorconfig/editorconfig-core-py
#!RemoteAsset:  sha256:23c08b00e8e08cc3adcddb825251c497478df1dada6aefeb01e626ad37303745
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core. EditorConfig helps developers define and maintain consistent coding
styles between different editors and IDEs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/editorconfig

%changelog
%autochangelog
