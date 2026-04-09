# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvncserver
Version:        0.9.15
Release:        %autorelease
Summary:        Library to make writing a VNC server easy
License:        GPL-2.0-or-later
URL:            https://github.com/LibVNC/libvncserver
#!RemoteAsset:  sha256:62352c7795e231dfce044beb96156065a05a05c974e5de9e023d688d8ff675d7
Source0:        https://github.com/LibVNC/libvncserver/archive/refs/tags/LibVNCServer-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{__cxx}
BuildOption(conf):  -DBUILD_EXAMPLES=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lzo2)

%description
LibVNCServer makes writing a VNC server (or more correctly, a program exporting
a frame-buffer via the Remote Frame Buffer protocol) easy.
It hides the programmer from the tedious task of managing clients and
compression schemata.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       coreutils
Requires:       pkgconfig(zlib)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
for file in ChangeLog ; do
    iconv -f ISO_8859-1 -t UTF-8 ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv -f ${file}.new ${file}
done

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS* README* CONTRIBUTING.md HISTORY.md SECURITY.md
%{_libdir}/libvncclient.so.*
%{_libdir}/libvncserver.so.*

%files devel
%{_includedir}/rfb/
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc
%{_libdir}/cmake/LibVNCServer/

%changelog
%autochangelog
