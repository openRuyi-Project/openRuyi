# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name timeago
%global full_version 0.6.1
%global pkgname timeago-0.6

Name:           rust-timeago-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "timeago"
License:        MIT OR Apache-2.0
URL:            https://github.com/vi/timeago
#!RemoteAsset:  sha256:46c29b13d230e9cd58513d38701a661fc06e1215398937532a2d938ecca6f219
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/translations) = %{version}

%description
Parsing it back to Duration is not supported yet.
Source code for takopackized Rust crate "timeago"

%package     -n %{name}+chrono
Summary:        Given a Duration, lossily format it like in 'N days ago' - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Parsing it back to Duration is not supported yet.
This metapackage enables feature "chrono" for the Rust timeago crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Given a Duration, lossily format it like in 'N days ago' - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/isolang) = %{version}
Requires:       crate(%{pkgname}/translations) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Parsing it back to Duration is not supported yet.
This metapackage enables feature "default" for the Rust timeago crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+isolang
Summary:        Given a Duration, lossily format it like in 'N days ago' - feature "isolang"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(isolang-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/isolang) = %{version}

%description -n %{name}+isolang
Parsing it back to Duration is not supported yet.
This metapackage enables feature "isolang" for the Rust timeago crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
