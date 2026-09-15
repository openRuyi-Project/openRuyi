# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lingcage
%global full_version 0.2.0
%global pkgname lingcage-0.2

Name:           rust-lingcage-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "lingcage"
License:        Apache-2.0
URL:            https://lingcage.com
#!RemoteAsset:  sha256:470d09558753474b2f4ecd3eeb4364a0ac91e483700cbf02d362333e0dec88c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for the Rust crate "lingcage"

%package     -n %{name}+agent
Summary:        Secure agent infrastructure that cages AI agents with minimum overhead - feature "agent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lcp) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Provides:       crate(%{pkgname}/agent) = %{version}

%description -n %{name}+agent
This metapackage enables feature "agent" for the Rust lingcage crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lcp
Summary:        Secure agent infrastructure that cages AI agents with minimum overhead - feature "lcp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(thiserror-2/default) >= 2.0.18
Provides:       crate(%{pkgname}/lcp) = %{version}

%description -n %{name}+lcp
This metapackage enables feature "lcp" for the Rust lingcage crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+template
Summary:        Secure agent infrastructure that cages AI agents with minimum overhead - feature "template" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lcp) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(lingcore-0.2/default) >= 0.2.0
Requires:       crate(lingcore-0.2/kvm) >= 0.2.0
Requires:       crate(lingcore-0.2/machine) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(sha2-0.10/default) >= 0.10.9
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/sandbox) = %{version}
Provides:       crate(%{pkgname}/template) = %{version}

%description -n %{name}+template
This metapackage enables feature "template" for the Rust lingcage crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cli", and "sandbox" features.

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
