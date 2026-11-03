# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfreehand
Version:        0.1.4
Release:        %autorelease
Summary:        Macromedia FreeHand drawing import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libfreehand
VCS:            git:https://git.libreoffice.org/libfreehand
#!RemoteAsset:  sha256:350b10d24a76d7e8c8ae98b74c2d432a2c8ddec08935d09856d20b695a35e600
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
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(cppunit)

%description
libfreehand reads Macromedia FreeHand drawings. Its conversion tools
export drawings to SVG and extract their text and drawing commands.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS
%license COPYING
%{_bindir}/fh2raw
%{_bindir}/fh2svg
%{_bindir}/fh2text
%{_libdir}/libfreehand-0.1.so.*

%files devel
%{_includedir}/libfreehand-0.1/
%{_libdir}/libfreehand-0.1.so
%{_libdir}/pkgconfig/libfreehand-0.1.pc

%changelog
%autochangelog
