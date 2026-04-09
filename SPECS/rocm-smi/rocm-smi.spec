# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm_smi_lib

%bcond test 0
%bcond doc 0

Name:           rocm-smi
Version:        %{rocm_version}
Release:        %{autorelease}
Summary:        ROCm System Management Interface Library
License:        MIT AND NCSA
URL:            https://github.com/ROCm/rocm_smi_lib
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF
BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=TRUE
BuildOption(conf):  -DBUILD_TESTS=%{?with_test:ON}%{!?with_test:OFF}

BuildRequires:  cmake
%if %{with doc}
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
%if %{with test}
BuildRequires:  pkgconfig(gtest)
%endif
BuildRequires:  pkgconfig(libdrm)

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package        devel
Summary:        ROCm SMI Library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
# /usr/include/rocm_smi/kfd_ioctl.h:26:10: fatal error: 'libdrm/drm.h' file not found
Requires:       libdrm-devel

%description    devel
ROCm System Management Interface Library development files

%if %{with test}
%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{summary}
%endif

%prep -a
# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i 's@/usr/bin/env python3@/usr/bin/python3@' python_smi_tools/*.py python_smi_tools/rsmiBindingsInit.py.in

# do not download gtest and install
# https://github.com/ROCm/rocm-systems/issues/1022
sed -i -e 's@FetchContent_MakeAvailable(googletest)@#FetchContent_MakeAvailable(googletest)@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e 's@PUBLIC GTest::gtest_main@PUBLIC gtest_main gtest@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e '/TARGETS gtest gtest_main/,+3d' tests/rocm_smi_test/CMakeLists.txt

# fix iomanip include
# https://github.com/ROCm/rocm-systems/issues/1021
sed -i '/#include <string.*/a#include <iomanip>' tests/rocm_smi_test/test_base.h

%install -a
mv %{buildroot}%{_datadir}/doc/rocm-smi-lib %{buildroot}%{_datadir}/doc/rocm_smi

%files
%doc %{_docdir}/rocm_smi
%license LICENSE.md
%{_bindir}/rocm-smi
%{_libdir}/liboam.so.1{,.*}
%{_libdir}/librocm_smi64.so.1{,.*}
%{_libexecdir}/rocm_smi

%files      devel
%{_includedir}/oam/
%{_includedir}/rocm_smi/
%{_libdir}/cmake/rocm_smi/
%{_libdir}/liboam.so
%{_libdir}/librocm_smi64.so

%if %{with test}
%files      test
%{_datarootdir}/rsmitst_tests
%endif

%changelog
%autochangelog
