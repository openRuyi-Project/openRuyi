# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rinutils
Version:        0.10.3
Release:        %autorelease
Summary:        Shlomi Fish's gnu11 C Library of Random headers
License:        MIT
URL:            https://github.com/shlomif/rinutils
#!RemoteAsset:  sha256:f9e527d37a6cc8c7b8870ada63caa24f32ab0d29fd1116df3ebb686583030955
Source0:        https://github.com/shlomif/rinutils/releases/download/%{version}/rinutils-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake

%description
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%package        devel
Summary:        Development files for rinutils
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

This package contains the header files and cmake files necessary for
developing programs using rinutils.

%files
%doc README.asciidoc
%license LICENSE

%files devel
%{_includedir}/rinutils/*
%{_libdir}/cmake/Rinutils/RinutilsConfig.cmake
%{_libdir}/cmake/Rinutils/RinutilsConfigVersion.cmake
%{_libdir}/pkgconfig/librinutils.pc

%changelog
%autochangelog
