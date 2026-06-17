# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ndarray
%global full_version 0.16.1
%global pkgname ndarray-0.16

Name:           rust-ndarray-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "ndarray"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-ndarray/ndarray
#!RemoteAsset:  sha256:882ed72dce9365842bf196bdeedf5055305f11fc8c03dee7bb0194a6cad34841
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(matrixmultiply-0.3/cgemm) >= 0.3.2
Requires:       crate(num-complex-0.4) >= 0.4.0
Requires:       crate(num-integer-0.1) >= 0.1.39
Requires:       crate(num-traits-0.2) >= 0.2.0
Requires:       crate(portable-atomic-1/default) >= 1.6.0
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.0
Requires:       crate(portable-atomic-util-0.2/default) >= 0.2.0
Requires:       crate(rawpointer-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Lightweight array views and slicing; views support chunking and splitting.
Source code for takopackized Rust crate "ndarray"

%package     -n %{name}+approx
Summary:        N-dimensional array for general elements and for numerics - feature "approx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(approx-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/approx) = %{version}

%description -n %{name}+approx
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "approx" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blas
Summary:        N-dimensional array for general elements and for numerics - feature "blas"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cblas-sys-0.1) >= 0.1.4
Requires:       crate(libc-0.2/default) >= 0.2.82
Provides:       crate(%{pkgname}/blas) = %{version}

%description -n %{name}+blas
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "blas" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+docs
Summary:        N-dimensional array for general elements and for numerics - feature "docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/approx) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/docs) = %{version}

%description -n %{name}+docs
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "docs" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+matrixmultiply-threading
Summary:        N-dimensional array for general elements and for numerics - feature "matrixmultiply-threading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(matrixmultiply-0.3/cgemm) >= 0.3.2
Requires:       crate(matrixmultiply-0.3/threading) >= 0.3.2
Provides:       crate(%{pkgname}/matrixmultiply-threading) = %{version}

%description -n %{name}+matrixmultiply-threading
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "matrixmultiply-threading" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-critical-section
Summary:        N-dimensional array for general elements and for numerics - feature "portable-atomic-critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/critical-section) >= 1.6.0
Provides:       crate(%{pkgname}/portable-atomic-critical-section) = %{version}

%description -n %{name}+portable-atomic-critical-section
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "portable-atomic-critical-section" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        N-dimensional array for general elements and for numerics - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "rayon" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        N-dimensional array for general elements and for numerics - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "serde" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-1" feature.

%package     -n %{name}+std
Summary:        N-dimensional array for general elements and for numerics - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(matrixmultiply-0.3/cgemm) >= 0.3.2
Requires:       crate(matrixmultiply-0.3/std) >= 0.3.2
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Lightweight array views and slicing; views support chunking and splitting.
This metapackage enables feature "std" for the Rust ndarray crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
