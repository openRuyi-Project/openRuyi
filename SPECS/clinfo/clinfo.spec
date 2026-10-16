# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clinfo
Version:        3.0.25.02.14
Release:        %autorelease
Summary:        Show OpenCL platforms and devices
License:        CC0-1.0
URL:            https://github.com/Oblomov/clinfo
VCS:            git:https://github.com/Oblomov/clinfo.git
#!RemoteAsset:  sha256:48b77dc33315e6f760791a2984f98ea4bff28504ff37d460d8291585f49fcd3a
Source0:        https://github.com/Oblomov/clinfo/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  MANDIR=%{_mandir}

BuildRequires:  pkgconfig(OpenCL-Headers)
BuildRequires:  pkgconfig(OpenCL)

Requires:       ocl-icd

%description
clinfo is a simple command-line application that enumerates
all possible (known) properties of the OpenCL platform and
devices available on the system.

%conf
# No configure

%check
# No check in Makefile

%files
%doc README.md
%license LICENSE legalcode.txt
%{_bindir}/clinfo
%{_mandir}/man1/clinfo.1*

%changelog
%autochangelog
