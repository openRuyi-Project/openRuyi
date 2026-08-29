# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tbb
Summary:        The Threading Building Blocks library
Version:        2022.3.0
Release:        %autorelease
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/uxlfoundation/oneTBB
#!RemoteAsset:  sha256:01598a46c1162c27253a0de0236f520fd8ee8166e9ebb84a4243574f88e6e50a
Source0:        https://github.com/uxlfoundation/oneTBB/archive/refs/tags/v%{version}.tar.gz
Source1:        tbbmalloc.pc
Source2:        tbbmalloc_proxy.pc
BuildSystem:    cmake

# Switch build from C to C++ linker.
Patch0:         0001-tbb-c++-linkage.patch

BuildOption(conf):  -DCMAKE_CXX_STANDARD=17
BuildOption(conf):  -DTBB_STRICT:BOOL=OFF
BuildOption(conf):  -DTBB4PY_BUILD:BOOL=OFF
BuildOption(conf):  -DTBB_DISABLE_HWLOC_AUTOMATIC_SEARCH=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++

Provides:       oneTBB = %{version}-%{release}

%description
Threading Building Blocks (TBB) is a C++ runtime library that
abstracts the low-level threading details necessary for optimal
multi-core performance.

%package        devel
Summary:        The Threading Building Blocks C++ headers and shared development libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       oneTBB-devel = %{version}-%{release}

%description    devel
Header files and shared object symlinks for the Threading Building
Blocks (TBB) C++ libraries.

%install -a
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
for file in %{SOURCE1} %{SOURCE2}; do
    target=%{buildroot}/%{_libdir}/pkgconfig/$(basename ${file})
    sed 's/_FEDORA_VERSION/%{version}/' $file > $target
    touch -r $file $target
done

rm -fr %{buildroot}%{_datadir}/doc

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libtbb.so.12*
%{_libdir}/libtbbmalloc.so.2*
%{_libdir}/libtbbmalloc_proxy.so.2*

%files devel
%doc cmake/README.md
%{_includedir}/oneapi/
%{_includedir}/tbb/
%{_libdir}/*.so
%{_libdir}/cmake/TBB/
%{_libdir}/pkgconfig/tbb.pc
%{_libdir}/pkgconfig/tbbmalloc.pc
%{_libdir}/pkgconfig/tbbmalloc_proxy.pc

%changelog
%autochangelog
