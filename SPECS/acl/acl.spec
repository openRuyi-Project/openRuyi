# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           acl
Summary:        Commands for Manipulating POSIX Access Control Lists
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Version:        2.4.0
Release:        %autorelease
URL:            https://savannah.nongnu.org/projects/acl
VCS:            git:https://git.savannah.nongnu.org/git/acl.git
#!RemoteAsset:  sha256:e661131456d2708a01c614a0f400e11d7d1bfaeb6f3e74b75bb980b72f0161a3
Source:         https://download.savannah.nongnu.org/releases/acl/acl-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --docdir=%{_defaultdocdir}/%{name}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libattr)
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
getfacl and setfacl commands for retrieving and setting POSIX access
control lists.

%package        devel
Summary:        Header files for the POSIX ACL library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
This package contains all necessary include files and libraries needed
to develop applications that require libacl.

%conf -p
autoreconf -fiv

%install -p
rm -rvf %{buildroot}/%{_defaultdocdir}/%{name}

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license doc/COPYING doc/COPYING.LGPL
%doc doc/extensions.txt doc/libacl.txt doc/CHANGES
%{_docdir}/acl
%{_libdir}/libacl.so.1*
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%{_includedir}/acl/
%{_includedir}/sys/acl.h
%{_libdir}/libacl.so
%{_mandir}/man3/*.3*
%{_libdir}/pkgconfig/libacl.pc

%changelog
%autochangelog
