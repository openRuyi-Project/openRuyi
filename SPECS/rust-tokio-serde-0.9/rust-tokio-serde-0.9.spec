# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-serde
%global full_version 0.9.0
%global pkgname tokio-serde-0.9

Name:           rust-tokio-serde-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "tokio-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/carllerche/tokio-serde
#!RemoteAsset:  sha256:caf600e7036b17782571dd44fa0a5cea3c82f60db5137f774a325a76a0d6852b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Drop features that depend on unpackaged crates.
Patch2000:      2000-drop-unpackaged-features.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(futures-sink-0.3/default) >= 0.3.0
Requires:       crate(pin-project-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This library is used as a building block for serialization format specific libraries.
Source code for takopackized Rust crate "tokio-serde"

%package     -n %{name}+bincode-crate
Summary:        Send and receive Serde encodable types over the network using Tokio - feature "bincode-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bincode-crate) = %{version}

%description -n %{name}+bincode-crate
This library is used as a building block for serialization format specific libraries.
This metapackage enables feature "bincode-crate" for the Rust tokio-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Send and receive Serde encodable types over the network using Tokio - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This library is used as a building block for serialization format specific libraries.
This metapackage enables feature "serde" for the Rust tokio-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Send and receive Serde encodable types over the network using Tokio - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This library is used as a building block for serialization format specific libraries.
This metapackage enables feature "serde_json" for the Rust tokio-serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
