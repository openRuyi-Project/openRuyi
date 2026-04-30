# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pypinyin

Name:           python-%{srcname}
Version:        0.55.0
Release:        %autorelease
Summary:        Hanzi-to-pinyin conversion module and tool
License:        MIT
URL:            https://github.com/mozillazg/python-pinyin
#!RemoteAsset:  sha256:b5711b3a0c6f76e67408ec6b2e3c4987a3a806b7c528076e7c7b86fcf0eaa66b
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The pypinyin package provides a Hanzi-to-pinyin conversion library and
command line tool.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -o addopts=-slv

%files -f %{pyproject_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{_bindir}/pypinyin

%changelog
%autochangelog
