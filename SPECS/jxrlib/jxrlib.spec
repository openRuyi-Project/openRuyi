# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jxrlib
Version:        1.4.2
Release:        %autorelease
Summary:        JPEG XR reference implementation library
License:        BSD-2-Clause
URL:            https://github.com/mircomir/jxrlib
#!RemoteAsset:  sha256:1ccc2b6e3afd758c8b33cabc1f05ff56c9babb8b91a99b8281136a1a329b8adb
Source0:        %{url}/archive/refs/tags/%{version}/%{version}.tar.gz
# https://gitlab.archlinux.org/archlinux/packaging/packages/jxrlib/-/blob/1.3.2-1/CMakeLists.txt
Source1:        CMakeLists.txt
BuildSystem:    cmake

BuildRequires:  cmake

%description
Jxrlib is the reference implementation of the JPEG XR image codec. It provides
the codec and glue libraries as well as command-line encoding and decoding tools.

%package        devel
Summary:        Development files for jxrlib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config metadata for developing applications using jxrlib.

%prep -a
# The upstream release does not ship a CMake build description.
install -pm 0644 %{SOURCE1} CMakeLists.txt

%files
%doc README.md
%license LICENSE
%{_bindir}/JxrDecApp
%{_bindir}/JxrEncApp
%{_libdir}/libjpegxr.so.*
%{_libdir}/libjxrglue.so.*

%files devel
%{_includedir}/jxrlib/
%{_libdir}/libjpegxr.so
%{_libdir}/libjxrglue.so
%{_libdir}/pkgconfig/libjxr.pc

%changelog
%autochangelog
