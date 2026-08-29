# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lsb-release
Version:        12.1
Release:        %autorelease
Summary:        Linux Standard Base version reporting utility (minimal implementation)
License:        ISC
URL:            https://gioele.io/lsb-release-minimal
VCS:            git:https://codeberg.org/gioele/lsb-release-minimal.git
#!RemoteAsset:  sha256:87bdd39802a7c15753f5c5187f2901b6b9df4dd11721e3762ca4b1701a421c85
Source0:        https://codeberg.org/gioele/lsb-release-minimal/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make

%description
The Linux Standard Base (http://www.linuxbase.org/) is a standard
core system that third-party applications written for Linux can
depend upon.

The lsb_release command is a simple tool to help identify the Linux
distribution being used and its compliance with the Linux Standard Base.

This package contains a bare-bones implementation that uses the
information in /etc/os-release instead of relying on LSB packages.

# No Configure
%conf

# No tests
%check

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/lsb_release
%{_datadir}/man/man1/lsb_release.1.gz

%changelog
%autochangelog
