# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libisofs
Version:        1.5.6
Release:        %autorelease
Summary:        Library to create ISO 9660 disk images
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://libburnia-project.org/
VCS:            git:https://dev.lovelyhq.com/libburnia/libisofs.git
#!RemoteAsset
Source:         https://files.libburnia-project.org/releases/libisofs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(zlib)

%description
Libisofs is a library to create an ISO-9660 filesystem and supports
extensions like RockRidge or Joliet. It supports zisofs compression as well.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc AUTHORS COPYRIGHT README
%{_libdir}/libisofs*.so.*

%files devel
%{_includedir}/libisofs/
%{_libdir}/libisofs.so
%{_libdir}/pkgconfig/libisofs-1.pc

%changelog
%{?autochangelog}
