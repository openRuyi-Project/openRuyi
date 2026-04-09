# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Pygments

Name:           python-pygments
Version:        2.15.1
Release:        %autorelease
Summary:        Syntax highlighting
License:        BSD-2-clause
URL:            https://pygments.org/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Provides:       python3-pygments
%python_provide python3-pygments

BuildRequires:  python3-devel
BuildSystem:    pyproject

BuildRequires:  python3-docutils
BuildOption(install):  -l pygments
BuildOption(check):    -e 'pygments.sphinxext*'
%description
Pygments is a syntax highlighting package written in Python.


%generate_buildrequires
%pyproject_buildrequires


%files -f %{pyproject_files}
%license LICENSE*
%doc README*
%{_bindir}/pygmentize

%changelog
%autochangelog
