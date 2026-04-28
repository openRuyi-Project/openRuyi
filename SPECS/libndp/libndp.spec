# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libndp
Version:        1.9
Release:        %autorelease
Summary:        Library for Neighbor Discovery Protocol
License:        LGPL-2.1-or-later
URL:            http://libndp.org
VCS:            git:https://github.com/jpirko/libndp
#!RemoteAsset
Source0:        http://libndp.org/files/libndp-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(install):  INSTALL="install -p"

BuildRequires:  make

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package        devel
Summary:        Libraries and header files for libndp development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%files
%doc COPYING
%{_libdir}/*so.*
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libndp.pc

%changelog
%{?autochangelog}
