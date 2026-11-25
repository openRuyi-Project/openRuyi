# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name include_dir
%global full_version 0.7.4
%global pkgname include-dir-0.7

Name:           rust-include-dir-0.7
Version:        0.7.4
Release:        %autorelease
Summary:        Rust crate "include_dir"
License:        MIT
URL:            https://github.com/Michael-F-Bryan/include_dir
#!RemoteAsset:  sha256:923d117408f1e49d914f1a379a309cffe4f18c05cf4e3d12e613a15fc81bd0dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(include-dir-macros-0.7/default) >= 0.7.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "include_dir"

%package     -n %{name}+glob
Summary:        Embed the contents of a directory in your binary - feature "glob"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glob-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/glob) = %{version}

%description -n %{name}+glob
This metapackage enables feature "glob" for the Rust include_dir crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metadata
Summary:        Embed the contents of a directory in your binary - feature "metadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-dir-macros-0.7/metadata) >= 0.7.4
Provides:       crate(%{pkgname}/metadata) = %{version}

%description -n %{name}+metadata
This metapackage enables feature "metadata" for the Rust include_dir crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Embed the contents of a directory in your binary - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-dir-macros-0.7/nightly) >= 0.7.4
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust include_dir crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
