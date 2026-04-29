# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Pygments
%global pypi_name pygments

Name:           python-pygments
Version:        2.19.2
Release:        %autorelease
Summary:        Syntax highlighting
License:        BSD-2-clause
URL:            https://pygments.org/
#!RemoteAsset:  sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pygments
BuildOption(check):  -e 'pygments.sphinxext*'

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(docutils)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pygments is a syntax highlighting package written in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE*
%doc README*
%{_bindir}/pygmentize

%changelog
%{?autochangelog}
