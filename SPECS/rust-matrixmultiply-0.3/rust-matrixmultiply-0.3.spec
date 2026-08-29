# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matrixmultiply
%global full_version 0.3.10
%global pkgname matrixmultiply-0.3

Name:           rust-matrixmultiply-0.3
Version:        0.3.10
Release:        %autorelease
Summary:        Rust crate "matrixmultiply"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/matrixmultiply/
#!RemoteAsset:  sha256:a06de3016e9fae57a36fd14dba131fccf49f74b40b7fbdb472f96e361ec71a08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(rawpointer-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cgemm) = %{version}
Provides:       crate(%{pkgname}/constconf) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Operates on matrices with general layout (they can use arbitrary row and column stride). Detects and uses AVX or SSE2 on x86 platforms transparently for higher performance. Uses a microkernel strategy, so that the implementation is easy to parallelize and optimize.
Supports multithreading.
Source code for takopackized Rust crate "matrixmultiply"

%package     -n %{name}+num-cpus
Summary:        General matrix multiplication for f32 and f64 matrices - feature "num_cpus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-cpus-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/num-cpus) = %{version}

%description -n %{name}+num-cpus
Operates on matrices with general layout (they can use arbitrary row and column stride). Detects and uses AVX or SSE2 on x86 platforms transparently for higher performance. Uses a microkernel strategy, so that the implementation is easy to parallelize and optimize.
Supports multithreading.
This metapackage enables feature "num_cpus" for the Rust matrixmultiply crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        General matrix multiplication for f32 and f64 matrices - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
Operates on matrices with general layout (they can use arbitrary row and column stride). Detects and uses AVX or SSE2 on x86 platforms transparently for higher performance. Uses a microkernel strategy, so that the implementation is easy to parallelize and optimize.
Supports multithreading.
This metapackage enables feature "once_cell" for the Rust matrixmultiply crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-tree
Summary:        General matrix multiplication for f32 and f64 matrices - feature "thread-tree"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thread-tree-0.3/default) >= 0.3.2
Provides:       crate(%{pkgname}/thread-tree) = %{version}

%description -n %{name}+thread-tree
Operates on matrices with general layout (they can use arbitrary row and column stride). Detects and uses AVX or SSE2 on x86 platforms transparently for higher performance. Uses a microkernel strategy, so that the implementation is easy to parallelize and optimize.
Supports multithreading.
This metapackage enables feature "thread-tree" for the Rust matrixmultiply crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+threading
Summary:        General matrix multiplication for f32 and f64 matrices - feature "threading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-cpus) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/thread-tree) = %{version}
Provides:       crate(%{pkgname}/threading) = %{version}

%description -n %{name}+threading
Operates on matrices with general layout (they can use arbitrary row and column stride). Detects and uses AVX or SSE2 on x86 platforms transparently for higher performance. Uses a microkernel strategy, so that the implementation is easy to parallelize and optimize.
Supports multithreading.
This metapackage enables feature "threading" for the Rust matrixmultiply crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
