# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libzmf
Version:        0.0.2
Release:        %autorelease
Summary:        Zoner Draw document import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libzmf
VCS:            git:https://git.libreoffice.org/libzmf
#!RemoteAsset:  sha256:27051a30cb057fdb5d5de65a1f165c7153dc76e27fe62251cbb86639eb2caf22
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tests
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)

%description
libzmf reads Zoner Draw vector drawings and exposes their content
through librevenge. Its utilities export SVG and raw drawing events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/zmf2raw
%{_bindir}/zmf2svg
%{_libdir}/libzmf-0.0.so.*

%files devel
%{_includedir}/libzmf-0.0/
%{_libdir}/libzmf-0.0.so
%{_libdir}/pkgconfig/libzmf-0.0.pc

%changelog
%autochangelog
