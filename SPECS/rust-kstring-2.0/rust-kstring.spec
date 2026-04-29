# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kstring
%global full_version 2.0.2
%global pkgname kstring-2.0

Name:           rust-kstring-2.0
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "kstring"
License:        MIT OR Apache-2.0
URL:            https://github.com/cobalt-org/kstring
#!RemoteAsset:  sha256:558bf9508a558512042d3095138b1f7b8fe90c5467d94f9f1da28b3731c5dbd1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(static-assertions-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arc)
Provides:       crate(%{pkgname}/max-inline)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unsafe)
Provides:       crate(%{pkgname}/unstable-bench-subset)

%description
Source code for takopackized Rust crate "kstring"

%package     -n %{name}+default
Summary:        Key String: optimized for map keys - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unsafe)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust kstring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Key String: optimized for map keys - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust kstring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Key String: optimized for map keys - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust kstring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
