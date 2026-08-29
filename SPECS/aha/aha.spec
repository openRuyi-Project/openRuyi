# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aha
Version:        0.5.1
Release:        %autorelease
Summary:        ANSI color to HTML converter
License:        MPL-1.1 OR LGPL-2.1-or-later
URL:            https://github.com/theZiz/aha/
#!RemoteAsset:  sha256:6aea13487f6b5c3e453a447a67345f8095282f5acd97344466816b05ebd0b3b1
Source:         https://github.com/theZiz/aha/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  make

%description
aha (ANSI HTML Adapter) converts ANSI colors to HTML, e.g. if you
want to publish the output of ls --color=yes, git diff, ccal or htop
as static HTML somewhere.

# no configure
%conf

# upstream Makefile has no test suite
%check

%files
%doc CHANGELOG README.md
%{_bindir}/aha
%{_mandir}/man1/aha.*

%changelog
%autochangelog
