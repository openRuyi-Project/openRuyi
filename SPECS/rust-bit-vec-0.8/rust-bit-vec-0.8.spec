# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit-vec
%global full_version 0.8.0
%global pkgname bit-vec-0.8

Name:           rust-bit-vec-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "bit-vec"
License:        Apache-2.0 OR MIT
URL:            https://github.com/contain-rs/bit-vec
#!RemoteAsset:  sha256:5e764a1d40d510daf35e07be9eb06e75770908c27d411ee6c92109c9840eaaf7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bit-vec"

%package     -n %{name}+borsh
Summary:        Vector of bits - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1/derive) >= 1.5.0
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh-std
Summary:        Vector of bits - feature "borsh_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1/derive) >= 1.5.0
Requires:       crate(borsh-1/std) >= 1.5.0
Provides:       crate(%{pkgname}/borsh-std) = %{version}

%description -n %{name}+borsh-std
This metapackage enables feature "borsh_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miniserde
Summary:        Vector of bits - feature "miniserde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(miniserde-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/miniserde) = %{version}

%description -n %{name}+miniserde
This metapackage enables feature "miniserde" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nanoserde
Summary:        Vector of bits - feature "nanoserde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nanoserde-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/nanoserde) = %{version}

%description -n %{name}+nanoserde
This metapackage enables feature "nanoserde" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Vector of bits - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-no-std
Summary:        Vector of bits - feature "serde_no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde-no-std) = %{version}

%description -n %{name}+serde-no-std
This metapackage enables feature "serde_no_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-std
Summary:        Vector of bits - feature "serde_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-std) = %{version}

%description -n %{name}+serde-std
This metapackage enables feature "serde_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
