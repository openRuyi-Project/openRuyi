# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rpmlint
Version:        2.8.0
Release:        %autorelease
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
#!RemoteAsset:  sha256:69884a3b80438698e41dc4b39658fae611b45ad6cfb31e38db76279bfb4288b1
Source0:        https://github.com/rpm-software-management/rpmlint/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l rpmlint +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3-rpm

Requires:       bash
Requires:       binutils
Requires:       cpio
Requires:       desktop-file-utils
Requires:       file
Requires:       findutils
Requires:       python3-rpm
Requires:       python3dist(zstandard)
Requires:       rpm-build

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%generate_buildrequires
%pyproject_buildrequires

%files
%license COPYING
%doc README*
%{_bindir}/rpmlint
%{_bindir}/rpmdiff
%{python3_sitelib}/rpmlint*

%changelog
%autochangelog
