# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch_fancy_pypi_readme

Name:           python-hatch-fancy-pypi-readme
Version:        25.1.0
Release:        %autorelease
Summary:        Fancy PyPI READMEs with Hatch
License:        MIT
URL:            https://github.com/hynek/hatch-fancy-pypi-readme
#!RemoteAsset:  sha256:9c58ed3dff90d51f43414ce37009ad1d5b0f08ffc9fc216998a06380f01c0045
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-hatch-fancy-pypi-readme = %{version}-%{release}
%python_provide python3-hatch-fancy-pypi-readme

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
