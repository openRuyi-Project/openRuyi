# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global parquet_test_commit a3d96a65e11e2bbca7d22a894e8313ede90a33a3
%global arrow_test_commit df428ddaa22d94dfb525af4c0951f3dafb463795

Name:           arrow
Version:        23.0.1
Release:        %autorelease
Summary:        Apache Arrow is a universal columnar format and multi-language toolbox
License:        Apache-2.0
URL:            https://arrow.apache.org
VCS:            git:https://github.com/apache/arrow
#!RemoteAsset
Source0:        https://github.com/apache/arrow/archive/apache-arrow-%{version}/%{name}-%{version}.tar.gz
# parquet-testing data submodule, pinned to the commit used by arrow %%{version}
#!RemoteAsset
Source1:        https://github.com/apache/parquet-testing/archive/%{parquet_test_commit}/parquet-testing.tar.gz
# arrow-testing data submodule, pinned to the commit used by arrow %%{version}
#!RemoteAsset
Source2:        https://github.com/apache/arrow-testing/archive/%{arrow_test_commit}/arrow-testing.tar.gz
BuildSystem:    cmake

# use system mimalloc
Patch0:         0001-use-system-mimalloc-shared-library.patch
# riscv64: relax quantile test precision (IEEE 754 strict, no extended intermediates)
%ifarch riscv64
Patch1:         0002-test-use-approximate-comparison-for-quantile.patch
%endif

BuildOption(conf):  -DARROW_BUILD_STATIC:BOOL=OFF
BuildOption(conf):  -DARROW_BUILD_SHARED:BOOL=ON
BuildOption(conf):  -DARROW_DEPENDENCY_SOURCE:STRING=SYSTEM
BuildOption(conf):  -DARROW_PARQUET:BOOL=ON
BuildOption(conf):  -DARROW_DATASET:BOOL=ON
BuildOption(conf):  -DARROW_ACERO:BOOL=ON
BuildOption(conf):  -DARROW_SUBSTRAIT:BOOL=OFF
BuildOption(conf):  -DARROW_FLIGHT:BOOL=OFF
BuildOption(conf):  -DARROW_GANDIVA:BOOL=OFF
BuildOption(conf):  -DARROW_WITH_ZLIB:BOOL=ON
BuildOption(conf):  -DARROW_WITH_LZ4:BOOL=ON
BuildOption(conf):  -DARROW_WITH_ZSTD:BOOL=ON
BuildOption(conf):  -DARROW_WITH_BROTLI:BOOL=ON
BuildOption(conf):  -DARROW_WITH_RE2:BOOL=ON
BuildOption(conf):  -DARROW_WITH_UTF8PROC:BOOL=ON
BuildOption(conf):  -DARROW_BUILD_UTILITIES:BOOL=OFF
BuildOption(conf):  -DARROW_USE_JEMALLOC:BOOL=OFF
BuildOption(conf):  -DARROW_USE_MIMALLOC:BOOL=ON
BuildOption(conf):  -DARROW_PYTHON:BOOL=ON
# skips xxhash RVV build failure
BuildOption(conf):  -DCMAKE_CXX_FLAGS_INIT=-DXXH_VECTOR=0
BuildOption(conf):  -S cpp
BuildOption(conf):  -DARROW_BUILD_TESTS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(xsimd)
BuildRequires:  pkgconfig(thrift)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(mimalloc)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(bzip2)
# test Requires
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  python-unversioned-command

%description
Apache Arrow is a universal columnar format and multi-language toolbox for fast
data interchange and in-memory analytics. It defines a language-independent
columnar memory format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware like CPUs and GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and pkg-config files for Apache Arrow.

%prep -a
mkdir %{_builddir}/parquet-testing
mkdir %{_builddir}/arrow-testing
# Extract test data submodules
tar -xf %{SOURCE1} -C %{_builddir}/parquet-testing --strip-components=1
tar -xf %{SOURCE2} -C %{_builddir}/arrow-testing --strip-components=1

%install -a
# Remove libarrow_testing and related files (unnecessary, only needed during build)
rm -rf %{buildroot}%{_libdir}/libarrow_testing.so*
rm -rf %{buildroot}%{_libdir}/cmake/ArrowTesting/
rm -f  %{buildroot}%{_libdir}/pkgconfig/arrow-testing.pc

%check -p
# Set required env vars
export PARQUET_TEST_DATA=%{_builddir}/parquet-testing/data
export ARROW_TEST_DATA=%{_builddir}/arrow-testing/data

%files
%license %{_datadir}/doc/arrow/LICENSE.txt
%doc %{_datadir}/doc/arrow/NOTICE.txt
%doc %{_datadir}/doc/arrow/README.md
%{_libdir}/libarrow.so.*
%{_libdir}/libarrow_acero.so.*
%{_libdir}/libarrow_compute.so.*
%{_libdir}/libarrow_dataset.so.*
%{_libdir}/libparquet.so.*
%{_datadir}/arrow/
%{_datadir}/gdb/auto-load/%{_libdir}/libarrow.so.*

%files devel
%{_includedir}/arrow/
%{_includedir}/parquet/
%{_libdir}/libarrow.so
%{_libdir}/libarrow_acero.so
%{_libdir}/libarrow_compute.so
%{_libdir}/libarrow_dataset.so
%{_libdir}/libparquet.so
%{_libdir}/cmake/Arrow/
%{_libdir}/cmake/ArrowAcero/
%{_libdir}/cmake/ArrowCompute/
%{_libdir}/cmake/ArrowDataset/
%{_libdir}/cmake/Parquet/
%{_libdir}/pkgconfig/arrow.pc
%{_libdir}/pkgconfig/arrow-acero.pc
%{_libdir}/pkgconfig/arrow-compute.pc
%{_libdir}/pkgconfig/arrow-csv.pc
%{_libdir}/pkgconfig/arrow-dataset.pc
%{_libdir}/pkgconfig/arrow-filesystem.pc
%{_libdir}/pkgconfig/arrow-json.pc
%{_libdir}/pkgconfig/parquet.pc

%changelog
%autochangelog
