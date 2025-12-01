# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libisofs
Version:        1.5.6
Release:        %autorelease
Summary:        Library to create ISO 9660 disk images
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://libburnia-project.org/
#!RemoteAsset
Source:         https://files.libburnia-project.org/releases/libisofs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  gcc libtool automake autoconf
BuildRequires:  make
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(zlib)

%description
Libisofs is a library to create an ISO-9660 filesystem and supports
extensions like RockRidge or Joliet. It supports zisofs compression as well.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
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
%{_libdir}/pkgconfig/libisofs*.pc

%changelog
%{?autochangelog}
