# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clang-sys
%global full_version 0.26.4
%global pkgname clang-sys-0.26

Name:           rust-clang-sys-0.26
Version:        0.26.4
Release:        %autorelease
Summary:        Rust crate "clang-sys"
License:        Apache-2.0
URL:            https://github.com/KyleMayes/clang-sys
#!RemoteAsset:  sha256:6ef0c1bcf2e99c649104bd7a7012d8f8802684400e03db0ec0af48583c6fa0e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glob-0.2) >= 0.2.11
Requires:       crate(glob-0.2/default) >= 0.2.11
Requires:       crate(libc-0.2) >= 0.2.39

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clang-3-5) = %{version}
Provides:       crate(%{pkgname}/clang-3-6) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Provides:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Provides:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Provides:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Provides:       crate(%{pkgname}/gte-clang-4-0) = %{version}
Provides:       crate(%{pkgname}/gte-clang-5-0) = %{version}
Provides:       crate(%{pkgname}/gte-clang-6-0) = %{version}
Provides:       crate(%{pkgname}/gte-clang-7-0) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}

%description
Source code for takopackized Rust crate "clang-sys"

%package     -n %{name}+clang-3-7
Summary:        Rust bindings for libclang - feature "clang_3_7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Provides:       crate(%{pkgname}/clang-3-7) = %{version}

%description -n %{name}+clang-3-7
This metapackage enables feature "clang_3_7" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-8
Summary:        Rust bindings for libclang - feature "clang_3_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Provides:       crate(%{pkgname}/clang-3-8) = %{version}

%description -n %{name}+clang-3-8
This metapackage enables feature "clang_3_8" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-9
Summary:        Rust bindings for libclang - feature "clang_3_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Provides:       crate(%{pkgname}/clang-3-9) = %{version}

%description -n %{name}+clang-3-9
This metapackage enables feature "clang_3_9" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-4-0
Summary:        Rust bindings for libclang - feature "clang_4_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Requires:       crate(%{pkgname}/gte-clang-4-0) = %{version}
Provides:       crate(%{pkgname}/clang-4-0) = %{version}

%description -n %{name}+clang-4-0
This metapackage enables feature "clang_4_0" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-5-0
Summary:        Rust bindings for libclang - feature "clang_5_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Requires:       crate(%{pkgname}/gte-clang-4-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-5-0) = %{version}
Provides:       crate(%{pkgname}/clang-5-0) = %{version}

%description -n %{name}+clang-5-0
This metapackage enables feature "clang_5_0" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-6-0
Summary:        Rust bindings for libclang - feature "clang_6_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Requires:       crate(%{pkgname}/gte-clang-4-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-5-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-6-0) = %{version}
Provides:       crate(%{pkgname}/clang-6-0) = %{version}

%description -n %{name}+clang-6-0
This metapackage enables feature "clang_6_0" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-7-0
Summary:        Rust bindings for libclang - feature "clang_7_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-6) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-7) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-8) = %{version}
Requires:       crate(%{pkgname}/gte-clang-3-9) = %{version}
Requires:       crate(%{pkgname}/gte-clang-4-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-5-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-6-0) = %{version}
Requires:       crate(%{pkgname}/gte-clang-7-0) = %{version}
Provides:       crate(%{pkgname}/clang-7-0) = %{version}

%description -n %{name}+clang-7-0
This metapackage enables feature "clang_7_0" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libloading
Summary:        Rust bindings for libclang - feature "libloading" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/libloading) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
