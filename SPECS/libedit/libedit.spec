# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define pkg_version 20250104-3.1

Name:           libedit
Version:        20250104.3.1
Release:        %autorelease
Summary:        Command Line Editing and History Library
License:        BSD-3-Clause
URL:            https://www.thrysoee.dk/editline/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://www.thrysoee.dk/editline/libedit-%{pkg_version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules

BuildRequires:  pkgconfig(ncurses)

%description
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

%package        devel
Summary:        Development files for libedit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
This package contains the header files, symbolic links, and documentation
needed to develop applications that use the libedit library.

%files
%license COPYING
%doc ChangeLog
%{_libdir}/libedit.so.0
%{_libdir}/libedit.so.0.*
%{_mandir}/man5/editrc.5*

%files devel
%{_libdir}/libedit.so
%{_includedir}/histedit.h
%{_includedir}/editline/
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%{_libdir}/pkgconfig/libedit.pc
%doc examples/*c THANKS

%changelog
%autochangelog
