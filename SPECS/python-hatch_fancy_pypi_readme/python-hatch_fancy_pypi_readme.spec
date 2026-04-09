# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch_fancy_pypi_readme

Name:           python-%{srcname}
Version:        25.1.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/hynek/hatch-fancy-pypi-readme
Summary:        Fancy PyPI READMEs with Hatch
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
This hatch plugin allows defining a project description in
terms of concatenated fragments that are based on static strings, files and
parts of files defined using cut-off points or regular expressions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
