# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name riscv
%global full_version 0.16.1
%global pkgname riscv-0.16

Name:           rust-riscv-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "riscv"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/riscv
#!RemoteAsset:  sha256:e42cdafa0aa3f0f956b7993cace26de5dafff7bb4f2c5b1dcb2c3723f4267a4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(critical-section-1/default) >= 1.2.0
Requires:       crate(embedded-hal-1/default) >= 1.0.0
Requires:       crate(pastey-0.2/default) >= 0.2.2
Requires:       crate(riscv-types-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/s-mode) = %{version}

%description
Source code for takopackized Rust crate "riscv"

%package     -n %{name}+critical-section-single-hart
Summary:        Low level access to RISC-V processors - feature "critical-section-single-hart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(critical-section-1/restore-state-bool) >= 1.2.0
Provides:       crate(%{pkgname}/critical-section-single-hart) = %{version}

%description -n %{name}+critical-section-single-hart
This metapackage enables feature "critical-section-single-hart" for the Rust riscv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+riscv-macros
Summary:        Low level access to RISC-V processors - feature "riscv-macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(riscv-macros-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/riscv-macros) = %{version}

%description -n %{name}+riscv-macros
This metapackage enables feature "riscv-macros" for the Rust riscv crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+rt
Summary:        Low level access to RISC-V processors - feature "rt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(riscv-macros-0.4/rt) >= 0.4.1
Provides:       crate(%{pkgname}/rt) = %{version}

%description -n %{name}+rt
This metapackage enables feature "rt" for the Rust riscv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-v-trap
Summary:        Low level access to RISC-V processors - feature "rt-v-trap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(riscv-macros-0.4/rt-v-trap) >= 0.4.1
Provides:       crate(%{pkgname}/rt-v-trap) = %{version}

%description -n %{name}+rt-v-trap
This metapackage enables feature "rt-v-trap" for the Rust riscv crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
