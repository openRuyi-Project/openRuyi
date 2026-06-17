# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vergen-gitcl
%global full_version 9.1.0
%global pkgname vergen-gitcl-9

Name:           rust-vergen-gitcl-9
Version:        9.1.0
Release:        %autorelease
Summary:        Rust crate "vergen-gitcl"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustyhorde/vergen
#!RemoteAsset:  sha256:77ff3b5300a085d6bcd8fc96a507f706a28ae3814693236c9b409db71a1d15b9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.100
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(rustversion-1) >= 1.0.22
Requires:       crate(time-0.3/default) >= 0.3.45
Requires:       crate(time-0.3/formatting) >= 0.3.45
Requires:       crate(time-0.3/local-offset) >= 0.3.45
Requires:       crate(time-0.3/parsing) >= 0.3.45
Requires:       crate(vergen-9) >= 9.1.0
Requires:       crate(vergen-lib-9/default) >= 9.1.0
Requires:       crate(vergen-lib-9/git) >= 9.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vergen-gitcl"

%package     -n %{name}+build
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-9/build) >= 9.1.0
Provides:       crate(%{pkgname}/build) = %{version}

%description -n %{name}+build
This metapackage enables feature "build" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "cargo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-9/cargo) >= 9.1.0
Provides:       crate(%{pkgname}/cargo) = %{version}

%description -n %{name}+cargo
This metapackage enables feature "cargo" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+emit-and-set
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "emit_and_set"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-lib-9/emit-and-set) >= 9.1.0
Requires:       crate(vergen-lib-9/git) >= 9.1.0
Provides:       crate(%{pkgname}/emit-and-set) = %{version}

%description -n %{name}+emit-and-set
This metapackage enables feature "emit_and_set" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "rustc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-9/rustc) >= 9.1.0
Provides:       crate(%{pkgname}/rustc) = %{version}

%description -n %{name}+rustc
This metapackage enables feature "rustc" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+si
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "si"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-9/si) >= 9.1.0
Provides:       crate(%{pkgname}/si) = %{version}

%description -n %{name}+si
This metapackage enables feature "si" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-9/unstable) >= 9.1.0
Requires:       crate(vergen-lib-9/git) >= 9.1.0
Requires:       crate(vergen-lib-9/unstable) >= 9.1.0
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust vergen-gitcl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
