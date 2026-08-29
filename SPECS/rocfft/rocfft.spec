# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Without a GPU, the test cases will fail with `what():  hipGetDeviceCount failed`
# rocFFT needs a GPU to run tests
%bcond test 0

%global rocm_release 7.2
%global rocm_patch   4
%global rocm_version %{rocm_release}.%{rocm_patch}

%global llvm_maj_ver 22

Name:           rocfft
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Fast Fourier Transforms library
License:        MIT
URL:            https://github.com/ROCm/rocFFT
#!RemoteAsset:  sha256:3a01fab8e598e16d42dbcbd3ce942b9b55a86d1c2ce383dec829835f42b42222
Source:         %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-cmake-use-gnu-installdirs.patch
Patch2000:      2000-relax-sqlite-version-requirement.patch

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=ON
BuildOption(conf):  -DROCFFT_BUILD_OFFLINE_TUNER=OFF
BuildOption(conf):  -DROCFFT_KERNEL_CACHE_ENABLE=OFF
BuildOption(conf):  -DSQLITE_USE_SYSTEM_PACKAGE=ON
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  boost-devel
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hiprand)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(rocrand)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  libomp-devel(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros

%global _description %{expand:
rocFFT is a software library for computing fast Fourier transforms (FFTs) written
in HIP. It is part of AMD's software ecosystem based on ROCm. In addition to
AMD GPU hardware, rocFFT also works on CPU devices to facilitate testing.
}

%description
%{_description}

%package        devel
Summary:        The rocFFT development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(hip)

%description    devel
The rocFFT development package.

%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%install -a
# we don't need the rocfft_rtc_helper binary and client-info file
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} rm -rf "{}"
rm -rf %{buildroot}/%{_prefix}/.info
rm -f %{buildroot}%{_datadir}/doc/rocfft/LICENSE.md

%if %{with test}
%check
%{_vpath_builddir}/clients/staging/rocfft-test
%endif

%files
%doc README.md
%license LICENSE.md
%{_libdir}/librocfft.so.0{,.*}

%files devel
%{_includedir}/rocfft/
%{_libdir}/cmake/rocfft/
%{_libdir}/librocfft.so

%files test
%{_bindir}/rocfft-test
%{_bindir}/rtc_helper_crash

%changelog
%autochangelog
