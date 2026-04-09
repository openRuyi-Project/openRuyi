# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           checkpolicy
Version:        3.10
Release:        %autorelease
Summary:        SELinux policy compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/SELinuxProject/selinux/tree/main/libsemanage
# VCS: TODO: Multiple tags in one repo
#!RemoteAsset
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  LIBDIR="%{_libdir}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  LIBDIR="%{_libdir}"

BuildRequires:  bison
BuildRequires:  flex-devel
BuildRequires:  libsepol-static >= %{version}

%description
checkpolicy is the SELinux policy compiler. It uses libsepol to
generate the binary policy.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

# No configure
%conf

%install -a
mkdir -p %{buildroot}%{_bindir}
install test/dismod %{buildroot}%{_bindir}/sedismod
install test/dispol %{buildroot}%{_bindir}/sedispol

%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
