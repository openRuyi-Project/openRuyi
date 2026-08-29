# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ply

Name:           python-%{srcname}
Version:        3.11
Release:        %autorelease
Summary:        Python Lex-Yacc
License:        BSD-3-Clause
URL:            https://github.com/dabeaz/ply
#!RemoteAsset:  sha256:00c7c1aaa88358b9c765b6d3000c6eec0ba42abca5351b095321aef446081da3
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PLY is a straightforward lex/yacc implementation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES README.md

%changelog
%autochangelog
