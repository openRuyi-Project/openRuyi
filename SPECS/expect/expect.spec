# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
Name:           expect
Version:        5.45.4
Release:        %autorelease
Summary:        A Tool for Automating Interactive Programs
License:        OpenRuyi-Public-Domain
URL:            https://core.tcl-lang.org/expect/
#!RemoteAsset
Source:         https://downloads.sourceforge.net/expect/expect%{version}.tar.gz
Patch1:         0001-expect.patch
Patch2:         0002-expect-fixes.patch
Patch3:         0003-expect-log.patch
Patch4:         0004-config-guess-sub-update.patch
Patch5:         0005-expect-errorfd.patch
Patch6:         0006-expect-5.45-format-security.patch
Patch7:         0007-expect-fix-implicit.patch
BuildSystem:    autotools

BuildOption(prep): -p0 -n %{name}%{version}
BuildOption(conf): --with-tcl=%{_libdir}
BuildOption(conf): --with-tk=no_tk
BuildOption(conf): --with-tclinclude=%{_includedir}
BuildOption(conf): --enable-shared

BuildOption(build): CFLAGS="%{optflags} -fPIC -pie -std=gnu89"
BuildOption(build): SHLIB_LD="gcc -shared"
BuildOption(build): pkglibdir=%{_libdir}/tcl/%{name}%{version}

BuildOption(install): pkglibdir=%{_libdir}/tcl/%{name}%{version}

BuildRequires:  autoconf
BuildRequires:  tcl-devel

%description
Expect is a tool for automating interactive applications like telnet, ftp, passwd,
and more. It is also useful for testing these applications.

%package        devel
Summary:        Header Files and C API Documentation for expect
Requires:       %{name} = %{version}

%description   devel
This package contains header files and documentation needed for linking to expect
from compiled languages like C or C++.

%conf -p
autoreconf -fiv

%install -a
# remove cryptdir/decryptdir, as Linux has no crypt command (bug 6668).
rm -f %{buildroot}%{_bindir}/{cryptdir,decryptdir}
rm -f %{buildroot}%{_mandir}/man1/{cryptdir,decryptdir}.1*
rm -f %{buildroot}%{_bindir}/autopasswd

ln -s libexpect%{version}.so %{buildroot}%{_libdir}/libexpect.so

# TODO: Fix tests.
%check

%files
%doc ChangeLog HISTORY INSTALL FAQ NEWS README
%{_bindir}/*
%{_libdir}/tcl/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libexpect.so
%{_mandir}/man1/*

%files devel
%{_libdir}/libexpect.so
%{_includedir}/*
%{_mandir}/man3/*

%changelog
%{?autochangelog}
