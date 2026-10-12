# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name riscv-macros
%global full_version 0.4.1
%global pkgname riscv-macros-0.4

Name:           rust-riscv-macros-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "riscv-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/riscv
#!RemoteAsset:  sha256:6ad9f6dda08d90d091bc0743967cab369b8fe39ea74b26783ba2ca5c0ce39e86
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rt) = %{version}
Provides:       crate(%{pkgname}/rt-v-trap) = %{version}
Provides:       crate(%{pkgname}/s-mode) = %{version}

%description
Source code for takopackized Rust crate "riscv-macros"

%package     -n %{name}+riscv-rt
Summary:        Procedural macros re-exported in `riscv` - feature "riscv-rt" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}/riscv-rt) = %{version}
Provides:       crate(%{pkgname}/rvrt-pre-default-start-trap) = %{version}
Provides:       crate(%{pkgname}/rvrt-u-boot) = %{version}

%description -n %{name}+riscv-rt
This metapackage enables feature "riscv-rt" for the Rust riscv-macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rvrt-pre-default-start-trap", and "rvrt-u-boot" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
