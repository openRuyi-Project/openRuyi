# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aom
Version:        3.13.3
Release:        %autorelease
Summary:        Royalty-free next-generation video format
License:        BSD-3-Clause
URL:            http://aomedia.org/
VCS:            git:https://aomedia.googlesource.com/aom
#!RemoteAsset:  git+https://aomedia.googlesource.com/aom#v%{version}
#!CreateArchive
Source:         %{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=1
BuildOption(conf):  -DENABLE_DOCS=0
BuildOption(conf):  -DENABLE_TESTS=0
BuildOption(conf):  -DCONFIG_ANALYZER=0
BuildOption(conf):  -DCONFIG_WEBM_IO=1
BuildOption(conf):  -DENABLE_CCACHE=0

# Building static library breaks .cmake files if we don't ship it, so drop it
# https://src.fedoraproject.org/rpms/aom/blob/rawhide/f/aom-nostatic.patch
Patch2000:          2000-aom-nostatic.patch

BuildRequires:  cmake
BuildRequires:  nasm

%description
The Alliance for Open Media's focus is to deliver a next-generation
video format that is:

 - Interoperable and open;
 - Optimized for the Internet;
 - Scalable to any modern device at any bandwidth;
 - Designed with a low computational footprint and optimized for hardware;
 - Capable of consistent, highest-quality, real-time video delivery; and
 - Flexible for both commercial and non-commercial content, including
   user-generated content.

This package contains the reference encoder and decoder.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE PATENTS
%{_bindir}/aomdec
%{_bindir}/aomenc
%{_libdir}/libaom.so.*

%files devel
%{_includedir}/aom/
%{_libdir}/libaom.so
%{_libdir}/pkgconfig/aom.pc
%{_libdir}/cmake/AOM/

%changelog
%autochangelog
