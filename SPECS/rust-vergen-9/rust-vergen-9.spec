# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vergen
%global full_version 9.1.0
%global pkgname vergen-9

Name:           rust-vergen-9
Version:        9.1.0
Release:        %autorelease
Summary:        Rust crate "vergen"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustyhorde/vergen
#!RemoteAsset:  sha256:b849a1f6d8639e8de261e81ee0fc881e3e3620db1af9f2e0da015d4382ceaf75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.100
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(rustversion-1) >= 1.0.22
Requires:       crate(vergen-lib-9/default) >= 9.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vergen"

%package     -n %{name}+build
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(vergen-lib-9/build) >= 9.1.0
Provides:       crate(%{pkgname}/build) = %{version}

%description -n %{name}+build
This metapackage enables feature "build" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "cargo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cargo-metadata) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(vergen-lib-9/cargo) >= 9.1.0
Provides:       crate(%{pkgname}/cargo) = %{version}

%description -n %{name}+cargo
This metapackage enables feature "cargo" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo-metadata
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "cargo_metadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-metadata-0.23/default) >= 0.23.1
Provides:       crate(%{pkgname}/cargo-metadata) = %{version}

%description -n %{name}+cargo-metadata
This metapackage enables feature "cargo_metadata" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+emit-and-set
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "emit_and_set"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-lib-9/emit-and-set) >= 9.1.0
Provides:       crate(%{pkgname}/emit-and-set) = %{version}

%description -n %{name}+emit-and-set
This metapackage enables feature "emit_and_set" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.12.2
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "rustc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustc-version) = %{version}
Requires:       crate(vergen-lib-9/rustc) >= 9.1.0
Provides:       crate(%{pkgname}/rustc) = %{version}

%description -n %{name}+rustc
This metapackage enables feature "rustc" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-version
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "rustc_version"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/rustc-version) = %{version}

%description -n %{name}+rustc-version
This metapackage enables feature "rustc_version" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+si
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "si"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sysinfo) = %{version}
Requires:       crate(vergen-lib-9/si) >= 9.1.0
Provides:       crate(%{pkgname}/si) = %{version}

%description -n %{name}+si
This metapackage enables feature "si" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sysinfo
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "sysinfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sysinfo-0.37/default) >= 0.37.2
Provides:       crate(%{pkgname}/sysinfo) = %{version}

%description -n %{name}+sysinfo
This metapackage enables feature "sysinfo" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.45
Requires:       crate(time-0.3/formatting) >= 0.3.45
Requires:       crate(time-0.3/local-offset) >= 0.3.45
Requires:       crate(time-0.3/parsing) >= 0.3.45
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vergen-lib-9/unstable) >= 9.1.0
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
