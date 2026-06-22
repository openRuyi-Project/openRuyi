# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chumsky
%global full_version 0.9.3
%global pkgname chumsky-0.9

Name:           rust-chumsky-0.9
Version:        0.9.3
Release:        %autorelease
Summary:        Rust crate "chumsky"
License:        MIT
URL:            https://github.com/zesterer/chumsky
#!RemoteAsset:  sha256:8eebd66744a15ded14960ab4ccdbfb51ad3b81f51f3f04a80adac98c985396c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.14/default) >= 0.14.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ahash) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "chumsky"

%package     -n %{name}+default
Summary:        Parser library for humans with powerful error recovery - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/spill-stack) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spill-stack
Summary:        Parser library for humans with powerful error recovery - feature "spill-stack"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/stacker) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/spill-stack) = %{version}

%description -n %{name}+spill-stack
This metapackage enables feature "spill-stack" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stacker
Summary:        Parser library for humans with powerful error recovery - feature "stacker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stacker-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/stacker) = %{version}

%description -n %{name}+stacker
This metapackage enables feature "stacker" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
