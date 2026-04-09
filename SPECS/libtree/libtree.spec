# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtree
Version:        3.1.1
Release:        %autorelease
Summary:        Ldd as a tree
License:        MIT
URL:            https://github.com/haampie/libtree
#!RemoteAsset:  sha256:6148436f54296945d22420254dd78e1829d60124bb2f5b9881320a6550f73f5c
Source0:        https://github.com/haampie/libtree/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  make
BuildRequires:  gcc

%description
Libtree is tool that turns ldd into a tree, and explains how shared libraries
are found or why they cannot be located.

# No configure.
%conf

%build -p
%set_build_flags

%check
# this test is not working in rv64.
rm -rf tests/05_32_bits
make check

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/libtree
%{_mandir}/man1/libtree.1*

%changelog
%autochangelog
