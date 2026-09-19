# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getopts
%global full_version 0.2.24
%global pkgname getopts-0.2

Name:           rust-getopts-0.2
Version:        0.2.24
Release:        %autorelease
Summary:        Rust crate "getopts"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/getopts
#!RemoteAsset:  sha256:cfe4fbac503b8d1f88e6676011885f34b7174f46e59956bba534ba83abded4df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "getopts"

%package     -n %{name}+rustc-dep-of-std
Summary:        Getopts-like option parsing - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Getopts-like option parsing - feature "unicode" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
