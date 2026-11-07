# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 0.6.15
%global pkgname serde-0.6

Name:           rust-serde-0.6
Version:        0.6.15
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/serde
#!RemoteAsset:  sha256:c97b18e9e53de541f11e497357d6c5eaeb39f0cb9c8734e274abe4935f6991fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-0.1) >= 0.1.27

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Patch2000:      2000-Specify-a-concrete-compatible-Clippy-dependency.patch

%description
Source code for takopackized Rust crate "serde"

%package     -n %{name}+clippy
Summary:        Generic serialization/deserialization framework - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.166/default) >= 0.0.166
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-testing
Summary:        Generic serialization/deserialization framework - feature "nightly-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/nightly-testing) = %{version}

%description -n %{name}+nightly-testing
This metapackage enables feature "nightly-testing" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Generic serialization/deserialization framework - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-0.1/bigint) >= 0.1.27
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-complex
Summary:        Generic serialization/deserialization framework - feature "num-complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-0.1/complex) >= 0.1.27
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-impls
Summary:        Generic serialization/deserialization framework - feature "num-impls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-bigint) = %{version}
Requires:       crate(%{pkgname}/num-complex) = %{version}
Requires:       crate(%{pkgname}/num-rational) = %{version}
Provides:       crate(%{pkgname}/num-impls) = %{version}

%description -n %{name}+num-impls
This metapackage enables feature "num-impls" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-rational
Summary:        Generic serialization/deserialization framework - feature "num-rational"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-0.1/rational) >= 0.1.27
Provides:       crate(%{pkgname}/num-rational) = %{version}

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
