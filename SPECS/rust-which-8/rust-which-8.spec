# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 8.0.2
%global pkgname which-8

Name:           rust-which-8
Version:        8.0.2
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/harryfei/which-rs.git
#!RemoteAsset:  sha256:81995fafaaaf6ae47a7d0cc83c67caf92aeb7e5331650ae6ff856f7c0c60c459
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Locate installed executable in cross platforms.
Source code for takopackized Rust crate "which"

%package     -n %{name}+real-sys
Summary:        Rust equivalent of Unix command "which" - feature "real-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/real-sys) = %{version}

%description -n %{name}+real-sys
Locate installed executable in cross platforms.
This metapackage enables feature "real-sys" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+regex
Summary:        Rust equivalent of Unix command "which" - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.10.2
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
Locate installed executable in cross platforms.
This metapackage enables feature "regex" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Rust equivalent of Unix command "which" - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
Locate installed executable in cross platforms.
This metapackage enables feature "tracing" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
