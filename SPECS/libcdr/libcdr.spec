# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcdr
Version:        0.1.9
Release:        %autorelease
Summary:        CorelDRAW and Corel Presentation Exchange import library
License:        MPL-2.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libcdr
VCS:            git:https://git.libreoffice.org/libcdr
#!RemoteAsset:  sha256:f7bb6abdd7f226820f288a93dd8d07759833c0250d9e202af90f9b312c4665a3
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-tools
BuildOption(conf):  --enable-tests
BuildOption(conf):  --without-docs

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)

%description
libcdr reads CorelDRAW and Corel Presentation Exchange drawings. Its
utilities extract text and export drawings as XHTML with embedded SVG.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license COPYING.MPL
%{_bindir}/cdr2raw
%{_bindir}/cdr2text
%{_bindir}/cdr2xhtml
%{_bindir}/cmx2raw
%{_bindir}/cmx2text
%{_bindir}/cmx2xhtml
%{_libdir}/libcdr-0.1.so.*

%files devel
%{_includedir}/libcdr-0.1/
%{_libdir}/libcdr-0.1.so
%{_libdir}/pkgconfig/libcdr-0.1.pc

%changelog
%autochangelog
