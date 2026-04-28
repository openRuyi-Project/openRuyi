# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 16e8662c34917be0065110bfcd9cc27d30f52fdf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gemmlowp
Version:        0+git20231103.%{shortcommit}
Release:        %autorelease
Summary:        Header-only low-precision GEMM library for quantized matrix multiplication
License:        Apache-2.0
URL:            https://github.com/google/gemmlowp
VCS:            git:https://github.com/google/gemmlowp.git
#!RemoteAsset:  sha256:c3feb896a1b42595cf9a508ed64ed0dc3cd84fffdb8eed790d02d0534ab322ce
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildSystem:    cmake

# Downstream packaging patch to keep the installed package header-only.
# It disables installation/export of the deprecated eight_bit_int_gemm target.
Patch2000:         2000-contrib-add-packager-options.patch

BuildOption(conf):  -S contrib
BuildOption(conf):  -DBUILD_TESTING:BOOL=OFF
BuildOption(conf):  -DGEMMLOWP_INSTALL_LEGACY_EIGHT_BIT_INT_GEMM:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
gemmlowp is a header-only C++11 library for low-precision GEMM operations.
It provides a small public interface for quantized matrix multiplication and
installs CMake package metadata for consumers of the header-only API.

%prep
%autosetup -p1 -n %{name}-%{commit}

%install -a
rm -f %{buildroot}%{_libdir}/libeight_bit_int_gemm.a

%check
# no check

%files
%license LICENSE
%doc README.md AUTHORS CONTRIBUTORS
%{_includedir}/gemmlowp/
%{_libdir}/cmake/gemmlowp/

%changelog
%autochangelog
