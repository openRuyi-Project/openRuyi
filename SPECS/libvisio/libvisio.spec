# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvisio
Version:        0.1.11
Release:        %autorelease
Summary:        Microsoft Visio drawing import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libvisio
VCS:            git:https://git.libreoffice.org/libvisio
#!RemoteAsset:  sha256:2a6efd40b6d9dbcb70fba3be53112366882ba97b57151df3698dfa478c8d8dd3
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tests
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)

%description
libvisio reads Microsoft Visio drawings and stencils. Its conversion
tools extract text and render drawings as XHTML with embedded SVG.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING.MPL
%{_bindir}/vsd2raw
%{_bindir}/vsd2text
%{_bindir}/vsd2xhtml
%{_bindir}/vss2raw
%{_bindir}/vss2text
%{_bindir}/vss2xhtml
%{_libdir}/libvisio-0.1.so.*

%files devel
%{_includedir}/libvisio-0.1/
%{_libdir}/libvisio-0.1.so
%{_libdir}/pkgconfig/libvisio-0.1.pc

%changelog
%autochangelog
