# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name markdown
%global full_version 1.0.0
%global pkgname markdown-1.0

Name:           rust-markdown-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "markdown"
License:        MIT
URL:            https://github.com/wooorm/markdown-rs
#!RemoteAsset:  sha256:a5cab8f2cadc416a82d2e783a1946388b31654d391d1c7d92cc1f03e295b1deb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-id-0.3/default) >= 0.3.6
Requires:       crate(unicode-id-0.3/no-std) >= 0.3.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "markdown"

%package     -n %{name}+log
Summary:        CommonMark compliant markdown parser in Rust with ASTs and extensions - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust markdown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        CommonMark compliant markdown parser in Rust with ASTs and extensions - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/json)
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust markdown crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
