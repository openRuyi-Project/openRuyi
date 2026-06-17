# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519-compact
%global full_version 2.2.0
%global pkgname ed25519-compact-2

Name:           rust-ed25519-compact-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "ed25519-compact"
License:        MIT
URL:            https://github.com/jedisct1/rust-ed25519-compact
#!RemoteAsset:  sha256:33ce99a9e19c84beb4cc35ece85374335ccc398240712114c85038319ed709bd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/blind-keys) = %{version}
Provides:       crate(%{pkgname}/disable-signatures) = %{version}
Provides:       crate(%{pkgname}/opt-size) = %{version}
Provides:       crate(%{pkgname}/self-verify) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/x25519) = %{version}

%description
Source code for takopackized Rust crate "ed25519-compact"

%package     -n %{name}+ct-codecs
Summary:        Small, self-contained, wasm-friendly Ed25519 implementation - feature "ct-codecs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ct-codecs-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/ct-codecs) = %{version}
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+ct-codecs
This metapackage enables feature "ct-codecs" for the Rust ed25519-compact crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "pem" feature.

%package     -n %{name}+default
Summary:        Small, self-contained, wasm-friendly Ed25519 implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/random) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/x25519) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ed25519-compact crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ed25519
Summary:        Small, self-contained, wasm-friendly Ed25519 implementation - feature "ed25519" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/ed25519) = %{version}
Provides:       crate(%{pkgname}/traits) = %{version}

%description -n %{name}+ed25519
This metapackage enables feature "ed25519" for the Rust ed25519-compact crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "traits" feature.

%package     -n %{name}+getrandom
Summary:        Small, self-contained, wasm-friendly Ed25519 implementation - feature "getrandom" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/default) >= 0.3.0
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ed25519-compact crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "random" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
