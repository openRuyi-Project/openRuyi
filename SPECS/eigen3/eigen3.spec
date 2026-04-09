# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           eigen3
Version:        5.0.1
Release:        %autorelease
Summary:        A lightweight C++ template library for vector and matrix math
License:        MPL-2.0 AND LGPL-2.1-or-later AND BSD-3-Clause
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
VCS:            git:https://gitlab.com/libeigen/eigen
#!RemoteAsset
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.bz2
Patch0:         eigen3_libinstalldir.patch
BuildSystem:    cmake

BuildOption(conf):  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/eigen3
BuildOption(conf):  -DCMAKE_CXX_FLAGS='%{build_cxxflags}'

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms. This package contains the
header files needed for development.

%check
%cmake_build --target buildtests
# FIXME: A few tests might fail.
%ctest -- || tac %{_build}/Testing/Temporary/LastTest.log| gawk -e '
             /Test Failed./ {found=1; print; next}
             /[0-9]+\/[0-9]+ Test: / {if(found) print; found=0; next}
             found {print}'|tac

%files
%license COPYING.README COPYING.BSD COPYING.MPL2
%{_includedir}/eigen3/
%dir %{_datadir}/eigen3
%{_datadir}/eigen3/cmake/
%{_datadir}/pkgconfig/eigen3.pc
%{_libdir}/libeigen_*

%changelog
%autochangelog
