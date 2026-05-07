# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           exiv2
Version:        0.28.8
Release:        %autorelease
Summary:        Exif, IPTC and XMP metadata manipulation library
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/Exiv2/exiv2
#!RemoteAsset:  sha256:ea51b0609f58a9afa063b60daa1539948b62247721e154f4fff0ad3aec9f9756
Source0:        https://github.com/Exiv2/exiv2/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DEXIV2_BUILD_SAMPLES=OFF
BuildOption(conf):  -DEXIV2_ENABLE_NLS=ON
%if %{with doc}
BuildOption(conf):  -DEXIV2_BUILD_DOC=ON
BuildOption(conf):  -DCMAKE_INSTALL_DOCDIR="%{_pkgdocdir}"
%else
BuildOption(conf):  -DEXIV2_BUILD_DOC=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(zlib)

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libxslt
%endif

%description
Exiv2 is a C++ library and a command line utility to read, write, delete and
modify Exif, IPTC, XMP and ICC image metadata.

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed for
developing with exiv2.

%if %{with doc}
%build -a
%cmake_build --target doc
%endif

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING doc/COPYING-XMPSDK
%doc doc/ChangeLog exiv2.md SECURITY.md
%{_bindir}/exiv2
%{_mandir}/man1/exiv2*.1*
%{_libdir}/libexiv2.so.28*
%{_libdir}/libexiv2.so.%{version}

%files devel
%{_includedir}/exiv2/
%{_libdir}/cmake/exiv2/
%{_libdir}/libexiv2.so
%{_libdir}/pkgconfig/exiv2.pc
%if %{with doc}
%{_pkgdocdir}/
%endif

%changelog
%autochangelog
