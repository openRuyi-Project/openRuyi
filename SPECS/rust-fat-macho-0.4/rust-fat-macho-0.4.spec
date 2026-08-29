# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fat-macho
%global full_version 0.4.11
%global pkgname fat-macho-0.4

Name:           rust-fat-macho-0.4
Version:        0.4.11
Release:        %autorelease
Summary:        Rust crate "fat-macho"
License:        MIT
URL:            https://github.com/messense/fat-macho-rs.git
#!RemoteAsset:  sha256:bed3960cfd332df43d86b2ae31bfed07a7b727a6170ae65dddc342775e810ca7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(goblin-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "fat-macho"

%package     -n %{name}+llvm-bitcode
Summary:        Mach-O Fat Binary Reader and Writer - feature "llvm-bitcode" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(llvm-bitcode-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bitcode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/llvm-bitcode) = %{version}

%description -n %{name}+llvm-bitcode
This metapackage enables feature "llvm-bitcode" for the Rust fat-macho crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bitcode", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
