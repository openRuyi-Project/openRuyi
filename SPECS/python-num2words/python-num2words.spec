# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname num2words

Name:           python-%{srcname}
Version:        0.5.14
Release:        %autorelease
Summary:        Modules to convert numbers to words
License:        LGPL-2.1-or-later
URL:            https://github.com/savoirfairelinux/num2words
VCS:            git:https://github.com/savoirfairelinux/num2words.git
#!RemoteAsset:  sha256:b066ec18e56b6616a3b38086b5747daafbaa8868b226a36127e0451c0cf379c6
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       python3dist(docopt) >= 0.6.2

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
num2words is a Python library that converts numbers to words in multiple
languages. It supports cardinal, ordinal, year, and currency conversions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license COPYING
%{_bindir}/num2words

%changelog
%autochangelog
