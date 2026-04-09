# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           debugedit
Version:        5.2
Release:        %autorelease
Summary:        Debuginfo extraction
License:        GPL-3.0-or-later
URL:            https://www.sourceware.org/debugedit
VCS:            git:https://sourceware.org/git/debugedit.git
#!RemoteAsset
Source0:        https://sourceware.org/ftp/%{name}/%{version}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://sourceware.org/ftp/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildSystem:    autotools

BuildOption(conf):  CC="gcc -gz=none" CXX="g++ -gz=none"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
# Tests
BuildRequires:  gdb
BuildRequires:  dwz

Requires:       binutils
Requires:       coreutils
Requires:       dwz
Requires:       elfutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       sed
Requires:       xz

%description
debugedit provides programs and scripts for creating debuginfo and source file distributions,
collect build-ids and rewrite source paths in DWARF data for debugging, tracing and profiling.

%conf -p
autoreconf -fiv

%install -a
mkdir -p %{buildroot}/usr/lib/rpm
mv %{buildroot}%{_bindir}/{find-debuginfo,sepdebugcrcfix} %{buildroot}/usr/lib/rpm
ln -s ../../bin/debugedit %{buildroot}/usr/lib/rpm

%files
%license COPYING3
%doc README
%{_bindir}/debugedit
/usr/lib/rpm/debugedit
/usr/lib/rpm/find-debuginfo
/usr/lib/rpm/sepdebugcrcfix
%{_mandir}/man1/debugedit.1%{?ext_man}
%{_mandir}/man1/find-debuginfo.1%{?ext_man}
%{_mandir}/man1/sepdebugcrcfix.1%{?ext_man}

%changelog
%autochangelog
