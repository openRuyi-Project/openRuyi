# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-zigbuild
%global full_version 0.22.3
%global pkgname cargo-zigbuild-0.22

Name:           rust-cargo-zigbuild-0.22
Version:        0.22.3
Release:        %autorelease
Summary:        Rust crate "cargo-zigbuild"
License:        MIT
URL:            https://github.com/rust-cross/cargo-zigbuild
#!RemoteAsset:  sha256:418b19ee36a550c7c34a0bfd04e0b31d0dfb2c92f54aa36189ea3f2f85764845
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.53
Requires:       crate(cargo-config2-0.1/default) >= 0.1.24
Requires:       crate(cargo-metadata-0.23/default) >= 0.23.1
Requires:       crate(cargo-options-0.7/default) >= 0.7.4
Requires:       crate(clap-4/default) >= 4.3.0
Requires:       crate(clap-4/derive) >= 4.3.0
Requires:       crate(clap-4/env) >= 4.3.0
Requires:       crate(clap-4/unstable-styles) >= 4.3.0
Requires:       crate(clap-4/wrap-help) >= 4.3.0
Requires:       crate(crc-3/default) >= 3.2.1
Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(fs-err-3/default) >= 3.0.0
Requires:       crate(goblin-0.10/mach32) >= 0.10.5
Requires:       crate(goblin-0.10/mach64) >= 0.10.5
Requires:       crate(goblin-0.10/std) >= 0.10.5
Requires:       crate(path-slash-0.2/default) >= 0.2.0
Requires:       crate(rustc-version-0.4/default) >= 0.4.0
Requires:       crate(rustflags-0.1/default) >= 0.1.6
Requires:       crate(scroll-0.13/default) >= 0.13.0
Requires:       crate(semver-1/default) >= 1.0.5
Requires:       crate(serde-1/default) >= 1.0.136
Requires:       crate(serde-1/derive) >= 1.0.136
Requires:       crate(serde-json-1/default) >= 1.0.79
Requires:       crate(shell-words-1/default) >= 1.1.1
Requires:       crate(target-lexicon-0.13/default) >= 0.13.0
Requires:       crate(target-lexicon-0.13/std) >= 0.13.0
Requires:       crate(which-8/default) >= 8.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "cargo-zigbuild"

%package     -n %{name}+fat-macho
Summary:        Compile Cargo project with zig as linker - feature "fat-macho" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fat-macho-0.4) >= 0.4.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fat-macho) = %{version}
Provides:       crate(%{pkgname}/universal2) = %{version}

%description -n %{name}+fat-macho
This metapackage enables feature "fat-macho" for the Rust cargo-zigbuild crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "universal2" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
