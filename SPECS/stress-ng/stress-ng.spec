# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           stress-ng
Version:        0.20.01
Release:        %autorelease
Summary:        Stress test a computer system in various ways
License:        GPL-2.0-or-later
URL:            https://github.com/ColinIanKing/stress-ng
#!RemoteAsset:  sha256:f974863d1861e7e7b5d19e381a17f22d653dcafa12096ac96d11b2e62a22ea77
Source0:        https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  JOBDIR=%{_datadir}/stress-ng/jobs
BuildOption(install):  BASHDIR=%{_datadir}/bash-completion/completions

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  linux-headers
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  libatomic
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  bash-completion

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%conf
# No configure.

%files
%license COPYING
%doc README.md
%{_bindir}/stress-ng
%{_mandir}/stress-ng.1*
%{_datadir}/stress-ng/jobs/
%{bash_completions_dir}/stress-ng

%changelog
%{?autochangelog}
