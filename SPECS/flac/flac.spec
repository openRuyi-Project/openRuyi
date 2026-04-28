# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           flac
Version:        1.5.0
Release:        %autorelease
Summary:        An encoder/decoder for the Free Lossless Audio Codec
License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.3-or-later
URL:            https://github.com/xiph/flac
#!RemoteAsset
Source:         https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ogg)

%description
This package contains the command-line tools (flac, metaflac) for the
Free Lossless Audio Codec.

%package        libs
Summary:        Libraries for the Free Lossless Audio Codec

%description    libs
This package contains the shared libraries for the Free Lossless Audio Codec.

%package        devel
Summary:        Development files for the FLAC libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and documentation
needed to develop applications that use the FLAC libraries.

%prep -a
sed -i 's|FLAC__TEST_LEVEL=1|FLAC__TEST_LEVEL=0|' test/CMakeLists.txt

%check
%ctest --parallel 1

%install -a
rm -rfv %{buildroot}%{_docdir}/FLAC
install -d -m 755 %{buildroot}%{_datadir}/aclocal
install src/libFLAC/libFLAC.m4 %{buildroot}%{_datadir}/aclocal/
install src/libFLAC++/libFLAC++.m4 %{buildroot}%{_datadir}/aclocal/

%files
%{_bindir}/flac
%{_bindir}/metaflac
%{_mandir}/man1/flac.1*
%{_mandir}/man1/metaflac.1*

%files libs
%doc AUTHORS README.md CHANGELOG.md
%license COPYING.*
%{_libdir}/libFLAC.so.14*
%{_libdir}/libFLAC++.so.11*

%files devel
%doc doc/api
%{_includedir}/FLAC
%{_includedir}/FLAC++
%{_libdir}/cmake/FLAC/
%{_libdir}/libFLAC.so
%{_libdir}/libFLAC++.so
%{_libdir}/pkgconfig/flac++.pc
%{_libdir}/pkgconfig/flac.pc
%{_datadir}/aclocal/*.m4

%changelog
%{?autochangelog}
