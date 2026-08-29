# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kernel-hardening-checker
%global modname kernel_hardening_checker

Name:           %{srcname}
Version:        0.6.17.1
Release:        %autorelease
Summary:        Tool for checking the security hardening options of the Linux kernel
License:        GPL-3.0-only
URL:            https://github.com/a13xp0p0v/kernel-hardening-checker
#!RemoteAsset:  sha256:2383e851b44fe74c9a5db32919b897af05f022e676e8d1184cc53594bb9b344c
Source0:        https://github.com/a13xp0p0v/kernel-hardening-checker/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%description
A tool for checking the security hardening options of the Linux kernel.
It checks the kernel configuration options and sysctl parameters against
security hardening recommendations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%{_bindir}/kernel-hardening-checker

%changelog
%autochangelog
