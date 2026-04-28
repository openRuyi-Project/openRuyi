# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname argparse-manpage

Name:           python-%{srcname}
Version:        4.7
Release:        %autorelease
Summary:        Build manual page from Python's ArgumentParser object
License:        Apache-2.0
URL:            https://github.com/praiskup/argparse-manpage
#!RemoteAsset:  sha256:1deab76b212ac8753cbb67b9d2d2bc0949bbc338bb1cc3547f0890cb34108b32
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/argparse_manpage-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l argparse_manpage build_manpages +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides tools to build manual pages from Python's
ArgumentParser object.

%pyproject_extras_subpkg -n python-%{srcname} setuptools

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
