# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name logos
%global full_version 0.15.1
%global pkgname logos-0.15

Name:           rust-logos-0.15
Version:        0.15.1
Release:        %autorelease
Summary:        Rust crate "logos"
License:        MIT OR Apache-2.0
URL:            https://logos.maciej.codes/
#!RemoteAsset:  sha256:ff472f899b4ec2d99161c51f60ff7075eeb3097069a36050d8037a6325eb8154
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "logos"

%package     -n %{name}+debug
Summary:        Create ridiculously fast Lexers - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-derive-0.15/debug) >= 0.15.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust logos crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Create ridiculously fast Lexers - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/export-derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust logos crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+forbid-unsafe
Summary:        Create ridiculously fast Lexers - feature "forbid_unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-derive-0.15/forbid-unsafe) >= 0.15.1
Provides:       crate(%{pkgname}/forbid-unsafe) = %{version}

%description -n %{name}+forbid-unsafe
This metapackage enables feature "forbid_unsafe" for the Rust logos crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logos-derive
Summary:        Create ridiculously fast Lexers - feature "logos-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-derive-0.15/default) >= 0.15.1
Provides:       crate(%{pkgname}/export-derive) = %{version}
Provides:       crate(%{pkgname}/logos-derive) = %{version}

%description -n %{name}+logos-derive
This metapackage enables feature "logos-derive" for the Rust logos crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "export_derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
