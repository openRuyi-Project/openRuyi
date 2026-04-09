# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 1
%bcond doc 0

Name:           taglib
Summary:        Audio Meta-Data Library
Version:        2.1.1
Release:        %autorelease
License:        LGPL-2.1-only OR MPL-1.1
URL:            https://github.com/taglib/taglib
#!RemoteAsset
Source0:        https://github.com/taglib/taglib/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release

%if %{with tests}
BuildOption(conf):  -DBUILD_TESTS=ON
%else
BuildOption(conf):  -DBUILD_TESTS=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  utf8cpp
%if %{with tests}
BuildRequires:  pkgconfig(cppunit)
%endif
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files needed when building software with %{name}.

%if %{with doc}
%build -a
%cmake_build --target docs

%install -a
mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a %{_vpath_builddir}/doc/html/* %{buildroot}%{_docdir}/%{name}/html/
%endif

%if %{without tests}
%check
%endif

%files
%doc AUTHORS
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libtag.so.*
%{_libdir}/libtag_c.so.*
%if %{with doc}
%doc %{_docdir}/%{name}/html
%endif

%files devel
%doc examples
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_libdir}/cmake/taglib
%{_libdir}/pkgconfig/taglib.pc
%{_libdir}/pkgconfig/taglib_c.pc

%changelog
%autochangelog
