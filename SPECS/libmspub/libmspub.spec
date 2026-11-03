# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmspub
Version:        0.1.5
Release:        %autorelease
Summary:        Microsoft Publisher document import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libmspub
VCS:            git:https://git.libreoffice.org/libmspub
#!RemoteAsset:  sha256:3671095f5a10bee8a755052a30576952c5b16d8b0f2ba9f2fb998338c18cb119
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CXXFLAGS="%{optflags} -std=gnu++17"
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-i18n)

%description
libmspub reads Microsoft Publisher documents and exposes their layout
through librevenge. The utilities export XHTML and raw drawing events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING.MPL
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml
%{_libdir}/libmspub-0.1.so.*

%files devel
%{_includedir}/libmspub-0.1/
%{_libdir}/libmspub-0.1.so
%{_libdir}/pkgconfig/libmspub-0.1.pc

%changelog
%autochangelog
