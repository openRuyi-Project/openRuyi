# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _lto_cflags %{nil}

Name:           cmocka
Version:        2.0.2
Release:        %autorelease
Summary:        Lightweight library to simplify and generalize unit tests for C
License:        Apache-2.0
URL:            https://cmocka.org
VCS:            git:https://git.cryptomilk.org/projects/cmocka.git
#!RemoteAsset:  sha256:39f92f366bdf3f1a02af4da75b4a5c52df6c9f7e736c7d65de13283f9f0ef416
Source0:        https://cmocka.org/files/2.0/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DUNIT_TESTING=ON

BuildRequires:  cmake
BuildRequires:  pkg-config

%description
cmocka is an elegant unit testing framework for C with support for mock
objects. It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

%package        devel
Summary:        Development headers for the cmocka library
Requires:       cmocka = %{version}-%{release}
Requires:       pkg-config
Requires:       (cmocka-cmake if cmake)

%description    devel
Development headers for the cmocka unit testing library.

%package        cmake
Summary:        cmake support for the cmocka library
Requires:       cmake
Requires:       cmocka-devel = %{version}-%{release}
Provides:       cmocka-devel:%{_libdir}/cmake/cmocka

%description    cmake
cmake support for developing with the cmocka unit testing library.

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libcmocka.so.*

%files devel
%{_includedir}/cmocka.h
%{_includedir}/cmocka_pbc.h
%{_includedir}/cmocka_version.h
%{_libdir}/libcmocka.so
%{_libdir}/pkgconfig/cmocka.pc

%files cmake
%{_libdir}/cmake/cmocka

%changelog
%autochangelog
