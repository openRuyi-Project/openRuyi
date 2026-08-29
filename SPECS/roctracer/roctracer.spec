# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# roctracer needs a GPU to run tests
%bcond test 0

%global rocm_release 7.2
%global rocm_patch   4
%global rocm_version %{rocm_release}.%{rocm_patch}

%global llvm_maj_ver 22

Name:           roctracer
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Tracer Callback/Activity Library
License:        MIT
URL:            https://github.com/ROCm/roctracer
#!RemoteAsset:  sha256:dbae23414fdb186085072b025d6b233b8ece27dd6e58e4650f5fb1fa2fe1af2a
Source:         %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  python3dist(cppheaderparser)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros

%global _description %{expand:
roctracer is a callback and activity tracing library for ROCm. It provides
function call tracing for HIP and other ROCm runtimes, activity (asynchronous)
tracing, and ROCTx user-defined event markers.
}

%description
%{_description}

%package        devel
Summary:        The roctracer development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The roctracer development package.

%if %{with test}
%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}
%endif

%prep -a
# No option in cmake to turn off testing
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt
%else
# Adjust test running script lib dir
sed -i -e 's@../lib/@../%{_lib}/@' test/run.sh
%endif

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%install -a
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE.md
rm -rf %{buildroot}%{_datadir}/doc/%{name}-asan

%files
%doc README.md
%license LICENSE.md
%{_libdir}/libroctracer64.so.*
%{_libdir}/libroctx64.so.*
%{_libdir}/roctracer/

%files devel
%{_includedir}/roctracer/
%{_libdir}/libroctracer64.so
%{_libdir}/libroctx64.so

%if %{with test}
%files test
%{_datadir}/roctracer/
%endif

%changelog
%autochangelog
